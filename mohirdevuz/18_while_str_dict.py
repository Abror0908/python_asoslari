# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:34:03 2023

@author: Abror
"""
# =============================================================================
# 
# ismlar = []
# 
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# =============================================================================
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
#     
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
# 
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
# =============================================================================
# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# print(cars)
# =============================================================================
# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
# =============================================================================
# print('Foydalanuvchidan buyurtma qabul qiluvchi dastur.')
# buyurtmalar = []
# ishora = True
# while ishora:
#     buyurtma = input('Buyurtma nomini kiriting: ')
#     buyurtmalar.append(buyurtma)
#     javob = input("Yana burtma uchun mahsulot kiritishni xohlaysizmi? (ha/yo'q) ")
#     if javob == "yo'q":
#         ishora = False
# =============================================================================
# print("e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur.")
# mahsulotlar = {}
# n=1
# while True:
#     mahsulot = input(f'{n} - mahsulot nomini kiriting: ')
#     mahsulotlar[mahsulot] = input(f'{n} - mahsulot narxini kiriting:')
#     javob = input("Davom etishni xohlaysizmi? (ha/yo'q)")
#     n+=1
#     if javob == "yo'q":
#         break
# =============================================================================
# buyurtmalar = ['olma', 'nok', 'banan', 'qulupnay']
# mahsulotlar = {'olma': '6000', 'banan': '9000', 'uzum': '8000', 'nok': '10000', 'gilos': '9000', 'olcha': '8000'}
# 
# for buyurtma in buyurtmalar:
#     if buyurtma in mahsulotlar:
#         print(f"{buyurtma}ning narxi {mahsulotlar[buyurtma]} sum.")
#     else:
#         print(f"{buyurtma} mavjud emas.")
# =============================================================================
# Yana boshqa variant
buyurtmalar = ["olma", "anjir", "uzum", "qovun"]
mahsulotlar = {"olma": 20000, "shaftoli": 25000, "tarvuz": 18000, "uzum": 22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")