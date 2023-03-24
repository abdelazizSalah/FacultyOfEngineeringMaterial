# Lab5 notes.
* In the previous lab, we have been (etkarwetna)
* This is because, there were a lot of librabries that we have to installed, and used which we don't understand how they work and what they are doing. 
* we have a lot of functions to be applied
* 1. Scaling: 
      * Lw 3auzen nkbr el object, fa bndrb kol el vertices 3la el scale factor
* 2. Rotation:
      * Bndrb fe sin w cos, da bydef zawya lel points, fa by5leha tlf.
* 3. Translation:
      * el mushkela hena enna lw shaghalen fel 3x3, msh hn3rf ne3ml matrix tegm3lna el scalar 3la el x, y, z.
      * fa 34an keda olna 5las ehna hanshtghl 4x4. 
      * w hyb2a 3ndna component esmo homogenous component `w`
      * fa lw 3auzen negm3 7aga han7otha fe akher column, fe awl 3 rows. 
      * w lw 3auzen nedrb fe scale han7otha 3la el main diagonal, bta3 awl 3 rows.
      * wlw 3auz t3ml rotation?
      * bzbt hayb2a bfe el amakn el fadla fl matrix, fe awl 3 rows. 
      * fa el hadaf mn enna 3mlnaha 4x4, enna 5lena best5dam matrix wahda bs, a2dr a3ml kol el operations m3 b3d. 
      * el `w` bt3bry 3n no3 el haga el shghal beha, lw 5letha 1 da m3nah en da point w leho location mo3yn w a2dr a7rko. 
      * lakn lw 5letha 0 -> da m3naha en el haga el m3aya de vector malhash location, w msh h3ml 3leh  translation.  
-----------
### Relation between vectors and points. 
* Vector:
  > it is a magnitude and direction with no location in the space. 
* Point:
  > location in the space. 
* Vector + Vector = Vector (etgah b direction m3 etgah b dircetion)
* Vector - Vector = Vector
* Point + Vector = Point -> da m3naha eh??
  * m3naha en kan 3ndk point fl space, w 7araktha le makan tany, fa el resultant hayb2a eh? -> bzbt point bs fe mkan gded b magnitude gded.
* Point - Vector = Point. 
* Vector - Point = INVALID. -> mynf34 yabny, enta 3auz tetr7 mkan fl space mn mogrd etgah w direction, fa el point mmkn tefkr feha aknha korsy fl sha2a, w el vector hwa 3bara 3n force enta bt7otha 3l korsy 34an t7rko, fa yenf3 t2ol ana hatr7 el korsy mn el force el hazo2 beha? 
* lakn lw gm3t 3la el korsy el force el hat7rk beha da hay5leny a7ot el korsy fe mkan gded fl space. 
* w lw tr7t mno el force brdu hy5leny a7oto f makan gded.
* Point - Point = enta 3ndk korsy kan fe location x1, w b3den baa fe mkan x2, yeb2a mgmo3 el etnen hwa a?
* bzbt, hwa el vector el 5lany a7rk el korsy mn x1, le x2. 
* point + Point = invalid
* (Point + Point) / 2 = Point
------------------
### How to understand them? 
* Since w = 0 means vector 
* Since w = 1 means point
* Vector + Vector = 0 + 0 = 0 -> vector
* Vector - Vector = 0 - 0 = 0 -> vector
* Point + Vector = 1 + 0 = 1 -> point
* Point - Vector = 1 - 0 = 1 -> point
* Vector - point = 0 - 1 = -1 -> invalid
* Point - Point = 1 - 1 = 0 -> vector
* Point + Point = 1 + 1 = 2 -> invalid :) 
* (Point + Point) / 2 = (1+1) / 2 = 1 => Point
---------------------
### Matrix composition
* Badal ma a3od a3ml multilplication one by one
* v1 = M1V0
* v2 = M2V1
* v3 = M3V2 and so on
* laa ehna mmkn n2ol haga asr3 
* v3 = (M3M2M1)V0 -> da asr3 bkter. 
  * el helw fel hwar da enk bt5ly kol el matricies mogrd matrix wahda bs w shamla kol haga baa. 
  * l2n enta lw 3auz t3ml 10 transformations. 
  * w 3ndk 8 points 
  * fa lw hnshtghl bl tre2a el oula, ehna kol point han3mlha el 10 transformations.
  * yeb2a total = 10 * 8 = 80 operations
  * lakn lw ehna khadna aa el 10 transformations dol mn el awl w rohna darbenhom f b3d w tl3na matrix wahda kbera?
  * fa kda hatakhud 10 operations. 
  * w b3den baa khlas l kol point mn el 8 lw drbtha fel resultant matrix hatwslny lel haga el ana 3auzha.
  * yeb2a mehtag kman 8 operations. 
  * fa keda total = 10 + 8 = 18 operations.
  * fa awfar kter tb3n 
NOTE:
> If we have Matrix M, and Matrix N, then M * N is not equal to N * M. in the matrix operations. 

> using the same concept if we want to make rotation then scaling, this won't be equal to scaling then rotation.

> So in order to apply the MVP we use it in this order

> P * V * M. 

> because we want to apply the modling first, then we use the view matrix to allocate how we want to see the object, then finaly we multiply by the projection matrix to allocate how we want to see the object in the screen.

### TRS
* ehna mabn7bsh net3aml m3 el matricies wl matricies operations.
* 34an sa3ba w rekhma, w ktera fl 7sabat.
* fa 34an kda bnst5md el transilation, rotation, scaling methods (TRS). 
* de b7aded beha 9 no2at bs w hwa el computer baa by7wlha lel 4x4 matrix fl akher. 
*  dol bnfs el tre2a el etkmlna 3leha, fa msln el transilation, by3bro 3n awl 3 components fe akher row fl matrix. 
*  w hakaza baa. 
