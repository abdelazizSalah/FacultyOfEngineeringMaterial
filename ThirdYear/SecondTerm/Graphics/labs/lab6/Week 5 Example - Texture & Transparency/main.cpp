#include <iostream>
#include <glad/gl.h>
#include <GLFW/glfw3.h>
#include <string>
#include <fstream>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtx/euler_angles.hpp>

struct Color
{
    uint8_t r, g, b, a;
};

struct Vertex
{
    glm::vec3 position;
    Color color;
    // da bnst5dmo 34an ne2dr enna nwz3 el texture fe amakn mo3yna
    glm::vec2 tex_coord;
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

    Vertex vertices[4] = {
        {{-0.5, -0.5, 0.0}, {255, 0, 0, 255}, {0.0, 0.0}},
        {{0.5, -0.5, 0.0}, {0, 255, 0, 255}, {1.0, 0.0}},
        {{0.5, 0.5, 0.0}, {0, 0, 255, 255}, {1.0, 1.0}},
        {{-0.5, 0.5, 0.0}, {255, 255, 0, 255}, {0.0, 1.0}},
    };

    uint16_t elements[6] = {0, 1, 2, 2, 3, 0};

    GLuint vertex_buffer;
    glGenBuffers(1, &vertex_buffer);
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer);
    glBufferData(GL_ARRAY_BUFFER, 4 * sizeof(Vertex), vertices, GL_STATIC_DRAW);

    GLuint element_buffer;
    glGenBuffers(1, &element_buffer);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, element_buffer);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 6 * sizeof(uint16_t), elements, GL_STATIC_DRAW);

    GLuint vertex_array;
    glGenVertexArrays(1, &vertex_array);
    glBindVertexArray(vertex_array);

    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer);

    GLint position_loc = 0; // glGetAttribLocation(program, "position");
    glEnableVertexAttribArray(position_loc);
    glVertexAttribPointer(position_loc, 3, GL_FLOAT, false, sizeof(Vertex), 0);

    GLint color_loc = 1; // glGetAttribLocation(program, "color");
    glEnableVertexAttribArray(color_loc);
    glVertexAttribPointer(color_loc, 4, GL_UNSIGNED_BYTE, true, sizeof(Vertex), (void *)offsetof(Vertex, color));

    // da 34an neb3t el coordinates lel vertex shader.
    GLint tex_coord_loc = 2; // glGetAttribLocation(program, "tex_coord");
    glEnableVertexAttribArray(tex_coord_loc);
    glVertexAttribPointer(tex_coord_loc, 2, GL_FLOAT, false, sizeof(Vertex), (void *)offsetof(Vertex, tex_coord));

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, element_buffer);

    glBindVertexArray(0);

    GLint mvp_loc = glGetUniformLocation(program, "MVP");

    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);

    glClearColor(0.5, 0.5, 0.0, 1.0);
    glClearDepth(1.0f);

    /// el viewport by2ooly el mfrod arsm fe msa7a ad a mn el shasha .
    ///             width  height
    // glViewport(0, 0, 650, 640);

    /// el scissor bt5leney arsm el view fe 7eta mo3yna bs mn el shasha w bmn3 ay haga tetrsm fe ay heta tnya
    // glEnable(GL_SCISSOR_TEST);
    // glScissor(0, 0, 320, 240);

    /// Defining colors
    Color B = {0, 0, 0, 255};
    Color W = {255, 255, 255, 0};
    Color Y = {255, 255, 0, 255};
    Color R = {255, 0, 0, 255};

    /// building the image using our colors
    /// fanta bt3rf el shakl el nefsk feh bl colors ely 3mltha
    /// bs el hagat de btb2a mt3rfa fl CPU
    /// ehna 3auzen nerf3ha 3la el GPU baa.
    Color image[] = {
        W, W, Y, Y, Y, Y, Y, Y, W, W,
        W, Y, Y, Y, R, R, Y, Y, Y, W,
        Y, Y, Y, R, W, W, R, Y, Y, Y,
        Y, Y, Y, Y, R, R, Y, Y, Y, Y,
        Y, Y, Y, Y, Y, Y, Y, Y, Y, Y,
        Y, R, R, Y, Y, Y, Y, R, R, Y,
        Y, B, B, Y, Y, Y, Y, B, B, Y,
        W, Y, Y, Y, Y, Y, Y, Y, Y, W,
        W, W, Y, Y, Y, Y, Y, Y, W, W};

    /// fbn3rf texture w n3mlo bind
    /// 34an nersmo fl gpu bn3rf haga zy el buffer esmha texture
    GLuint texture;
    glGenTextures(1, &texture);

    glBindTexture(GL_TEXTURE_2D, texture);
    /// el boarder lazm yeb2a b 0
    /// bt7dd el rasma el 3auzha 2D, 1D, 3D w hakaza.
    /// b3d keda btb3t shwyt arguments baa
    /*
        1- GL_TEXTURE_2D: da el no3 el 3auz tersmo
        2- level: da el m3na eno el texture da m3rfsh yb2a m3ah mipmap levels
        3- internal_format: da el format el 3auzen n5zn beh el lon 3la el GPU, fahna bnst5dm RGBA
        4- width
        5- height
        6- boarder -> must be 0
        7- format -> da el format el gy beh, el enta m3rf beh el array bta3k
        8- type -> da el type bta3 el data -> fe 7aletna de hwa unsigned
        9- data -> el sora baa el htrsmha.
    */
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, 10, 9, 0, GL_RGBA, GL_UNSIGNED_BYTE, image);

    // 34an ne2dr nersm el texture lazm n3rf el mipmap
    glGenerateMipmap(GL_TEXTURE_2D);

    // da el goz2 el b3ml beh sampling lel texture
    GLuint sampler;
    glGenSamplers(1, &sampler);

    // hena bn3mlo bl nearest.
    // mmkn n3mlo bilinear
    glSamplerParameteri(sampler, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glSamplerParameteri(sampler, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

    GLint tex_loc = glGetUniformLocation(program, "tex");

    // glEnable(GL_BLEND);
    // glBlendEquation(GL_FUNC_ADD);
    // glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    while (!glfwWindowShouldClose(window))
    {
        // this is how we can make the image dynamically grow and shrink in size :)
        int width, height;
        glfwGetFramebufferSize(window, &width, &height);

        glViewport(0, 0, width, height);

        float time = (float)glfwGetTime();
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glUseProgram(program);
        glBindVertexArray(vertex_array);

        /// hwa da el goz2 el bab3t beh el texture lel shader
        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, texture);
        glUniform1i(tex_loc, 0);
        // glUniform1i(0);

        // de el tre2a el b2dr beha eny ast5dm el sampler w a3mlo bind m3 ba2y el buffers
        glBindSampler(0, sampler);

        glm::mat4 P = glm::perspective(glm::pi<float>() * 0.5f, float(width) / height, 0.01f, 1000.0f);
        glm::mat4 V = glm::lookAt(
            glm::vec3(2.0f * cosf(time), 1.0f, 2.0f * sinf(time)),
            glm::vec3(0.0f, 0.0f, 0.0f),
            glm::vec3(0.0f, 1.0f, 0.0f));
        for (int i = 0; i < 8; i++)
        {
            float theta = glm::two_pi<float>() * (float(i) / 8);
            for (int z = 1; z <= 2; z++)
            {
                glm::mat4 M = glm::yawPitchRoll(theta, 0.0f, 0.0f) * glm::translate(glm::mat4(1.0f), glm::vec3(0.0f, 0.0f, (float)z));

                glm::mat4 MVP = P * V * M;

                glUniformMatrix4fv(mvp_loc, 1, false, &MVP[0][0]);
                glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_SHORT, 0);
            }
        }

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glDeleteBuffers(1, &vertex_buffer);
    glDeleteBuffers(1, &element_buffer);
    glDeleteVertexArrays(1, &vertex_array);
    glDeleteProgram(program);

    glfwDestroyWindow(window);
    glfwTerminate();

    return 0;
}
