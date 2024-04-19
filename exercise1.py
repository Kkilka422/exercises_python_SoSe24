# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:19:05 2024

@author: s_kilka20
"""
def cagr_berechnung(AK, EK, t):
   AK_abs = abs(AK)
   t_abs = abs(t)
   cagr = ((EK/AK)**(1/t)-1) #*100
   return cagr



print(cagr_berechnung(100, 700, 30))

AK = 120
t=30
cagr = cagr_berechnung(100, 700, 30)
EK = AK * (1+ cagr)**t

print(EK)






    