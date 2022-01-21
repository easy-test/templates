#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-01-06 20:36:46
# @Author  : zzz {easy-quest@vk.com}
# @Link    : https://github.com/easy-quest/
# @Version : 1.0.0

import random
from os import system as cmd
from time import sleep


# def Generate(): #function generates a random 6 digit number
#     code = ''
#     for i in range(6):
#         code += str(random.randint(0,9))
#     return code

# print(Generate()+".txt")

def Ft():
    """Генерация рандомного имени файла"""
    code = ''
    for i in range(18):
         code += str(random.randint(0,9))
    return code

# print(Ft()+".png")