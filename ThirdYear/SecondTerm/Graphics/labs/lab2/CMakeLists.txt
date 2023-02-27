cmake_minimum_required(VERSION 3.0.0) # this indicates the minimum version for cmake 
project(lab2 VERSION 0.1.0) # this specify the name of the project and the version


# this is how we can add subdirectories to our project
add_subdirectory (vendor/glfw)

# if the other project has somethings that you want to turn off 
# we use the set function to turn them off or on depending on what we want
set(GLFW_BUILD_DOCS OFF CACHE BOOL "" FORCE) # don't build documentations
set(GLFW_BUILD_TESTS OFF CACHE BOOL "" FORCE) # don't build Tests
set(GLFW_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE) # don't build examples
set(GLFW_INSTALL OFF CACHE BOOL "" FORCE) # don't install
set(GLFW_USE_HYBRID_HPG ON CACHE BOOL "" FORCE) # add variables to use high performance GPU
# dol 3obara 3n files ehna msh 3auzenhom ye3mlolhom compile.


# to be able to include libraries
include_directories(
    vendor/glfw/include
    vendor/glad/include
    ) # da el mkan elly bt2olo yero7 ydwr feh 3la el files el btst5dmha
add_executable(lab2 main.cpp vendor/glad/src/gl.c) # here we add the executable file with the project name. w 34an n3ml run lel exe (lab2) lazm n3ml compile le main.cpp
    
    
# kol el klam el fo2 da msh kfaya, lw ana 3auz eny akhleh yest5dm el data bta3t glfw,
# 34an ye2dr ye3ml keda lazm a2olo ye3ml link ben el project bta3na el hwa lab2 w el library el 3auzenha
target_link_libraries (lab2 glfw)