# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 08:15:14 2024

@author: nardo
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:29:26 2024

@author: nardo
"""

inviteList = ["MaYun","LiHongYan","MaHuaTeng"];

for invite in inviteList:
    print("我邀请" + invite + "参加晚餐。")
    
print("MaYun 无法出席！")

inviteList[0] = "MaS";

for invite in inviteList:
    print("我重新邀请"+ invite + "参加晚餐。")
    
print("我找到了更大的餐桌，决定多邀请两位嘉宾。")

inviteList.insert(0, "Ray");

inviteList.append("DaLong"); 

for invite in inviteList:
    print("我重新邀请"+ invite + "参加晚餐。")
    

print("收到消息，餐桌没到。只能邀请两位嘉宾。")

i = 0;

for invite in inviteList:
    if  len(inviteList) > 2:
      unInvite = inviteList.pop(0)
      print("抱歉，不能邀请"+unInvite)
      

for invite in inviteList:
    print(invite + ",你依然获得邀请。")
    
print("晚宴结束。")
del(inviteList[1]);
del(inviteList[0]);
print("在场的客人:" ) 
print(inviteList)