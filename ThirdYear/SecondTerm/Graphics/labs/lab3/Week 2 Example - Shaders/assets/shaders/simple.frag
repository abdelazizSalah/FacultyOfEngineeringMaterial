#version 330
//**
/*    this file is responsible for the fragment shader. 
    fragment shader is responsible for the color of the pixels.
*/


// if we are accepting some input from outside the shader we give it (in) datatype.
in vec4 vertex_color; 
out vec4 frag_color;
uniform float time; 

void main () {
    //  vec4 tint = vec4(sin(time * 10.0), sin(time * 10.0 + 1.0), sin(time * 10.0 + 2.0),1.0); 
    //  tint = 0.5 * (tint + 1.0);
    // frag_color = vec4(1.0, 0.0, 0.0,1.0);
    frag_color = vertex_color;
}