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
* 