v1 = 'thirty'
v2 = 'days'
v3 = 'of'
v4 = 'python'
variable = v1 + v2 + v3 + v4

v5 = 'coding'
v6 = 'for'
v7 = 'all'
variable2 = v5 + v6 + v7

v8 = 'company'
variable3 = v8
print(v8)
len('company')
'company'.upper()
'company'.upper().lower()

capitalizar='coding'.capitalize()
titulo='for'.title()
usarswapcase='all'.swapcase()

cut="coding for all".split()
for word in cut:
    print(word[0])

verificar="coding for all".index
print(verificar)

cambiar="coding for all"
print(cambiar.replace('coding' , 'python'))

cambiar="python for all"
print(cambiar.replace('python for all' , 'python for everyone'))

separar="coding for all"
print(separar.split())
separar="coding, for, all"
print(separar.split(','))

cadena="facebook, google, microsoft, appel, IBM, oracle, amazon"
print(cadena.split(','))

caracter="coding for all"
first_letter=caracter[0]
print(first_letter)

caracter="coding for all"
last_letter=caracter[13]
print(last_letter)

caracter="coding for all"
indice='for all'
print(caracter.index(indice))
print(caracter.index(indice, 10))

abreviatura="python for everyone"
print(abreviatura.replace ('python for everyone', 'pyfoev'))

abreviatura="coding for all"
print(abreviatura.replace('conding for all', 'cofoal'))

variable="coding for all"
indice='c'
print(variable.index(indice))
print(variable.index(indice, 0))

variable="coding fo3r all"
indice='for'
print(variable.index(indice))
print(variable.index(indice, 7))

variable="coding for all"
print(variable.rfind('l'))

oracion='You cannot end a sentence with because because because is a conjunction'
print(oracion.index('because'))

oracion='You cannot end a sentence with because because because is a conjunction'
print(oracion.rindex('because'))

#25
oracion= 'You cannot end a sentence with because because because is a conjunction'
palabra='because'
print(oracion.index(palabra))
print(oracion.rindex(palabra))

oracion= 'You cannot end a sentence with because because because is a conjunction'
cortar='bacause because because'
print(oracion.strip('because because because'))
print(oracion.index(cortar))



