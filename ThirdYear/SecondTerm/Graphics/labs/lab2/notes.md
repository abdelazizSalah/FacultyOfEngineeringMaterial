# Lab2 Notes 
* we have two buffers
  * 1. front buffer which the user see the data on 
  * 2. back buffer, in which we prepare the data before we send it to the front buffer.
* we use separate buffer in order to make the scenes more realistic and smooth. 
* so we draw the whole scene on the back buffer, then when we finish we jut swap the back buffer to be shown on the front buffer. 

## Graphics pipeline
* all the objects that we are going to draw, are triangles. 
* so our pipeline goes as follow
* vertex data -> vertex shader -> primitive assembly -> rasterization -> Fragment shader -> frame buffer. 

### Vertex Data 
> they are the raw points or the verticies we have, from which we want to create the triangle
>
### Vertex shader 
> hwa da el mkan elly by2dr ywsf el mkan bta3 el verticies w hal hya el mfrod tban b3eda wla oryba, wla el mfrod n5leha orybawla a w keda.
> el 7sabat de ehna el bn3mlha bs bn3mlha fe el vertex shader da y3ny.
> it generate them by applying some mathimatical equations. 
### Primitive Assembly
>  this  is responsible for collecting each 3 points together and generate a triangle from them.

### Rasterization
> el mosls da 3aml covering le shwyt khtot, el khtot de btt3rd 3la el shasha, wl shasha mtkwna mn shwyt pixels.

> fa ehna baa bnb2a 3auzen ne3rf fl rasterization, eh hwa el pixels el m3molha cover mn kol triangle. 

### Fragment Shader 
> da bya5od baa el pixels el ana 3rft en el trianngle by3mlha cover, w y2om mlwnha baa, w yshof el color properties.  
### Frame buffer
> bnro7 baa n7ot el pixels el etrsmt fl buffer, el back buffer 8alebn.

### NOTE:
we program both vertex shader and fragment shader, while the other pipe we don't have access on them 