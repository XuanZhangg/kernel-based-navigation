# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

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
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/yxhan/yxh/kernel-based-navigation-new-rvo

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/yxhan/yxh/kernel-based-navigation-new-rvo

# Include any dependencies generated for this target.
include CMakeFiles/mainDebug.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/mainDebug.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/mainDebug.dir/flags.make

CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o: CMakeFiles/mainDebug.dir/flags.make
CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o: Main/mainDebug.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/yxhan/yxh/kernel-based-navigation-new-rvo/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o -c /home/yxhan/yxh/kernel-based-navigation-new-rvo/Main/mainDebug.cpp

CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/yxhan/yxh/kernel-based-navigation-new-rvo/Main/mainDebug.cpp > CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.i

CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/yxhan/yxh/kernel-based-navigation-new-rvo/Main/mainDebug.cpp -o CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.s

CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o.requires:

.PHONY : CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o.requires

CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o.provides: CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o.requires
	$(MAKE) -f CMakeFiles/mainDebug.dir/build.make CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o.provides.build
.PHONY : CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o.provides

CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o.provides.build: CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o


# Object files for target mainDebug
mainDebug_OBJECTS = \
"CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o"

# External object files for target mainDebug
mainDebug_EXTERNAL_OBJECTS =

mainDebug: CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o
mainDebug: CMakeFiles/mainDebug.dir/build.make
mainDebug: libRVO.a
mainDebug: /usr/lib/x86_64-linux-gnu/libcholmod.so
mainDebug: /usr/lib/x86_64-linux-gnu/libamd.so
mainDebug: /usr/lib/x86_64-linux-gnu/libcolamd.so
mainDebug: /usr/lib/x86_64-linux-gnu/libcamd.so
mainDebug: /usr/lib/x86_64-linux-gnu/libccolamd.so
mainDebug: /usr/local/lib/libTinyVisualizer.so
mainDebug: /usr/lib/x86_64-linux-gnu/libmpfr.so
mainDebug: /usr/lib/x86_64-linux-gnu/libgmp.so
mainDebug: /usr/lib/x86_64-linux-gnu/libnuma.so
mainDebug: CMakeFiles/mainDebug.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/yxhan/yxh/kernel-based-navigation-new-rvo/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable mainDebug"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mainDebug.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/mainDebug.dir/build: mainDebug

.PHONY : CMakeFiles/mainDebug.dir/build

CMakeFiles/mainDebug.dir/requires: CMakeFiles/mainDebug.dir/Main/mainDebug.cpp.o.requires

.PHONY : CMakeFiles/mainDebug.dir/requires

CMakeFiles/mainDebug.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/mainDebug.dir/cmake_clean.cmake
.PHONY : CMakeFiles/mainDebug.dir/clean

CMakeFiles/mainDebug.dir/depend:
	cd /home/yxhan/yxh/kernel-based-navigation-new-rvo && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/yxhan/yxh/kernel-based-navigation-new-rvo /home/yxhan/yxh/kernel-based-navigation-new-rvo /home/yxhan/yxh/kernel-based-navigation-new-rvo /home/yxhan/yxh/kernel-based-navigation-new-rvo /home/yxhan/yxh/kernel-based-navigation-new-rvo/CMakeFiles/mainDebug.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/mainDebug.dir/depend

