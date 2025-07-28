#!/usr/bin/env python 
# -*- coding:utf-8 -*-
str1="kjsaidhoqwncugiag;a;oouofhosgicbaialalqpqweuf"
k=0
for s in str1:
    if s=="a":
        k+=1
print(f"字符串中一共有{k}个a")


for a in range(1,10):
    for b in range(1,a+1):
        print(f"{b}*{a}={b*a}\t",end="")
    print("\n")
