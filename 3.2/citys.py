# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:17:57 2024

@author: nardo
"""

citys= ["广州","上海","苏州","北京","南京"]

print("去过的城市数量" + str(len(citys)));

for city in citys:
     print("去过的城市：" + city);
     
print("好像第一个城市搞错了。")     

citys[0] = "昆明";


for city in citys:
     print("去过的城市：" + city);
     

print("不想再去的城市是:" + citys.pop(0));

citys.append("杭州");

citys.insert(0, "无锡");

citys.append("佛山");

del(citys[0]);


for city in citys:
     print("去过的城市：" + city);
     

citys.remove("佛山");     


print(str(len(citys)));

     



