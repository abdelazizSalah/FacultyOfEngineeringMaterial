# Lab1 Notes
* hadaf el graphics enk tfhm el user shwyt data mwgoda fl computer, te3rdhalo bshkl UI kwys yefhmo
* wenk te2dr te3rd pixels w sowar wara b3d bshkl gamed w waake3y. 
* ehna bnshtghl 3la haga esmha rasterization. 
* ehna bnt3lm ezay ne2dr n3ml game engines, ehna bngeb el mwdo3 mn t7t khalees, basics el basics
* enta mmkn teb2a graphics engineer , w da msh zyo zy el game developer, 
* el graphics engineer mmkn yshtghl feno ye3ml 
  * game engine
  * rendering softwares
  * medical apps
  * industrial apps
  * etc...

## GPU
* graphics processing unit
* why gpus?
  * 34an t5ly mwdo3 rsm el hagat 3la el shasha mlhash 3laka b tasks el processor el 3ady, fa 34an ye2dr eno ysr3 el denya.
  * w mehtag hagat t3ml run in parallel. 
  * byhtm eno yeshtghl 3la haga single instruction multiple data (SIMD)
* **The main difference between CPU and GPU is that GPU always execute things in parallel so when drawing things on the screen it has a huge impact on the performance**

### How to deal with the GPUS:
* el fekra en el GPUs byt3mlo mn kaza sherka
* w kol sherka bt3ml el hardware implementation el 3la mzagha
* fana wna bktb code, msh h3od a3ml code mkhssos lkol gpu 3la hasab sherkto, laa ehna 3auzen nktb haga tshtghl 3nd el kol
* fa 34an ne2dr ne3ml keda bnhtag nest5dm driver
* el driver wazefto eno ya5od el code mn API mo3un el API da yeb3t el instructions el 3auzen nnfzha, y2om el driver yefhm ehna 3auzen ne3ml a w y2om mtrgm el klam da ll GPU 3la hasab el hardware bta3o. 
* el driver el by3mlo bykon el manufacturer nfso, wl mfrod enohom ykono optimized gedan w el nas el t3mlo ykono experienced. 

### Examples on APIS
* openGL (1992) -> single Threaded. 
* Microsoft DirectX (1995)
* openGL|Es (2003) // to apply it on mobile
* WebGL (2011) // to apply it on web
* Vulkan (2016)
* DirectX 12
* Metal -> apple.
* Web GPU -> google.

## OpenGL
* it is a C api
* easy to be learned. 
* cross-platform
* up-to-date with modern GPUs
* we will use Version 3.3
* 3.3 is the modern version. 

## CMake
* da cross-platform free and open-source software tool for managing the build process of software using compiler-independent
* hwa bywsf 3laket el files el fnfs el project m3 b3d w eh kol file, we men el mfrod yet3mlo compile emta w men my3mlosh w keda
* bnwsf el klam da fe file esmo CMakeList.txt

## Shaders
* they are simple programs that descripe the traits of either a vertex or a pixel
* bernamg baset bywsf 5sa2s w mwasafat el pixels wl vertcies.

### Vertex Shader
* describe the attributes (position, texture, coordinates, color, etc) of each vertex
* de el btwsf el amakn bna3t el vertcies bto3 el mosls w 5sa2sha

### Fragment Shader
* describe the traits (color, z-depth, alpha value) of the pixel.
* bnwsf alwan kol pixel baa w ad eh hya shafafa w gham2a aw fat7a, w hakaza.

