# Lab 3 Notes 
* in -> 7aga gya mn bara.
* out -> 7aga ana el hakhrga. 
* ehna bnst5dm openGL.
* el hagat de kolaha bttnfz 3la el GPU. 
* void* da m3nah pointer w khlas, msh m7dd data type leh, bst5mha 34an a3ml cast, lw fe functions mo3yna btstna void ptr, fa b3ml void pointer
* enta bt7dd el alwan 3nd el verticies bs. 

* lakn 34an tegeb el keyam el fl nos bta3t el mosls, bn3ml linear interpolation. 

* uniform variable:
  * bnb3t input kharegy mn el cPP le ay shader. 
* bnndh 3leh mn el .cpp file.
* 34an ne2dr neb3tha bnro7 ngeb el location bta3o fl cpp code 
  * glUniform1f (time_loc, time) -> 1f da m3nah enk hatb3t one variable. 
* time da lazm ykon nfs el esm el fl frag shader, 
* lw enta ktbt esm mokhtalef, hwa msh hayedek error, lakn hwa hayt3aml akno msh shayef el mkan da w haytgahel ay haga begy 3leh.
* mmkn b shader wahed tersm 10000 object 3ady
* w mmkn object wahed bs w shader wahed bs, te3ml ashkal complex gedan. 
* variang, bytn2l mn el vertex shader lel fragment shader. 
* openGL, mkanosh m3rfen type monfasel le kol haga
* fkan byt3aml 3al en kol haga int
* w byrg3lk haga esmha name, 34an yeb2a id. 
* kol haga hant3aml m3aha hatb2a GLuint
* el GPU mabye2rash el RAM. 
* fa 34an ne2dr n5zn el vertcies fl GPU, bn3l haga esmha vertex_buffer 
  * glGenBuffers()
  * glBindBuffer(GL_ARRAY_BUFFER,name) -> da 34an n7dd esm 7aga mo3yna b7es enna lama negy n3ml apply l ay haga yeb2a 3aref enna asdna eno 3ayzo ye3ml el haga de 3la el 7aga el mo3yna el 7adedt esmha mn el awl, w byfdl keda l7d ma ye3ml bind lhaga gdeda.
  * fa keda 3mlna bind lel GL_ARRAY_BUFFER m3 el name

* 34an neb3t data baa bnst5dm 
  * GLBufferData(GL_ARRAY_BUFFER, sizeOfTheData, &TheDataItself, optionOfDrawing)
  * options
    * 1. GL_STATIC_DRAW
    * 2. GL_DYNAMIC_DRAW
    * 3. GL_STREAM_DRAW

*  stride: 3dd el steps el htt7rkha fl mra, zy aknk fe for loop w bdl ++ t2ol += 4 msln, fa kda el stride = 4.
*  ehna el hadaf enna msh 3auzen ne3ml hard coding fl shaders, ehna bnb2a 3auzen enna neb3tlo el hagat mn el cpp file.
*  badal ma yeb2a 3ndna kaza buffer bnkhly en 3ndna buffer wahed
* we da leh mezten
  * 1. eno by5ly el data oryba mn b3d, fa lama yegy ygbhom w y7otohom fl cache byb2a asr3
  * 2. enk msh bt7tag t keep synchronizng the positions and colors which was in two  seperate buffers every time manually.
* lw mehtag a3ml data structure bnfsy bnst5dm el struct.
  * struct position (float x,y,z);
  * struct color (uint8_t r,g,b,a)
  * struct Vertex (position pos; color clr;)

------------
> GLuint -> this is a common datatype for alot of variables in openGL, fa lama btegy te3ml brnamg geded by2om mrg3lk 7aga zy id keda w t5znha w lama tegy tt3aml 3la ayy haga tt3aml enta 3la el id el tl3 da. fa ehna kol el hnt3aml m3ah lhd akher el term haykon GLuint 
# Things To be done in this lab.
1. we want to set a communication between the shaders, so let the vertex shader send the color to the fragment shader. 
2. how to draw multiple shapes(triangles).
  ## Sending color from the vertex shader notes: 
* if you are sending something **out** from the shader we must define it as out data type:
  * out vec4 vertex_color; 
* and when assigning it we give it certain id. 
* and when we going to recive it in the other shader we define it as **in** 
  * in vec4 vertex_color
* this process is called **varing process**

## Sending information from the cpp file to the vertex shader. 
* to be able to do this we have to use a **unifrom** variables.
* they are varibales which has certain locations
* to call them in cpp we use **glGetUniformLocation(program, yourVariableName)**
* this gets its location, them after that we apply some function on it. 
* To be able to send certain value to it we use 
  * glUniform1f(location, value to be sent) -> this means that we are dealing with 1 uniform variable with datatype float 
  * then we send to it the return from glGetUniformLocation
  * then we send to it the value we want to place in this location.
## Attribute data 
* 

## By these knowleadge, now we can draw things rather than the triangle:
* we can draw rectangle by sending only 4 points, and tell the vertex shader to combine each 3 points together
* star by drawing two opposite triangles.


## important note: 
1. any attribute that we are going to define should have data type GLuint
2. glGenBuffer -> appreviaton for gl generate buffer, it has two attributes 
   1. number of buffers to be generated 
   2. refrence pointer to the buffers locations.
3. after generating any buffer we need to bind it, to do so we use **glBindBuffer** it also has two attributes 
   1. the new name -> GL_ARRAY_BUFFER
   2. the generated buffer (GLuint object which you send to the glGenBuffer)
4. glBufferData() is the function used to send the data, it has 4 attributes 
   1. name of the bind array (GL_ARRAY_BUFFER)
   2. size (in bytes) of the sent data
   3. the data to be sent
   4. whether the data is going to change alot or not, if not we use GL_STATIC_DRAW
5. glEnableVertexAttribArray() this is the function used to enable certain attribute defined as **in** in any of the shaders , it has single attribute
   1. the index defined in the shader, to get this index we have 2 ways 
      1. to define it by ourselfs by going to the shader and writing before it (layout (location  = x )) and set x to the value we want
      2. to get the automatic location by calling this function.
   > **glGetAttribLocation** (program, 'attributeExactName').
6. glVertexAttribPointer() this is used to send the data to this attribute, and it has 4 attributes 
   1. the idx return from glGetAttLocation or the predefined one.
   2. number of elements to be sent
   3. data type of these elements
   4. whethere the data should be normalized or not.
   5. the stride (space between consecutive atteributes)
   6. the offset of the first element.
7. glDrawElements() this is the function used for drawing, it has 4 attributes 
   1. the type of the element to be drawn (point, line or triangle)
   2. number of points to be drawn
   3. data type
   4. index of the start