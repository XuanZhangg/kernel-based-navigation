# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/new-rvo2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/new-rvo2

# Include any dependencies generated for this target.
include CMakeFiles/mainSimulator.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/mainSimulator.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/mainSimulator.dir/flags.make

CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.o: CMakeFiles/mainSimulator.dir/flags.make
CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.o: Main/mainSimulator.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/new-rvo2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.o -c /home/new-rvo2/Main/mainSimulator.cpp

CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/new-rvo2/Main/mainSimulator.cpp > CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.i

CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/new-rvo2/Main/mainSimulator.cpp -o CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.s

# Object files for target mainSimulator
mainSimulator_OBJECTS = \
"CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.o"

# External object files for target mainSimulator
mainSimulator_EXTERNAL_OBJECTS =

mainSimulator: CMakeFiles/mainSimulator.dir/Main/mainSimulator.cpp.o
mainSimulator: CMakeFiles/mainSimulator.dir/build.make
mainSimulator: libRVO.a
mainSimulator: /usr/lib64/libcholmod.so
mainSimulator: /usr/lib64/libamd.so
mainSimulator: /usr/lib64/libcolamd.so
mainSimulator: /usr/lib64/libcamd.so
mainSimulator: /usr/lib64/libccolamd.so
mainSimulator: /usr/local/lib/libTinyVisualizer.so
mainSimulator: /usr/lib64/libmpfr.so
mainSimulator: /usr/lib64/libgmp.so
mainSimulator: /usr/lib64/libnuma.so
mainSimulator: CMakeFiles/mainSimulator.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/new-rvo2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable mainSimulator"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mainSimulator.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/mainSimulator.dir/build: mainSimulator

.PHONY : CMakeFiles/mainSimulator.dir/build

CMakeFiles/mainSimulator.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/mainSimulator.dir/cmake_clean.cmake
.PHONY : CMakeFiles/mainSimulator.dir/clean

CMakeFiles/mainSimulator.dir/depend:
	cd /home/new-rvo2 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/new-rvo2 /home/new-rvo2 /home/new-rvo2 /home/new-rvo2 /home/new-rvo2/CMakeFiles/mainSimulator.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/mainSimulator.dir/depend

