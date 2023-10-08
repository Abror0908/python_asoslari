python_dict = {
    'variable':'o`zgaruvchi',
    'integer':'butun son',
    'float':'o`nli kasr',
    'string':'matn',
    'list':'ro`yxat',
    'tuple':"o'zgarmas ro'yxat",
    'dictionary':'lugat',
    'function':'funksiya',
    'loop':'tsikl',
    'set':'to`plam'
}
for kalit,qiymat in python_dict.items():
    print(f'{kalit.title()} - {qiymat.title()}')
#_____________________________________________________________
#rint('Dunyo davlatlari:  Davlatlarning poytaxtlari:')
dav = {
    'uzbekistan':'toshkent',
    'turkiya':'istanbul',
    'rossiya':'moskva',
    'qozog`iston':'nursulton',
    'qirg`iziston':'bishkek',
    'tojikiston':'dushanbe',
    'ozarbayjon':'boku'
}
print('\nDunyo davlatlari:')
for davlat in sorted(dav):
    print(f'{davlat.title()}')

print('\nDavlatlarning poytaxtlari:')
for poytaxt in sorted(dav.values()):
    print(f'{poytaxt.title()}')
#__________________________________________________________________________________
davlat = input('Qaysi davlatning poytaxtini bilishni xohlaysiz? - ').lower()
capital = dav.get(davlat)
if capital == None:
    print('Kechirasiz, bizda bu haqida ma`lumot mavjud emas')
else:
    print(f'{davlat.title()}ning poytaxti {capital.title()} shahri')
#___________________________________________________________________________________
ovqatlar = {
    'osh':'10000',
    'lagmon':'8000',
    'manti':'10000',
    'somsa':'5000',
    'shashlik':'15000',
    'jiz':'12000',
    'shorva':'8000',
    'tandir':'15000',
    'non':'3000',
    'choy':'1500'
}
taom1 = input('1 - taom: ')
taom2 = input('2 - taom: ')
taom3 = input('3 - taom: ')

zakaz_1 = ovqatlar.get(taom1)
if zakaz_1 == None:
    print(f'Kechirasiz bizda {taom1} yo`q')
else:
    print(f'{taom1.title()}:{zakaz_1}')

zakaz_2 = ovqatlar.get(taom2)
if zakaz_2 == None:
    print(f'Kechirasiz bizda {taom2} yo`q')
else:
    print(f'{taom2.title()}:{zakaz_2}')

zakaz_3 = ovqatlar.get(taom3)
if zakaz_3 == None:
    print(f'Kechirasiz bizda {taom3} yo`q')
else:
    print(f'{taom3.title()}:{zakaz_3}')
#_________________________________________________________________________________
print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f'{n+1} - taom: ').lower())
for buyurtma in buyurtmalar:
    if buyurtma in ovqatlar:
        print(f'{buyurtma.title()} {ovqatlar[buyurtma]} so`m')
    else:
        print(f'Kechirasiz biza {buyurtma.title()} yo`q')
#__________________________________________________________________________________