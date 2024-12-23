# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:44:38 2024

@author: nardo
"""

age = 1

if age < 2:
    print("你是婴儿")
elif age >= 2 and age < 4:
    print("你正蹒跚学步") 
elif age >= 4 and age <13:
    print("你是儿童")    
elif age >= 13 and age < 20:
    print("你是青少年")
elif age >= 20 and  age < 65:
    print("你是成年人")
elif age >= 65:
    print("你是老年人")