#version 330

// 3auzen n3rf eno ye2ra el position mn bara
// 7war el layout da m3nah enk 3auz tsbt el position mn bara
layout (location  = 0 )in vec3 position; // this is the position of the vertex in the triangle
layout (location  = 1 )in vec4 colors; // this is the color of the vertex in the triangle

// setting the variable to be sent out. 
out vec4 vertex_color; 


// this variable is used to act on time
// uniform means a variables which gets its value from the cpp file.
uniform float time;
void main() {

    // const vec3 position[3] = vec3[3] (
    //     vec3(-0.5, -0.5, 0.0), // contain (x pos, y pos, z pos)
    //     vec3( 0.5, -0.5, 0.0),
    //     vec3( 0.5,  0.5, 0.0)
    // );
   
    // we send only 3 colors, which indicates the corners colors,
    // then the gl itself apply an interpolation to be able to get 
    // the colors of the remaining pixels in the triangle.
    // const vec4 colors[3] = vec4[3] (
    //     vec4(1.0, 0.0, 0.0,1.0),
    //     vec4(0.0, 1.0, 0.0,1.0),
    //     vec4(0.0, 0.0, 1.,1.0) // mayten el komma, lw 7tet hena comma hayfr23 fwshk
    // );

    // to be able to make it move in a circle we add time to both x and y
    // gl_Position = vec4(position[gl_VertexID] + vec3(sin(time), cos(time), 0.0), 1.0);
    gl_Position = vec4(position , 1.0);
    // vertex_color = colors[gl_VertexID]; // gl_vertexID is a variable that is automatically set by opengl. it is the index of the vertex in the array.
    vertex_color = colors; // gl_vertexID is a variable that is automatically set by opengl. it is the index of the vertex in the array.
}
