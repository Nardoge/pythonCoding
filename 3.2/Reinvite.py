# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:22:41 2024

@author: nardo
"""

inviteList = ["MaYun","LiHongYan","MaHuaTeng"];

for invite in inviteList:
    print("我邀请" + invite + "参加晚餐。")
    
print("MaYun 无法出席！")

inviteList[0] = "MaS";

for invite in inviteList:
    print("我重新邀请"+ invite + "参加晚餐。")