#version 330

// lazm 34an teb3t el texture neb3tha lel fragment shader. 
// fa lazm ne3rfha enha uniform
// esmo sampler 34an ye2dr eno ye3ml tadarog fl alwan 
uniform sampler2D tex;

in Varyings {
    vec4 color;
    vec2 tex_coord;
} fs_in;

// in vec4 vertex_color; 

out vec4 frag_color;

void main() {
    // de bndeha el texture el hy2ra menha w bnb3tlha el coordinates
    frag_color = texture(tex, fs_in.tex_coord);
    if(frag_color.a < 0.5) discard; 

    // frag_color = texelFetch(tex, ivec2(gl_FragCoord), 0);
}
