from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
from Cython.Build import cythonize
import eigency
import numpy as np


class BuildRvo2Ext(_build_ext):
    """Builds RVO2 before our module."""

    def run(self):
        # Build RVO2
        import os
        import os.path
        import subprocess

        build_dir = os.path.abspath('build/RVO2')
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)
            subprocess.check_call(['cmake', '../..', '-DCMAKE_CXX_FLAGS=-fPIC'],
                                  cwd=build_dir)
        subprocess.check_call(['cmake', '--build', '.'], cwd=build_dir)

        _build_ext.run(self)
print(['build/RVO2/src']+ eigency.get_includes())
extensions = [
    Extension('rvo2', ['src/*.pyx'],
              include_dirs=['src']+ eigency.get_includes(),
              libraries=['RVO'],
              library_dirs=['build/RVO2/src'],
              extra_compile_args=['-fPIC']),
]
setup(
    name="pyrvo2",
    ext_modules=cythonize(extensions),
    cmdclass={'build_ext': BuildRvo2Ext},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Cython',
        'Topic :: Games/Entertainment :: Simulation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)