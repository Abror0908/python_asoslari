# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:13:58 2023

@author: Abror
"""

def tyil_hisobla(ism,yosh,joriy_yil=2023):
    """Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}")
    print(f"Foydalanuvchi yoshi: {yosh}")
    tyil = joriy_yil - yosh
    print(f"Foydalanuvchi tug'ilgan yiqli': {tyil}")
tyil_hisobla('abror', 26)

def kvad_kub_hisoblash(son):
    """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati {son**2} ga va kubi {son**3} ga teng.")
kvad_kub_hisoblash(9)

def juft_toq_tek(son):
    """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son % 2 == 0:
        print(f'{son} soni bu juft son')
    else:
        print(f'{son} soni toq son')
juft_toq_tek(6)

def katta_son_top(son1,son2):
    if son1 > son2:
        print(son1)
    elif son1 == son2:
        print('Sonlar teng.')
    else:
        print(son2)
katta_son_top(-2*5, -2*6)

def daraja_hisoblsh(x,y):
    """Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya"""
    javob = x**y
    print(javob)
daraja_hisoblsh(3,4)

def daraja_hisoblsh(x,y=2):
    """Foydalanuvchidan x sonni olib, kvadratini konsolga chiqaruvchi funksiya"""
    javob = x**y
    print(javob)
daraja_hisoblsh(3)

def qoldiq_tekshirish(son):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
    for i in range(2,11):
        natija = son % i
        if natija == 0:
            print(f"70 soni {i} ga qoldiqsiz bo'linadi.")
        else:
            continue
        
qoldiq_tekshirish(70)