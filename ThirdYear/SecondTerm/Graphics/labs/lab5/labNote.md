# Project notes
1. All assets are in the `assets` folder
   1. assets such as shaders, textures, models, etc.
2. all the libraries are stored in the `vendor` folder
3. when the code gets large, we will put it in `src` folder
4. to be able to create a cross-platform application, we will use `GLFW` -> Graphics Library Framework
5. and `OpenGL` -> Open Graphics Library to load OpenGL functions. 
6. we will use `GLM` -> OpenGL Mathematics to do the math for us.
   1. it is a header-only library, so we just need to include the header files.
7. ImGui is a library that allows us to create a GUI for our application.
   1. it is also a header-only library, so we just need to include the header files.
8. `stb` is a library that allows us to load images.
   1. it is also a header-only library, so we just need to include the header files.
   2. bnft7 sowar w nb3t el data bt3tu 3la el GPU
9. Tinyobjloader is a library that allows us to load 3D models.
   1. it is also a header-only library, so we just need to include the header files.
10. If we want to add more libraries, we can add them to the `vendor` folder.
    1.  First and foremost, check if the author wrote how to include the library into your project.
    2.  Header-only libraries are easy to include, just include the header files, but have negative effects on the compilation time.
    3.  Libraries that has a `CmakeLists.txt` file can usually be included by using `add_subdirectory` but need to search for the library's name for linking, can be found in `CMakeLists.txt` file.
    4.  if it was neither of the above, then we need to add the library's source files to our project manually. 
11. Project phases:
    1.  Initialization phase
        1.  Initialize GLFW
        2.  Initialize OpenGL
        3.  Initialize ImGui
        4.  Initialize our application
    2. Game loop phase:
        1.  Poll events
        2.  Update
        3.  Render
    3. Clean up phase:
        1.  Clean up ImGui
        2.  Clean up our application
        3.  Clean up GLFW
        4.  Clean up OpenGL
 12. CORE_PROFILE -> m3nah msh 3auzen nshtghl 3la el deprecated functions
----------
### Aliasing 
1. de bt7sl natega le eny msh ader agm3 kol el details bta3t el sora, fa el by7sl hwa eny batl3 sora moshawaha shwaya, natega le eny msh bakhud kol el details
2. fa el lines msln bttl3 mtksra shwya, aw el points bttl3 mtksra shwya
3. fa ehna 34an ne7l el mushkela de bn3ml tadarog fl alwan bta3t el pixels, b7es el pixel wl 7waleeha shades keda, t5ly el mwdo3 more smooth lel 3en fa t3rf enha tshof el mwdo3 kwys.
---------
### Solutions of Aliasing 
1. enk tzwd 3dd el pixels, fa keda bt7sn el resolution. -> superSamplning AntiAliasing **(SSAA)**
   1. el mushkela en el screen bt3ty mmkn mykonsh feha kol el pixels de, fa 34an n7l el mwdo3 da bna5ud kol 4 msln w n7sb el average bta3ha w n7oto gowa el pixel. 
   2. fa keda hytl3lk shades. 
   3. bs mushkelto eno bya5ud w2t atwal w space akbur. 
   4. el no3 da a7sn no3 ka 7al mshakel l2no by7l kol 7aga
   5. lakn hwa bate2 w mokalef
2. 2 Samples per pixel **(2xMSAA)**
   1. de el by7sl en kol pixel by2smha nosen 
   2. w kol nos byshof hwa mt8aty wla laa, lw ah 
      1. lw ah fa by7sblo el shader w y7oto fo2
      2. lw laa fa khalas msh hy7ot 3leh haga
   3. lw el no2tten mt8tyen, by7sbo mra wahda w y7oto fo2hom homa el etnen
   4. lw wla wahda mt8tya msh by7sbo khales.
   5. hwa keda b2a asr3 bs lesa byakhud memory aktur. 
3. 4 samples per pixel **(4xMSAA)**
   1. zyha zy el 2xMSAA bs by5lehom 4
   2. w 3ndna 5 cases:
      1. 0 samples covered -> msh hy7ot 3leh haga,
         1. 0% colored
      2. 1 sample covered
         1. 25% colored
      3. 2 samples covered
         1. 50% colored
      4. 3 samples covered
         1. 75% colored
      5. 4 samples covered
         1. 100% colored
   3. hena bn3ml run ll fragment shader mara wahda bs, w b3den bnshof men el points el h7ot 3leha. 
4. el fragment shader mn aktur el hagat el bta5ud calculations w t2el. 
-------
## MSAA 
### pors 
1. Fast and hardware supproted
2. Good result without blurring the whole scene. 
### cons
1. Extra memory
2. Only works on edge
3. Incompatible with Deferred Rendering which is popular in modern games.
------------
### Other Popular techniques
1. fast approximate anti-aliasing **(FXAA)**
   1. da sare3 gedan w byst5dmoh kman 3la el mobilat.
2. Subpixel Morphological Anti-Aliasing **(SMAA)**
   1. depend on image processing 
3. Temporal Anti-Aliasing **(TAA)**
   1. depend on shaking the image.
4. Deep Learning based Anti-Aliasing **(DLAA)**
   1. deeplearning hwa el ms2ol baa yet3aml m3aha. 
------------
## Buffers types 
1. Back buffer
   1. el buffer el 3ndna 3la el screen, da el ehna bnrsm 3leh fl backend, w el user msh byshofo
   2. bnst5dmuh 34an el user mayo3odsh yeshof el tghorat el malhash lazma bl nesbalo w l scene blnsbalo yeb2a smooth. 
2. Front Buffer 
   1. da el buffer el eluser fe3ln byb2a shayfo, w da el fayda mno eno y7ss el user en el denya smooth awy. 
   2. used to avoid flicking.
-------------
### Bits -> important for Color Buffer
1. 1 bit -> 2 values
2. kol ma el bits zadet kol ma edrt ageb shades a7sn.
3. 8 bits are usually enough.
4. kol bit bn3mlha representation b 8 bits. 
-------------
### Refresh rate
1. 60hz -> 60 frames per second
2. ye3ml refresh kol ad a, l 3mltha dont care hy3ml b asr3 taka 3ndo. 
----------
### Depth buffer 
1. muhem 34an y2ol men b3ed w y3ml el 3d effect.
----------
### Stencil Buffer
1. da by2ol en el object el folany haytrsm lama ykon el stencil kemto x w hakaza. kol ma aghyr kemt el stencil, b2dr a3rd objects tanya. 
2. hwa fekrto eny hashof el object mn anhy etgah.
3. mmkn lw 3ndk box, w 3auz tersm 3la one side --> sphere w on the other side triangle msln.
4. fa bnro7 3la el side el 3auzen feh el sphere n2om 7aten stencil = 1
5. w 3la el side el 3auzen feh el triangle n2om 7aten stencil = 2
6. w n2ol ll sphere etrsm fl amakn el feha 1 bs
7. w el triangle fl amakn el feha 2 bs. 
----------
### GPU VRAM
> GPU VRAM is not reachable as the RAM, it is a special memory that is only accessible by the GPU.

> Lama bntlob mn openGL te3ml object, ayan kan hwa eh, hya btrg3lna unsigned int by3br 3n el resource el et3ml da. 

> similar to object ID. 
-----------
### Pipeline
1. Vertex Data -> mgmo3t el pixels el 3auz arsmha
2. Vertex Shader -> el mas2ol 3n el t3amol m3 el vertcies. 
3. Primitive assembly -> bygm3 kol 3 verticies m3 b3d.
4. Rasterization -> by3ml el 3d effect.
5. Fragment Shader -> mas2ol 3n alwan el pixels el 3auz arsmha.
6. Frame buffer -> el buffer el 3ndna 3la el screen. 
> we can only write vertex shader or fragment shader.
----------

