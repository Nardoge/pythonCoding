# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:45:04 2024

@author: nardo
"""

cubes=[value**3 for value in range(1,11)]

for cube in cubes:
    print(cube);
    
    
print("The first three items in the list are:")   

for cube in cubes[0:3]:
    print(cube)
    
print("Three items from the middle of the list are:")
for cube in cubes[3:6]:
    print(cube)


print("Three items from the middle of the list are:")
for cube in cubes[-3:]:
        print(cube)