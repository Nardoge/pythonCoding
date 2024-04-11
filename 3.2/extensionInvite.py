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