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

        // swap buffers
        glfwSwapBuffers(window);

        // check for events
        glfwPollEvents(); // check events from the user.
    }

    glfwDestroyWindow(window);
    glfwTerminate();
}
