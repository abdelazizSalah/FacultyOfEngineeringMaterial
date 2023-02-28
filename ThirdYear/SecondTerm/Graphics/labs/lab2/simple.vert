#version 330 // this line must always be the first line, nothing can be before it, even comments, it specifies the version of OpenGL we are using.s

// this file contains the vertex shader implementation. 
void main () {

    vec3 positions [3] = vec3 [3] ( // we  use 3d even that our screen is only 2d, but we use the 3rd diminsion to determine the depth of the vertex.
        vec3 ( -0.5 , -0.5 , 0.0 ), 
        vec3 ( 0.5 , -0.5 , 0.0 ), 
        vec3 ( 0.0 , 0.5 , 0.0 )
    ); 

    gl_Position = vec4 ( positions [ gl_VertexID ], 1.0 ); // here we use 4d because we need 
}