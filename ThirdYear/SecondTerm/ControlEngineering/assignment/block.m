% creating the blocks
B1 = tf(1, -50); 
B2 = tf([100,100,55], 1); 
B3 = tf (1, 50); 
B4 = tf ([100,100,55] , 1); 

% creating matrix which contains all our blocks 
BlockMatrix = append (B1,B2, B3,B4); 

% creating connect maps 
% Block 3 feeds block 4 
% Block 2 feeds block 3 
% Block 1 feeds block 2
% Block 4 feeds block 1 but in negative value. (circular). 
%connect_map = [ 4 , 3 ;  ...
 %               3, 2; ...
  %              2, 1; ... 
   %             1, -4];

% define it using series
res1 = series (B2, B3);
res2 = series ( res1, B4); 
X2 = feedback (B1, res2); 
transferX2withU = minreal (X2); 
transferX2withU 

% defining ip/op locations 
input_loc = 1; 
output1_loc= 3; 
output2_loc= 1; 

% defining systems 
combinedSys = series (B1, B2, B3, B4); 
finalSys = feedback( combinedSys, [1]); 
finalSys
