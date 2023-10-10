buxoriy = {
    "ism": "Abu Abdulloh Muhammad ibn Ismoil",
    "tyil": 810,
    "vyil": 870,
    "tjoy": "Buxoro",
}

qodiriy = {"ism": "Abdulla Qodiriy", "tyil": 1894, "vyil": 1938, "tjoy": "Toshkent"}

vohidov = {"ism": "Erkin Vohidov", "tyil": 1936, "vyil": 2016, "tjoy": "Farg'ona"}

navoiy = {"ism": "Alisher Navoiy", "tyil": 1441, "vyil": 1501, "tjoy": "Xirot"}

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    print(f'{shaxs["ism"]} {shaxs["tyil"]} - yilda {shaxs["tjoy"]} shahrida tug`ilgan.'
    f' {shaxs["vyil"] - shaxs["tyil"]} yil umr ko`rgan.')
#___________________________________________________________________________________________
buxoriy['asar'] = ['Al-jome` as sahih','Al-adab al mufrad']
qodiriy['asar'] = ['O`tgan kunlar','Obid ketmon']
vohidov['asar'] = ['Tong nafasi','O`zbegim']
navoiy['asar'] = ['Xamsa','Lison ut-Tayr']

for muallif in shaxslar:
    print(f'{muallif["ism"]} ning mashxur asarlari:')
    for i in muallif['asar']:
        print(i)
#___________________________________________________________________________________________
kino = {
    'sardor': ['forsaj', 'terminator'],
    'ahmad': ['qasoskorlar', 'avatar'],
    'alisher': ['titanik', '2+1']
}
print(kino)

for i in kino:
    print(f'{i.title()}ning sevimli kinolari:')
    for n in kino[i]:
        print(n)
#_____________________________________________________________________________________
davlatlar = {
    'uzbekistan': {'poytaxti':'toshkent', 'hududi':'448978 kv.km', 'aholisi': '33000000', 'pul birligi': 'sum'},
    'rossiya': {'poytaxti':'moskva', 'hududi':'17098246 kv.km', 'aholisi': '144000000', 'pul birligi': 'rubl'},
    'aqsh': {'poytaxti':'vashington', 'hududi':'9631418 kv.km', 'aholisi': '327000000', 'pul birligi': 'dollar'}
}
for dav in davlatlar:
    print(f"{dav.title()}ning poytaxti {davlatlar[dav]['poytaxti'].title()} shahri")
    for key,value in davlatlar[dav].items():
        if key != 'poytaxti':
            print(f'{key.title()} : {value}')
#___________________________________________________________________________________________________________
davlat = input('Davlat nomini kiriting: ')
if davlat in davlatlar:
    print(f"{davlat.title()}ning poytaxti {davlatlar[davlat]['poytaxti'].title()} shahri")
    for key,value in davlatlar[davlat].items():
        if key != 'poytaxti':
            print(f'{key.title()} : {value}')
#____________________________________________________________________________________________________________
