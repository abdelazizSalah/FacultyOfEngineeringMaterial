#include <iostream>
#include <glad/gl.h>
#include <GLFW/glfw3.h>
#include <string>
#include <fstream>
// this library is used to do math for us.
#include <glm/glm.hpp>
/// this is included to do the matrix transformations and multiplication operations.
#include <glm/gtc/matrix_transform.hpp>

struct Color
{
    uint8_t r, g, b, a;
};

struct Vertex
{
    /// we used the glm vec3 instead of the normal vec3
    glm::vec3 position;
    Color color;
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
        {{-0.5, -0.5, 0.0}, {255, 0, 0, 255}},
        {{0.5, -0.5, 0.0}, {0, 255, 0, 255}},
        {{0.5, 0.5, 0.0}, {0, 0, 255, 255}},
        {{-0.5, 0.5, 0.0}, {255, 255, 0, 255}},
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

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, element_buffer);

    glBindVertexArray(0);

    GLint mvp_loc = glGetUniformLocation(program, "MVP");

    /// de el ms2ola enha t4a8al 5aseyet el depth.
    /// b7es en el oryb hwa elly y3ml overwrite 3la el pixel el b3eda msh el 3ks
    glEnable(GL_DEPTH_TEST);
    /// de b2ol eny 3auz elly el depth bta3o a2al hwa elly yetrsm
    glDepthFunc(GL_LESS);

    /// dol el b7dd behom el alwan wl depth
    // this for background
    glClearColor(0.0, 0.0, 0.0, 1.0);
    // this for the depth
    glClearDepth(1.0f);

    while (!glfwWindowShouldClose(window))
    {
        float time = (float)glfwGetTime();
        /// lazm ne3ml clear llel depth buffer fl awl.
        /// lw m3mlthash, htla2y en el pixels, lw 3adet lawent goz2 mo3yn mn el shasha
        /// khlas mafesh haga hatshel el lon da. -> lazm de3ml comment lel glEnable wl depth function kman
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glUseProgram(program);
        glBindVertexArray(vertex_array);

        /// we used the glm perspective function instead of the normal perspective function.
        /// prespective -> el 7agat el b3eda btb2a asghar, w el hagat el oryba btb2a akbur, zyha zy nazar el bashar
        /// fe no3 tany esmo el orthogonal w da feh kol haga btb2a parallel lb3d, w by7afz 3la el sizing.
        // perspective parameters:
        /// 1. field of view (in radians) -> zawyet el ro2ya bt3ty.
        /// 2. aspect ratio -> el width m2som 3la el height.
        /// 3.near -> a2rab haga m2drsh ashof a2rb mnha.
        /// 4.far -> ab3d haga a2dr ashofha.
        glm::mat4 PrespectiveView = glm::perspective(glm::pi<float>() * 0.5f, 640.0f / 480.0f, 0.01f, 1000.0f); // da by7ddly sefat el camera

        /// lookAt parameters:
        /// 1. eye -> el camera mawgoda fen?
        /// 2. center -> el camera btbos 3la fen?
        /// 3. up -> el zawya elly el camera btbos beha
        glm::mat4 View = glm::lookAt(
            glm::vec3(2.0f * cosf(time), 1.0f, 2.0f * sinf(time)), // keda el camera hatlf fe shakl circle
            glm::vec3(0.0f, 0.0f, 0.0f),                           // hasabet el mkan el babos 3leh
            glm::vec3(0.0f, 1.0f, 0.0f));                          // hasabet el zawya elly el camera btbos beha
        /// up (x y z)
        /// draw 5 cubes in a row -> 3n tre2 eny a7ot el Draw element gowa loop
        /// 34an arsm kaza mara, w kol mara b3ml transation 3la el x y z
        /// fa aghyr el mkan el 3auz arsm feh.
        for (int i = -10; i <= 10; i++)
        {
            /// M -> el location bta3 el elements.
            glm::mat4 ModelLocation = glm::translate(glm::mat4(1.0f), glm::vec3(0.0, 0.0, (float)i));

            /// MVP = Model View Projection
            glm::mat4 MVP = PrespectiveView * View * ModelLocation;

            /// hena bnb3t uniform no3o matrix 7agmo 4x4 w v (vector) da m3naha eny mmkn ab3t kaza element fe nfs el w2t.
            ///  mvp_loc-> fa bb3tlo mkan el uniform bta3y
            ///  1 -> 3ddhom
            ///  false -> m4 3auz a3ml transpose.
            ///  &MVP[0][0] -> el address bta3 awl point
            glUniformMatrix4fv(mvp_loc, 1, false, &MVP[0][0]);

            /// hya de el function elly btrsm
            glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_SHORT, 0);
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
