// whenever you change anything in this file, you have to recompile it.
#include <iostream>
#include <glad/gl.h>
#include <GLFW/glfw3.h>
#include <string>
#include <fstream>

struct Point
{
    float x;
    float y;
    float z;
};

struct Color
{
    // we shold define it as char to take only 1 byte to save in memory.
    uint8_t r;
    uint8_t g;
    uint8_t b;
    uint8_t a;
};

struct vertex
{
    Point pos;
    Color col;
};

GLuint load_shader(const std::string &path, GLenum shader_type)
{
    std::ifstream file(path);
    std::string sourceCode = std::string(std::istreambuf_iterator<char>(file), std::istreambuf_iterator<char>());
    const char *sourceCodeCStr = sourceCode.c_str();

    GLuint shader = glCreateShader(shader_type);
    glShaderSource(shader, 1, &sourceCodeCStr, nullptr);
    glCompileShader(shader);

    GLint status;
    glGetShaderiv(shader, GL_COMPILE_STATUS, &status);
    if (!status)
    {
        GLint length;
        glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &length);
        char *logStr = new char[length];
        glGetShaderInfoLog(shader, length, nullptr, logStr);
        std::cerr << "ERROR IN " << path << std::endl;
        std::cerr << logStr << std::endl;
        delete[] logStr;
        glDeleteShader(shader);
        return 0;
    }

    return shader;
}

int main()
{

    if (!glfwInit())
    {
        std::cerr << "Failed to initialize GLFW\n";
        exit(1);
    }

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    GLFWwindow *window = glfwCreateWindow(640, 480, "Hello Triangle", nullptr, nullptr);

    if (!window)
    {
        std::cerr << "Failed to create Window\n";
        glfwTerminate();
        exit(1);
    }

    glfwMakeContextCurrent(window);
    if (!gladLoadGL(glfwGetProcAddress))
    {
        std::cerr << "Failed to load OpenGL\n";
        glfwDestroyWindow(window);
        glfwTerminate();
        exit(1);
    }

    GLuint program = glCreateProgram();
    GLuint vs = load_shader("assets/shaders/simple.vert", GL_VERTEX_SHADER);
    GLuint fs = load_shader("assets/shaders/simple.frag", GL_FRAGMENT_SHADER);
    glAttachShader(program, vs);
    glAttachShader(program, fs);
    glLinkProgram(program);

    glDeleteShader(vs);
    glDeleteShader(fs);
    /*
        /////////////////////////////////////////
        defining the position of the vertices
        /////////////////////////////////////////
        el vectcies de btb2a mt3rfa fl ram, fa el klam da bate2, fa 34an ye7lo el 7war da 3mlo buffers
        34an teb2a oryba mn el GPU b7es enha tsr3 el denya w tkhls mn el CPU, fa tsr3 el denya .
    */
    // float vectcies[3 * 7] = {
    //     -0.5, -0.5, 0.0, 0.4, 0.2, 0.9, 1, // contain (x pos, y pos, z pos)
    //     0.5, -0.5, 0.0, 0.1, 0.5, 0.2, 1,
    //     0.5, 0.5, 0.0, 0.3, 0.3, 0.6, 1};
    vertex vertcies[3] = {
        {{-0.5, -0.5, 0.0}, {255, 0, 0, 1}}, // contain (x pos, y pos, z pos)
        {{0.5, -0.5, 0.0}, {0, 255, 0, 1}},
        {{0.0, 0.5, 0.0}, {0, 0, 255, 1}}};
    /*
        /////////////////////////////////////////
        defining buffers
        /////////////////////////////////////////
        3ndna 7aga esmha bind, de bdl ma kol mara agy a3ml call l function, lazm ab3t a2olaha ana btklm 3la men
        laa ana h3ml bind b7es a2ol wlahy ay operation ana h3mlha mn b3d el line da hayb2a 3la el buffer el folany.
    */
    GLuint vertex_buffer;
    glGenBuffers(1, &vertex_buffer); // creating a buffer
    // binding the name
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer);

    // the binded data, the size of the data, the data, the usage of the data
    /// GL_STATIC_DRAW: the data will not change at all or very rarely.
    glBufferData(GL_ARRAY_BUFFER, 3 * sizeof(vertex), vertcies, GL_STATIC_DRAW); // da el data el ana 3auz ab3tha w b2olo hast5dmha ezay.

    GLuint vertex_array;
    /// bb3tlo el 3dd el 3auz a3mlo create (hena h3ml 1 bs) , w el mkan el y7ot feh el data (vertex array address)
    glGenVertexArrays(1, &vertex_array);

    glBindVertexArray(vertex_array); // binding the name

    // sending the vectcies to the vertex shader
    // 1- the index of the attribute in the vertex shader
    // 2- the number of components in the attribute
    // 3- the type of the components
    // 4- whether the data should be normalized -> it divides all the values by the maximum value of the type
    // 5- the stride (the space between consecutive attributes) -> += 3 akno fl for loop kol khatwa hayt7rk 3
    // 6- the offset of the first component -> void pointer
    // GLuint pos_loc = glGetAttribLocation(program, "position");
    GLuint pos_loc = 0;
    glEnableVertexAttribArray(pos_loc); // enable the attribute
    glVertexAttribPointer(pos_loc, 3, GL_FLOAT, true, sizeof(vertex), 0);

    // GLuint clrs = glGetAttribLocation(program, "colors");
    GLuint clrs = 1;                 // l2n ana msbto already mn gowa m3rf en dayman da hykon el address location bta3 el color
    glEnableVertexAttribArray(clrs); // enable the attribute
    glVertexAttribPointer(clrs, 4, GL_UNSIGNED_BYTE, true, sizeof(vertex), (void *)offsetof(vertex, col));
    ///////////////////////////
    // GLuint time_loc = glGetUniformLocation(program, "time");
    // std::cout << "time_loc: " << time_loc << std::endl;

    while (!glfwWindowShouldClose(window))
    {
        // float time = (float)glfwGetTime();
        glClearColor( // this is how we set the background color
                      // 0.5 * sinf(time) + 0.5,
                      // 0.5 * sinf(time + 2.0) + 0.1,
                      // 0.5 * sinf(time + 1.0) + 0.9 // this to make it change with time,
                      // ,
                      // 1.0
            0.3, 0.3, 0.3, 1.0);
        glClear(GL_COLOR_BUFFER_BIT);

        glUseProgram(program);
        glBindVertexArray(vertex_array);

        // draw triangle
        glDrawArrays(GL_TRIANGLES, 0, 3); //
        // glUniform1f(time_loc, time);
        // glDrawArrays(GL_TRIANGLES, 0, 3);
        // glUniform1f(time_loc, time + 0.5);
        // glDrawArrays(GL_TRIANGLES, 0, 3);
        // glUniform1f(time_loc, time + 1.0);
        // glDrawArrays(GL_TRIANGLES, 0, 3);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glDeleteProgram(program);

    glfwDestroyWindow(window);
    glfwTerminate();

    return 0;
}
