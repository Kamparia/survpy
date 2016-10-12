# SurvPy

SurvPy is a Python based module that enables users to be able to execute basic land survey related computations using a set of properly defined functions

LIST OF FUNCTIONS
1. ft2m(feets) - This function does conversion from feets to meters
2. m2ft(meters) - This function does conversion from meters to feets
3. sqm2acr(area_sqmts) - This function does conversion from square meters to acres
4. acr2sqm(acres) - This function does conversion from acres to sqaure meters
5. plots(area_sqmts,stnd_lenght,stnd_breadth) - This function calculates the approximate numbers of plots that can be estimated in an area of sq.mts
6. deg2dec(deg,min,sec) - This function does conversion from degrees to decimal
7. dec2deg(decimal) - This function does conversion from decimal to degrees
8. rad2deg(radians) - This function converts from radians to degrees
9. deg2rad(deg,min,sec) - This function converts from degrees to radians
10. grad2deg(grads) - Units convertion from Grads to Degrees
11. angded(L1,L2,R2,R1) - This function deduce the mean angular observation on a zero of left and right faces of the theodolite
12. herotrig(a,b,c) - This function computes the area of a triangle based on Hero's formula
13. distance(Pnt1_E,Pnt1_N,Pnt2_E,Pnt2_N) - This function calculates the distance between the coordinates of two given known points
14. bearing(Pnt1_E,Pnt1_N,Pnt2_E,Pnt2_N) - This function calculates the bearing between the coordinates of two given known points
15. slope(distance,vangle) - This funcion computes both slope and horizontal distance measurement of a measured distance
16. fwdcomp(Pnt1_E,Pnt1_N,distance,bearing) - This function does forward computation on an horizontal plane
17. bckcomp(Pnt1_E,Pnt1_N,Pnt2_E,Pnt2_N) - This function does backward computation on an horizontal plane
18. tachydist(U,M,L,vangle) - This function computes the horizontal distance using tacheometric method of surveying
19. tachylevel(RL,hi,U,M,L,vangle) - This function computes the reduced level of a point using tacheometric method of surveying
20. ellip2cart(latitude,longitude,height) - This function converts from geodetic coordinate system to a plane(cartesian) coordinate system
