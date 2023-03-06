#include <iostream>
/**
 * @brief to be able to deal with GPU we will deal with a library called glfw
 * and create a window on cross platform
 *
 * glfw mlhash ay 3laka b openGL
 */

/**
 * 34an ne2dr net3aml m3 el driver m7tagen ne3ml include le library esmha glad
 *
 */
#include <glad/gl.h> // this must be included before glfw3.h
#include <GLFW/glfw3.h>

GLuint load_shader(const std::string &path, GLenum shader_type)
{
    std::ifstream file(path);
    std::string sourceCoder = std::string(std::istreambuf_iterator<char>(file), std::istreambuf_iterator<char>());
    const char *source = sourceCoder.c_str();

    GLuint shader = glCreateShader(shader_type);
    glShaderSource(shader, 1, &source, NULL);
    glCompileShader(shader);

    GLint status;
    glGetShaderiv(shader, GL_COMPILE_STATUS, &status);
    if (status == GL_FALSE)
    {
        GLint infoLogLength;
        glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &infoLogLength);
        GLchar *strInfoLog = new GLchar[infoLogLength + 1];
        glGetShaderInfoLog(shader, infoLogLength, NULL, strInfoLog);
        std::cerr << "Compile failure in shader: " << strInfoLog << std::endl;
        delete[] strInfoLog;
        glDeleteShader(shader);
        return 0;
    }

    return shader;
}
int main(int, char **)
{
    if (!glfwInit())
    {
        std::cerr << "Failed to initialize GLFW\n";
        return -1;
    }

    // lazm n7dd el verison el 3auzha mn openGL abl ma a3ml creation lel window bt3ty
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3); // el stren dol keda 5lony a3rf el version 3.3

    // creating a window
    GLFWwindow *window = glfwCreateWindow(640, 480, "Hello Triangle", NULL, NULL);

    if (!window)
    {
        std::cerr << "Failed to open GLFW window.\n";
        glfwTerminate();
        return -1;
    }

    //  keda openGL lama yegy ye3ml load ll functions bt3to, ht7otha 3la el new glfw window el ana lsa 3amlha ceration.
    // btb2a mohema awy lw hn3ml kza window
    glfwMakeContextCurrent(window);      // make the context of our window the main context on the current thread
    if (!gladLoadGL(glfwGetProcAddress)) // load glad
    {
        std::cerr << "Failed to load GL.\n";
        glfwTerminate();
        glfwDestroyWindow(window);
        return -2;
    }
    // this create the program to be used in the GPU
    GLuint program = glCreateProgram(); // hena bn3ml program

    // this is how we load the created shaders
    GLuint vs = load_shader("assets/shaders/simple.vert", GL_VERTEX_SHADER);
    GLuint fs = load_shader("assets/shaders/simple.frag", GL_FRAGMENT_SHADER);

    // this is how we attach the shaders to the program
    glAttachShader(program, vs);
    glAttachShader(program, fs);

    // we now after attaching them, we don't need them anymore
    glDeleteShader(vs);
    glDeleteShader(fs);

    // main loop
    while (!glfwWindowShouldClose(window))
    {
        float time = (float)glfwGetTime(); // get the time in seconds
        // hena bndelo el lon
        glClearColor(
            0.5 * sinf(time) + 0.5,
            0.5 * sinf(time + 1.0) + 0.5,
            0.5 * sinf(time + 2.0) + 0.5,
            1.0f); // set the color of the screen to black (R, G, B, A
        // clear the screen
        glClear(GL_COLOR_BUFFER_BIT); // hena bnms7o  fe3ln

        // draw something
        glUseProgram(program);
        glBindVertexArray(&vertex_array);
        glDrawArrays(GL_TRIANGLES, 0, 3);

        // swap buffers
        glfwSwapBuffers(window);

        // check for events
        glfwPollEvents(); // check events from the user.
    }

    glfwDestroyWindow(window);
    glfwTerminate();
}
