/*
 * Agent.cpp
 * RVO2 Library
 *
 * Copyright 2008 University of North Carolina at Chapel Hill
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Please send all bug reports to <geom@cs.unc.edu>.
 *
 * The authors may be contacted via:
 *
 * Jur van den Berg, Stephen J. Guy, Jamie Snape, Ming C. Lin, Dinesh Manocha
 * Dept. of Computer Science
 * 201 S. Columbia St.
 * Frederick P. Brooks, Jr. Computer Science Bldg.
 * Chapel Hill, N.C. 27599-3175
 * United States of America
 *
 * <http://gamma.cs.unc.edu/RVO2/>
 */

#include "Agent.h"

#include "KdTree.h"
#include "Obstacle.h"

namespace RVO {
Agent::Agent(RVOSimulator* sim) : maxNeighbors_(0), maxSpeed_(0.0), neighborDist_(0.0), radius_(0.0), sim_(sim), timeHorizon_(0.0), timeHorizonObst_(0.0), id_(0), lambda(0.5f) { }

void Agent::computeNeighbors() {
  obstacleNeighbors_.clear();
  double rangeSq = sqr(timeHorizonObst_ * maxSpeed_ + radius_) + sim_->d0;
  sim_->kdTree_->computeObstacleNeighbors(this, rangeSq);

  agentNeighbors_.clear();

  if(maxNeighbors_ > 0) {
    rangeSq = sim_->d0 + sqr(timeHorizon_ * maxSpeed_ + 2 * radius_);
    sim_->kdTree_->computeAgentNeighbors(this, rangeSq);
  }
}

/* Search for the best new velocity. */
void Agent::computeNewVelocity() {
  orcaLines_.clear();

  const double invTimeHorizonObst = 1.0f / timeHorizonObst_;

  /* Create obstacle ORCA lines. */
  for (size_t i = 0; i < obstacleNeighbors_.size(); ++i) {

    const Obstacle* obstacle1 = obstacleNeighbors_[i].second;
    const Obstacle* obstacle2 = obstacle1->nextObstacle_;

    const Vector2 relativePosition1 = obstacle1->point_ - position_;
    const Vector2 relativePosition2 = obstacle2->point_ - position_;

    /*
     * Check if velocity obstacle of obstacle is already taken care of by
     * previously constructed obstacle ORCA lines.
     */
    bool alreadyCovered = false;

    for (size_t j = 0; j < orcaLines_.size(); ++j) {
      if (det(invTimeHorizonObst * relativePosition1 - orcaLines_[j].point, orcaLines_[j].direction) - invTimeHorizonObst * radius_ >= -RVO_EPSILON && det(invTimeHorizonObst * relativePosition2 - orcaLines_[j].point, orcaLines_[j].direction) - invTimeHorizonObst * radius_ >= -RVO_EPSILON) {
        alreadyCovered = true;
        break;
      }
    }

    if (alreadyCovered) {
      continue;
    }

    /* Not yet covered. Check for collisions. */

    const double distSq1 = absSq(relativePosition1);
    const double distSq2 = absSq(relativePosition2);

    const double radiusSq = sqr(radius_);

    const Vector2 obstacleVector = obstacle2->point_ - obstacle1->point_;
    const double s = (-relativePosition1 * obstacleVector) / absSq(obstacleVector);
    const double distSqLine = absSq(-relativePosition1 - s * obstacleVector);

    Line line;

    if (s < 0.0 && distSq1 <= radiusSq) {
      /* Collision with left vertex. Ignore if non-convex. */
      if (obstacle1->isConvex_) {
        line.point = Vector2(0.0, 0.0);
        line.direction = normalize(Vector2(-relativePosition1.y(), relativePosition1.x()));
        orcaLines_.push_back(line);
      }

      continue;
    } else if (s > 1.0f && distSq2 <= radiusSq) {
      /* Collision with right vertex. Ignore if non-convex
       * or if it will be taken care of by neighoring obstace */
      if (obstacle2->isConvex_ && det(relativePosition2, obstacle2->unitDir_) >= 0.0) {
        line.point = Vector2(0.0, 0.0);
        line.direction = normalize(Vector2(-relativePosition2.y(), relativePosition2.x()));
        orcaLines_.push_back(line);
      }

      continue;
    } else if (s >= 0.0 && s < 1.0f && distSqLine <= radiusSq) {
      /* Collision with obstacle segment. */
      line.point = Vector2(0.0, 0.0);
      line.direction = -obstacle1->unitDir_;
      orcaLines_.push_back(line);
      continue;
    }

    /*
     * No collision.
     * Compute legs. When obliquely viewed, both legs can come from a single
     * vertex. Legs extend cut-off line when nonconvex vertex.
     */

    Vector2 leftLegDirection, rightLegDirection;

    if (s < 0.0 && distSqLine <= radiusSq) {
      /*
       * Obstacle viewed obliquely so that left vertex
       * defines velocity obstacle.
       */
      if (!obstacle1->isConvex_) {
        /* Ignore obstacle. */
        continue;
      }

      obstacle2 = obstacle1;

      const double leg1 = std::sqrt(distSq1 - radiusSq);
      leftLegDirection = Vector2(relativePosition1.x() * leg1 - relativePosition1.y() * radius_, relativePosition1.x() * radius_ + relativePosition1.y() * leg1) / distSq1;
      rightLegDirection = Vector2(relativePosition1.x() * leg1 + relativePosition1.y() * radius_, -relativePosition1.x() * radius_ + relativePosition1.y() * leg1) / distSq1;
    } else if (s > 1.0f && distSqLine <= radiusSq) {
      /*
       * Obstacle viewed obliquely so that
       * right vertex defines velocity obstacle.
       */
      if (!obstacle2->isConvex_) {
        /* Ignore obstacle. */
        continue;
      }

      obstacle1 = obstacle2;

      const double leg2 = std::sqrt(distSq2 - radiusSq);
      leftLegDirection = Vector2(relativePosition2.x() * leg2 - relativePosition2.y() * radius_, relativePosition2.x() * radius_ + relativePosition2.y() * leg2) / distSq2;
      rightLegDirection = Vector2(relativePosition2.x() * leg2 + relativePosition2.y() * radius_, -relativePosition2.x() * radius_ + relativePosition2.y() * leg2) / distSq2;
    } else {
      /* Usual situation. */
      if (obstacle1->isConvex_) {
        const double leg1 = std::sqrt(distSq1 - radiusSq);
        leftLegDirection = Vector2(relativePosition1.x() * leg1 - relativePosition1.y() * radius_, relativePosition1.x() * radius_ + relativePosition1.y() * leg1) / distSq1;
      } else {
        /* Left vertex non-convex; left leg extends cut-off line. */
        leftLegDirection = -obstacle1->unitDir_;
      }

      if (obstacle2->isConvex_) {
        const double leg2 = std::sqrt(distSq2 - radiusSq);
        rightLegDirection = Vector2(relativePosition2.x() * leg2 + relativePosition2.y() * radius_, -relativePosition2.x() * radius_ + relativePosition2.y() * leg2) / distSq2;
      } else {
        /* Right vertex non-convex; right leg extends cut-off line. */
        rightLegDirection = obstacle1->unitDir_;
      }
    }

    /*
     * Legs can never point into neighboring edge when convex vertex,
     * take cutoff-line of neighboring edge instead. If velocity projected on
     * "foreign" leg, no constraint is added.
     */

    const Obstacle* const leftNeighbor = obstacle1->prevObstacle_;

    bool isLeftLegForeign = false;
    bool isRightLegForeign = false;

    if (obstacle1->isConvex_ && det(leftLegDirection, -leftNeighbor->unitDir_) >= 0.0) {
      /* Left leg points into obstacle. */
      leftLegDirection = -leftNeighbor->unitDir_;
      isLeftLegForeign = true;
    }

    if (obstacle2->isConvex_ && det(rightLegDirection, obstacle2->unitDir_) <= 0.0) {
      /* Right leg points into obstacle. */
      rightLegDirection = obstacle2->unitDir_;
      isRightLegForeign = true;
    }

    /* Compute cut-off centers. */
    const Vector2 leftCutoff = invTimeHorizonObst * (obstacle1->point_ - position_);
    const Vector2 rightCutoff = invTimeHorizonObst * (obstacle2->point_ - position_);
    const Vector2 cutoffVec = rightCutoff - leftCutoff;

    /* Project current velocity on velocity obstacle. */

    /* Check if current velocity is projected on cutoff circles. */
    const double t = (obstacle1 == obstacle2 ? 0.5f : ((velocity_ - leftCutoff) * cutoffVec) / absSq(cutoffVec));
    const double tLeft = ((velocity_ - leftCutoff) * leftLegDirection);
    const double tRight = ((velocity_ - rightCutoff) * rightLegDirection);

    if ((t < 0.0 && tLeft < 0.0) || (obstacle1 == obstacle2 && tLeft < 0.0 && tRight < 0.0)) {
      /* Project on left cut-off circle. */
      const Vector2 unitW = normalize(velocity_ - leftCutoff);

      line.direction = Vector2(unitW.y(), -unitW.x());
      line.point = leftCutoff + radius_ * invTimeHorizonObst * unitW;
      orcaLines_.push_back(line);
      continue;
    } else if (t > 1.0f && tRight < 0.0) {
      /* Project on right cut-off circle. */
      const Vector2 unitW = normalize(velocity_ - rightCutoff);

      line.direction = Vector2(unitW.y(), -unitW.x());
      line.point = rightCutoff + radius_ * invTimeHorizonObst * unitW;
      orcaLines_.push_back(line);
      continue;
    }

    /*
     * Project on left leg, right leg, or cut-off line, whichever is closest
     * to velocity.
     */
    const double distSqCutoff = ((t < 0.0 || t > 1.0f || obstacle1 == obstacle2) ? std::numeric_limits<double>::infinity() : absSq(velocity_ - (leftCutoff + t * cutoffVec)));
    const double distSqLeft = ((tLeft < 0.0) ? std::numeric_limits<double>::infinity() : absSq(velocity_ - (leftCutoff + tLeft * leftLegDirection)));
    const double distSqRight = ((tRight < 0.0) ? std::numeric_limits<double>::infinity() : absSq(velocity_ - (rightCutoff + tRight * rightLegDirection)));

    if (distSqCutoff <= distSqLeft && distSqCutoff <= distSqRight) {
      /* Project on cut-off line. */
      line.direction = -obstacle1->unitDir_;
      line.point = leftCutoff + radius_ * invTimeHorizonObst * Vector2(-line.direction.y(), line.direction.x());
      orcaLines_.push_back(line);
      continue;
    } else if (distSqLeft <= distSqRight) {
      /* Project on left leg. */
      if (isLeftLegForeign) {
        continue;
      }

      line.direction = leftLegDirection;
      line.point = leftCutoff + radius_ * invTimeHorizonObst * Vector2(-line.direction.y(), line.direction.x());
      orcaLines_.push_back(line);
      continue;
    } else {
      /* Project on right leg. */
      if (isRightLegForeign) {
        continue;
      }

      line.direction = -rightLegDirection;
      line.point = rightCutoff + radius_ * invTimeHorizonObst * Vector2(-line.direction.y(), line.direction.x());
      orcaLines_.push_back(line);
      continue;
    }
  }

  const size_t numObstLines = orcaLines_.size();

  const double invTimeHorizon = 1.0f / timeHorizon_;

  /* Create agent ORCA lines. */
  for (size_t i = 0; i < agentNeighbors_.size(); ++i) {
    const Agent* const other = agentNeighbors_[i].second;

    const Vector2 relativePosition = other->position_ - position_;
    const Vector2 relativeVelocity = velocity_ - other->velocity_;
    const double distSq = absSq(relativePosition);
    const double combinedRadius = radius_ + other->radius_;
    const double combinedRadiusSq = sqr(combinedRadius);

    Line line;
    Vector2 u;

    if (distSq > combinedRadiusSq) {
      /* No collision. */
      const Vector2 w = relativeVelocity - invTimeHorizon * relativePosition;
      /* Vector from cutoff center to relative velocity. */
      const double wLengthSq = absSq(w);

      const double dotProduct1 = w * relativePosition;

      if (dotProduct1 < 0.0 && sqr(dotProduct1) > combinedRadiusSq * wLengthSq) {
        /* Project on cut-off circle. */
        const double wLength = std::sqrt(wLengthSq);
        const Vector2 unitW = w / wLength;

        line.direction = Vector2(unitW.y(), -unitW.x());
        u = (combinedRadius * invTimeHorizon - wLength) * unitW;
      } else {
        /* Project on legs. */
        const double leg = std::sqrt(distSq - combinedRadiusSq);

        if (det(relativePosition, w) > 0.0) {
          /* Project on left leg. */
          line.direction = Vector2(relativePosition.x() * leg - relativePosition.y() * combinedRadius, relativePosition.x() * combinedRadius + relativePosition.y() * leg) / distSq;
        } else {
          /* Project on right leg. */
          line.direction = -Vector2(relativePosition.x() * leg + relativePosition.y() * combinedRadius, -relativePosition.x() * combinedRadius + relativePosition.y() * leg) / distSq;
        }

        const double dotProduct2 = relativeVelocity * line.direction;

        u = dotProduct2 * line.direction - relativeVelocity;
      }
    } else {
      /* Collision. Project on cut-off circle of time timeStep. */
      const double invTimeStep = 1.0f / sim_->timeStep_;

      /* Vector from cutoff center to relative velocity. */
      const Vector2 w = relativeVelocity - invTimeStep * relativePosition;

      const double wLength = abs(w);
      const Vector2 unitW = w / wLength;

      line.direction = Vector2(unitW.y(), -unitW.x());
      u = (combinedRadius * invTimeStep - wLength) * unitW;
    }

    line.point = velocity_ + (1 - other->lambda) * u;
    orcaLines_.push_back(line);
  }

  size_t lineFail = linearProgram2(orcaLines_, maxSpeed_, prefVelocity_, false, newVelocity_);

  if (lineFail < orcaLines_.size()) {
    linearProgram3(orcaLines_, numObstLines, lineFail, maxSpeed_, newVelocity_);
  }
}

void Agent::insertAgentNeighbor(const Agent* agent, double& rangeSq) {
  if (this != agent) {
    const double distSq = absSq(position_ - agent->position_);

    if (distSq < rangeSq) {
      if (agentNeighbors_.size() < maxNeighbors_) {
        agentNeighbors_.push_back(std::make_pair(distSq, agent));
      }

      size_t i = agentNeighbors_.size() - 1;

      while (i != 0 && distSq < agentNeighbors_[i - 1].first) {
        agentNeighbors_[i] = agentNeighbors_[i - 1];
        --i;
      }

      agentNeighbors_[i] = std::make_pair(distSq, agent);

      if (agentNeighbors_.size() == maxNeighbors_) {
        rangeSq = agentNeighbors_.back().first;
      }
    }
  }
}

void Agent::insertObstacleNeighbor(const Obstacle* obstacle, double rangeSq) {
  const Obstacle* const nextObstacle = obstacle->nextObstacle_;

  const double distSq = distSqPointLineSegment(obstacle->point_, nextObstacle->point_, position_);

  if (distSq < rangeSq) {
    obstacleNeighbors_.push_back(std::make_pair(distSq, obstacle));

    size_t i = obstacleNeighbors_.size() - 1;

    while (i != 0 && distSq < obstacleNeighbors_[i - 1].first) {
      obstacleNeighbors_[i] = obstacleNeighbors_[i - 1];
      --i;
    }

    obstacleNeighbors_[i] = std::make_pair(distSq, obstacle);
  }
}

void Agent::update() {
  velocity_ = newVelocity_;
  position_ += velocity_ * sim_->timeStep_;
}

bool linearProgram1(const std::vector<Line>& lines, size_t lineNo, double radius, const Vector2& optVelocity, bool directionOpt, Vector2& result) {
  const double dotProduct = lines[lineNo].point * lines[lineNo].direction;
  const double discriminant = sqr(dotProduct) + sqr(radius) - absSq(lines[lineNo].point);

  if (discriminant < 0.0) {
    /* Max speed circle fully invalidates line lineNo. */
    return false;
  }

  const double sqrtDiscriminant = std::sqrt(discriminant);
  double tLeft = -dotProduct - sqrtDiscriminant;
  double tRight = -dotProduct + sqrtDiscriminant;

  for (size_t i = 0; i < lineNo; ++i) {
    const double denominator = det(lines[lineNo].direction, lines[i].direction);
    const double numerator = det(lines[i].direction, lines[lineNo].point - lines[i].point);

    if (std::fabs(denominator) <= RVO_EPSILON) {
      /* Lines lineNo and i are (almost) parallel. */
      if (numerator < 0.0) {
        return false;
      } else {
        continue;
      }
    }

    const double t = numerator / denominator;

    if (denominator >= 0.0) {
      /* Line i bounds line lineNo on the right. */
      tRight = std::min(tRight, t);
    } else {
      /* Line i bounds line lineNo on the left. */
      tLeft = std::max(tLeft, t);
    }

    if (tLeft > tRight) {
      return false;
    }
  }

  if (directionOpt) {
    /* Optimize direction. */
    if (optVelocity * lines[lineNo].direction > 0.0) {
      /* Take right extreme. */
      result = lines[lineNo].point + tRight * lines[lineNo].direction;
    } else {
      /* Take left extreme. */
      result = lines[lineNo].point + tLeft * lines[lineNo].direction;
    }
  } else {
    /* Optimize closest point. */
    const double t = lines[lineNo].direction * (optVelocity - lines[lineNo].point);

    if (t < tLeft) {
      result = lines[lineNo].point + tLeft * lines[lineNo].direction;
    } else if (t > tRight) {
      result = lines[lineNo].point + tRight * lines[lineNo].direction;
    } else {
      result = lines[lineNo].point + t * lines[lineNo].direction;
    }
  }

  return true;
}

size_t linearProgram2(const std::vector<Line>& lines, double radius, const Vector2& optVelocity, bool directionOpt, Vector2& result) {
  if (directionOpt) {
    /*
     * Optimize direction. Note that the optimization velocity is of unit
     * length in this case.
     */
    result = optVelocity * radius;
  } else if (absSq(optVelocity) > sqr(radius)) {
    /* Optimize closest point and outside circle. */
    result = normalize(optVelocity) * radius;
  } else {
    /* Optimize closest point and inside circle. */
    result = optVelocity;
  }

  for (size_t i = 0; i < lines.size(); ++i) {
    if (det(lines[i].direction, lines[i].point - result) > 0.0) {
      /* Result does not satisfy constraint i. Compute new optimal result. */
      const Vector2 tempResult = result;

      if (!linearProgram1(lines, i, radius, optVelocity, directionOpt, result)) {
        result = tempResult;
        return i;
      }
    }
  }

  return lines.size();
}

void linearProgram3(const std::vector<Line>& lines, size_t numObstLines, size_t beginLine, double radius, Vector2& result) {
  double distance = 0.0;

  for (size_t i = beginLine; i < lines.size(); ++i) {
    if (det(lines[i].direction, lines[i].point - result) > distance) {
      /* Result does not satisfy constraint of line i. */
      std::vector<Line> projLines(lines.begin(), lines.begin() + static_cast<ptrdiff_t>(numObstLines));

      for (size_t j = numObstLines; j < i; ++j) {
        Line line;

        double determinant = det(lines[i].direction, lines[j].direction);

        if (std::fabs(determinant) <= RVO_EPSILON) {
          /* Line i and line j are parallel. */
          if (lines[i].direction * lines[j].direction > 0.0) {
            /* Line i and line j point in the same direction. */
            continue;
          } else {
            /* Line i and line j point in opposite direction. */
            line.point = 0.5f * (lines[i].point + lines[j].point);
          }
        } else {
          line.point = lines[i].point + (det(lines[j].direction, lines[i].point - lines[j].point) / determinant) * lines[i].direction;
        }

        line.direction = normalize(lines[j].direction - lines[i].direction);
        projLines.push_back(line);
      }

      const Vector2 tempResult = result;

      if (linearProgram2(projLines, radius, Vector2(-lines[i].direction.y(), lines[i].direction.x()), true, result) < projLines.size()) {
        /* This should in principle not happen.  The result is by definition
         * already in the feasible region of this linear program. If it fails,
         * it is due to small doubleing point error, and the current result is
         * kept.
         */
        result = tempResult;
      }

      distance = det(lines[i].direction, lines[i].point - result);
    }
  }
}
}
