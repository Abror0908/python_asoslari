# print('Kiritilgan sonning kvadratini qaytaruvchi dastur')
# savol = 'Istalgan sonni kiriting: '
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing)"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
#________________________________________________________________# _________
# print('Kiritilgan sonning kvadratini qaytaruvchi dastur')
# savol = 'Istalgan sonni kiriting: '
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing)"
# qiymat = ''
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
#________________________________________________________________________
# print('Kiritilgan sonning kvadratini qaytaruvchi dastur')
# savol = 'Istalgan sonni kiriting: '
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing)"
# qiymat = ''
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
#___________________________________________________________________________
# savollar = "Yaxshi ko'rgan kitoblaringizni kiriting: "
# savollar += "(to'xtash uchun 'stop' tugmasini)"
# javob = ''
# while True:
#     javob = input(savollar)
#     if javob == 'stop':
#         break
#     else:
#         print(f"Sizni yaxshi ko'rgan kitobingiz - {javob}")
#__________________________________________________________________________
# print('Muzeyda chipta narxini aniqlash dasturi')
# savol = "Yoshingizni kiriting: "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing)"
# javob = ''
# while True:
#     javob = input(savol)
#     if javob == 'exit':
#         print('Dastur tugadi!')
#         break
#     elif 0<int(javob)<=7:
#         print(f'bilet narxi 2000 sum')
#     elif 7<int(javob)<=18:
#         print(f'bilet narxi 3000 sum')
#     elif 18<int(javob)<=65:
#         print(f'bilet narxi 10000 sum')
#     elif 65<int(javob):
#         print(f'bilet narxi bepul')
#_______________________________________________________________________
print("Kiritilgan sonning ildizini qaytaruvchi dastur.")
savol = "Musbat son kiriting: "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        print('Dastur tugadi!')
        break
    elif float(qiymat)<=0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")