akam = {
    'ismi': 'Abbos',
    'tug`ilgan yili': '1992',
    'shahri': 'Zarbdor'
}
#_____________________________________________________
taomlar = {
    'onam': 'manti',
    'akam': 'osh',
    'opam': 'manti',
    'singlim': 'jarkop',
    'men': 'somsa'
}
for i,n in taomlar.items():
    print(f'{i} yaxshi ko`rgan taom {n}')
#________________________________________________________
yangi_dict = {
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
soz = input(f'Biror so`z kiriting: ').lower()
print(yangi_dict.get(soz,"Bunday so'z mavjud emas"))
#________________________________________________________

soz = input(f'Biror so`z kiriting: ').lower()
tarjima = yangi_dict.get(soz)
if tarjima == None:
    print('Bunday so`z mavjud emas')
else:
    print(f'{soz.title()} - {tarjima} deb tarjima qilinadi')

#______________________________________________________________