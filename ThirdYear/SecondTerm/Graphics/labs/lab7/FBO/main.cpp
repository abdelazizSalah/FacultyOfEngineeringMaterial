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

    // bn3rf el brnagm el awl 3ntre2 function esmha glCreateProgram
    GLuint program = glCreateProgram();

    // bn3ml load lel vertex shader
    GLuint vs = load_shader("assets/shaders/simple.vert", GL_VERTEX_SHADER);
    // bn3ml load lel fragment shader
    GLuint fs = load_shader("assets/shaders/simple.frag", GL_FRAGMENT_SHADER);

    // bn3ml attach lkol shader m3 el program bta3y
    glAttachShader(program, vs);
    glAttachShader(program, fs);
    glLinkProgram(program);

    // b3d ma bn3ml el link, mbn7tgsh el vs wla el fs tany khlas, fa bnms7hom
    glDeleteShader(vs);
    glDeleteShader(fs);

    // bn3rf el verticies el hnb3thom lel vertex shader
    Vertex vertices[4] = {
        {{-0.5, -0.5, 0.0}, {255, 0, 0, 255}, {0.0, 0.0}},
        {{0.5, -0.5, 0.0}, {0, 255, 0, 255}, {1.0, 0.0}},
        {{0.5, 0.5, 0.0}, {0, 0, 255, 255}, {1.0, 1.0}},
        {{-0.5, 0.5, 0.0}, {255, 255, 0, 255}, {0.0, 1.0}},
    };

    uint16_t elements[6] = {0, 1, 2, 2, 3, 0};

    // bn3rf el vertex buffer w bn3mlo bind w b3den bn7ot feh el data
    GLuint vertex_buffer;
    glGenBuffers(1, &vertex_buffer);
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer);
    glBufferData(GL_ARRAY_BUFFER, 4 * sizeof(Vertex), vertices, GL_STATIC_DRAW);

    // bn3rf el element buffer w bn3mlo bind w bn7ot feh el data
    GLuint element_buffer;
    glGenBuffers(1, &element_buffer);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, element_buffer);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 6 * sizeof(uint16_t), elements, GL_STATIC_DRAW);

    // bn3rf el vertex array w bn3mlo bind w bn7ot feh el data
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

    // glViewport(0, 0, 320, 240);

    // glEnable(GL_SCISSOR_TEST);
    // glScissor(0, 0, 320, 240);

    Color B = {0, 0, 0, 255};
    Color W = {255, 255, 255, 0};
    Color Y = {255, 255, 0, 255};

    Color image[] = {
        W,
        W,
        Y,
        Y,
        Y,
        Y,
        W,
        W,
        W,
        Y,
        Y,
        B,
        B,
        Y,
        Y,
        W,
        Y,
        Y,
        B,
        Y,
        Y,
        B,
        Y,
        Y,
        Y,
        Y,
        Y,
        Y,
        Y,
        Y,
        Y,
        Y,
        Y,
        Y,
        B,
        Y,
        Y,
        B,
        Y,
        Y,
        Y,
        Y,
        B,
        Y,
        Y,
        B,
        Y,
        Y,
        W,
        Y,
        Y,
        Y,
        Y,
        Y,
        Y,
        W,
        W,
        W,
        Y,
        Y,
        Y,
        Y,
        W,
        W,
    };

    GLuint texture;
    glGenTextures(1, &texture);
    glBindTexture(GL_TEXTURE_2D, texture);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, 8, 8, 0, GL_RGBA, GL_UNSIGNED_BYTE, image);

    glGenerateMipmap(GL_TEXTURE_2D);

    GLuint sampler;
    glGenSamplers(1, &sampler);

    glSamplerParameteri(sampler, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glSamplerParameteri(sampler, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

    // hena bnbd2 baa enna n3rf el frame buffer 34an ne2dr nersm 3la el texture
    // fa bt3rf men el buffers el hnrsm 3leha
    GLuint framebuffer;
    glGenFramebuffers(1, &framebuffer);
    glBindFramebuffer(GL_DRAW_FRAMEBUFFER, framebuffer);

    int RTW = 256, RTH = 256;

    // bntarget el texture el hnrsm 3leh.
    // fa bn3ml frame fady 34an nersm 3leh
    GLuint render_target;
    glGenTextures(1, &render_target);
    glBindTexture(GL_TEXTURE_2D, render_target);
    GLsizei levels = (GLsizei)glm::floor(glm::log2((float)glm::max(RTW, RTH))) + 1;
    // da bnst5dmo 34an n7gz mkan leha.
    glTexStorage2D(GL_TEXTURE_2D, levels, GL_RGBA8, RTW, RTH);

    // el depth buffer faydeto eno y3rf kol object el depth bta3o ad a w ye2dr beh eno
    // ye3rf yersm men wara w men odam.
    GLuint depth_buffer;
    glGenTextures(1, &depth_buffer);
    glBindTexture(GL_TEXTURE_2D, depth_buffer);
    glTexStorage2D(GL_TEXTURE_2D, 1, GL_DEPTH_COMPONENT32, RTW, RTH);

    // de el bnrbot beha ben el render target wl framebuffer
    glFramebufferTexture2D(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, render_target, 0);
    glFramebufferTexture2D(GL_DRAW_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, depth_buffer, 0);

    GLint tex_loc = glGetUniformLocation(program, "tex");

    // glEnable(GL_BLEND);
    // glBlendEquation(GL_FUNC_ADD);
    // glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    while (!glfwWindowShouldClose(window))
    {
        int width, height;
        glfwGetFramebufferSize(window, &width, &height);

        glViewport(0, 0, width, height);

        float time = (float)glfwGetTime();

        glUseProgram(program);
        glBindVertexArray(vertex_array);

        {
            glBindFramebuffer(GL_DRAW_FRAMEBUFFER, framebuffer);
            glViewport(0, 0, RTW, RTH);

            glClearColor(0.5f, 0.2f, 0.1f, 1.0f);
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

            glActiveTexture(GL_TEXTURE0);
            glBindTexture(GL_TEXTURE_2D, texture);
            glBindSampler(0, sampler);
            glUniform1i(tex_loc, 0);

            glm::mat4 P = glm::perspective(glm::pi<float>() * 0.5f, float(RTW) / RTH, 0.01f, 1000.0f);
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
        }

        {
            glBindFramebuffer(GL_DRAW_FRAMEBUFFER, 0);
            glViewport(0, 0, width, height);

            glClearColor(0.1f, 0.2f, 0.5f, 0.0f);
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

            glActiveTexture(GL_TEXTURE0);
            glBindTexture(GL_TEXTURE_2D, render_target);
            glGenerateMipmap(GL_TEXTURE_2D);
            glBindSampler(0, sampler);
            glUniform1i(tex_loc, 0);

            glm::mat4 P = glm::perspective(glm::pi<float>() * 0.5f, float(width) / height, 0.01f, 1000.0f);
            glm::mat4 V = glm::lookAt(
                glm::vec3(2.0f, 1.0f, 2.0f),
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
