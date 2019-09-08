In archimedes.py, implement the archimedes in Listings 2.2 and 2.4 in the chapter. 2.7 Modify the archimedes function to take the radius as a parameter. Can you get a better answer more quickly using a larger circle?
import math  

def archimedes(numsides):  
    innerangleB = 360.0/numsides  
    halfangleA = innerangleB/2  
  
    onehalfsideS = math.sin(math.radians(halfangleA))  
    sideS = onehalfsideS * 2  
  
    polygonCircumference = numsides * sideS  
    pi = polygonCircumference/2  
  
    return pi  
Listing 2.2

>>> archimedes  
<function archimedes at 0x103e0b0>  
>>> archimedes(100)  
3.14263 
>>> archimedes(1000)  
3.14263
>>> archimedes(10000)  
3.1416
   
>>> for sides in range(8,100,8):  
        print(sides,archimedes(sides))  
