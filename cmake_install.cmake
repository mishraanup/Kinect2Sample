# Install script for directory: C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Program Files/Sample")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/Color/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/Depth/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/Infrared/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/BodyIndex/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/Body/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/JointSmooth/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/MultiSource/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/CoordinateMapper/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/Face/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/HDFace/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/Fusion/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/Gesture/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/Speech/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/AudioBeam/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/AudioBody/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/ChromaKey/cmake_install.cmake")
  include("C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/FaceClip/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "C:/Users/Shradha Shalini/Documents/Kinect2Sample-master/sample/build2/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
