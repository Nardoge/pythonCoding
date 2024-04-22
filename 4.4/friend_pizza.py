# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:23:39 2024

@author: nardo
"""

pizzas = ["达美乐","尊宝","快速"]


friend_pizzas = pizzas[:];

pizzas.append("快递披萨");


friend_pizzas.append("强记披萨");


print("我的披萨列表:")

for pizza in pizzas:
    print(pizza);
    

print("我朋友的披萨列表:")

for pizza in friend_pizzas:
    print(pizza);    