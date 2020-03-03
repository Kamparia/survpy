# Module for survey related computations and adjustments.

#*********Module Name: SurvPy***********
#*********Module Version: 1.0.1*********
#*******Publisher: Geospatech NG********
#********Author: Somide Olaoye A.*******
#******Year of Publication: 2013********
#************License: Freeware**********

'''
Description: 
SurvPy is a Python based module developed by Geospatech NG to enable the community of Python users to be able to execute land surveying related computations using a set of properly defined functions.

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
'''

import math
import os
import sys

#This function does conversion from feets to meters
def ft2m(feets):
    f = float(feets)
    meters = round(f * 0.3048,3)
    print(feets,'feets equals',meters,'meters')

#This function does conversion from meters to feets
def m2ft(meters):
    m = float(meters)
    feets = round(m * 3.280839895,3)
    print(meters,"meters equals",feets,"feets")

#This function does conversion from square meters to acres
def sqm2acr(area_sqmts):
    a = float(area_sqmts)
    acres = round(a / 4048.583,3)
    print(area_sqmts,"sq.mts equals",acres,"acres")

#This function does conversion from acres to sqaure meters
def acr2sqm(acres):
    a = float(acres)
    area_sqmts = round(a * 4048.583,3)
    print(acres,"acres equals",area_sqmts,"sq.mts")

#This function calculates the approximate numbers of plots that can be estimated in an area of sq.mts
def plots(area,lenght,breadth):
    a = float(area)
    b = lenght * breadth
    plot = a/b
    plots = round(plot,0)
    print("There exist approximately",plots,"plots in",area,"sq.mts")

#This function does conversion from degrees to decimal
def deg2dec(deg,min,sec):
    d = float(deg)
    m = float(min)
    s = float(sec)
    decimal = round((d + (m/60) + (s/3600)),6)
    print("Conversion from degrees to decimal:", decimal)

#This function does conversion from decimal to degrees
def dec2deg(decimal):
    d = float(decimal)
    dd = int(d)
    m = (d - dd) * 60
    mm = int(m)
    s = (m - mm) * 60
    ss = int(s)
    print("Conversion from decimal to degrees:", dd,mm,ss)

#This function converts from radians to degrees
def rad2deg(radians):
    a = float(radians)
    y = math.degrees(a)
    d = float(y)
    dd = int(d)
    m = (d - dd) * 60
    mm = int(m)
    s = (m - mm) * 60
    ss = int(s)
    print("Degrees =",dd,mm,ss)

#This function converts from degrees to radians
def deg2rad(deg,min,sec):
    d = float(deg)
    m = float(min)
    s = float(sec)
    decimal = round((d + (m/60) + (s/3600)),3)
    radians = round(math.radians(decimal),4)
    print("Radians =",radians)
    
#Convertion from Grads to Degrees
def grad2deg(grads):
    deg = 0.9 * grads
    d = float(deg)
    dd = int(d)
    m = (d - dd) * 60
    mm = int(m)
    s = (m - mm) * 60
    ss = int(s)
    print(grads,"Grads =",dd,mm,ss,"degrees")

#This function deduce the mean angular observation on
#a zero of left and right faces of the theodolite
def angded(L1,L2,R2,R1):
    dL = L2 - L1
    dR = R2 - R1
    A = (dL + dR)/2
    print(" Deduced horizontal angle:", A)

#This function computes the area of a triangle based on Hero's formula
def herotrig(a,b,c):
    s = (a+b+c)/2
    a = round((math.sqrt(s*(s-a)*(s-b)*(s-c))),3);
    print("Area of a triangle using Hero's formula:", a)

#This function calculates the distance between
#the coordinates of two given known points
def distance(Pnt1_E,Pnt1_N,Pnt2_E,Pnt2_N):
    dx = float(Pnt2_E - Pnt1_E)
    dy = float(Pnt2_N - Pnt1_N)
    distance = round(math.sqrt(dy**2 + dx**2),3)
    print("Distance is:", distance)

#This function calculates the bearing between
#the coordinates of two given known points
def bearing(Pnt1_E,Pnt1_N,Pnt2_E,Pnt2_N):
    dx = float(Pnt2_E - Pnt1_E)
    dy = float(Pnt2_N - Pnt1_N)
    bearing = round(math.degrees(math.atan(dx/dy)),3)
    print("Forward Bearing from Point 1 to Point 2 is:", bearing)

#This funcion computes both slope and horizontal
#distance measurement of a measured distance
def slope(distance,vangle):
    d = float(distance)
    v = float(90-vangle)
    hordist = round(d*(math.cos(math.radians(v))),3)
    slope = d - hordist
    print("Slope Correction is:", slope,", Horizontal Distance:",hordist)

#This function does forwad computation
def fwdcomp(Pnt1_E,Pnt1_N,distance,bearing):
    d = float(distance)
    b = float(bearing)
    dx = d * math.sin(math.radians(b))
    dy = d * math.cos(math.radians(b))
    x2 = round((Pnt1_E + dx),3)
    y2 = round((Pnt1_N + dy),3)
    print("Output Coordinate:", y2,"N,", x2,"E")

#This function does backward computation on an horizontal plane
def bckcomp(Pnt1_E,Pnt1_N,Pnt2_E,Pnt2_N):
    dx = float(Pnt2_E - Pnt1_E)
    dy = float(Pnt2_N - Pnt1_N)
    distance = round(math.sqrt(dy**2 + dx**2),3)
    bearing = round(math.degrees(math.atan(dx/dy)),3)
    d = float(bearing)
    dd = int(d)
    m = (d - dd) * 60
    mm = int(m)
    s = (m - mm) * 60
    ss = int(round(s,0))
    print("Distance:",distance,"Bearing:",dd,mm,ss)
    
#This function computes the horizontal distance
#using tacheometric method of surveying
def tachydist(U,M,L,vangle):
    u = float(U)
    m = float(M)
    l = float(L)
    v = float(vangle)
    s = u - l
    d = round((100 * s * ((math.cos(math.radians(v)))**2)),3)
    print("Tacheometric Distance:", d)

#This function computes the reduced level of a print feets,"feets equals",meters,"meters"point
#using tacheometric method of surveying
def tachylevel(RL,hi,U,M,L,vangle):
    rl = float(RL)
    HI = float(hi)
    u = float(U)
    m = float(M)
    l = float(L)
    v = float(vangle)
    s = u - l
    V = (0.5*100*s*math.sin(math.radians(2*v)))
    hb = round((rl + HI + V - m),3)
    print("Reduced Level:", hb)

#This function converts from geodetic coordinate system
#to a plane(cartesian) coordinate system
def ellip2cart(latitude,longitude,height):
    c = float(latitude)
    d = float(longitude)
    g = float(height)
    a = 6378137.000
    f = 1/298.25722357
    e = math.sqrt((2*f) - pow(f,2))
    e2 = pow(e,2)
    n = math.sqrt(1 - (e2*(math.sin(math.radians(c)))))
    N = a/n
    X = (N + g)*(math.cos(math.radians(c)))*(math.cos(math.radians(d)))
    Y = (N + g)*(math.cos(math.radians(c)))*(math.sin(math.radians(d)))
    Z = ((N*(1 - e2)) + g)*math.sin(math.radians(c))
    print("Ellipsoidal Northings:", Y)
    print("Ellipsoidal Eastings:", X)
    print("Ellipsoidal Height:", Z)
    
