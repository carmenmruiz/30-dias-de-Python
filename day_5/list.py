empty_list=list()

fruit=['mango','platano','uvas','sandia','melon']
len(fruit)

first_fruit=fruit[0]
print(first_fruit)
middle_fruit=fruit[2]
print(middle_fruit)
last_fruit=fruit[4]
print(last_fruit)

tipos_de_datos=['carmen','16','1,68','soltera','jerez']

companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(companies)

number_of_companies=7
print(number_of_companies)

first_company=companies[0]
print(first_company)
middle_company=companies[3]
print(middle_company)
last_company=companies[6]
print(last_company)


companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
companies.append('TI')
print(companies)
companies.insert(3, 'TI')
print(companies)

companies=['Facebook', 'Google', 'Microsoft','IT', 'Apple', 'IBM', 'Oracle', 'Amazon']
mayuscula='Appel'
mayuscula.upper('Apple')
print(mayuscula)

join1='#'.join(companies)
print(join1)

companies=['Facebook', 'Google', 'Microsoft','IT', 'Apple', 'IBM', 'Oracle', 'Amazon']
does_exits='Apple' in fruit
print(does_exits)

companies.sort()
print(companies)
companies.sort(reverse=True)
print(companies)

companies=['Oracle', 'Microsoft', 'IT', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']
slice(companies)[0:2]
slice(companies)[5:7]
slice(companies)[3:4]

companies.remove('Oracle')
print(companies)

companies.remove('IBM','Google')
print(companies)

companies.pop()
print(companies)

companies.clear()
print(companies)

del companies

front_end = ['HTML', 'CSS', 'JS', 'Reaccionar', 'Redux']
back_end = ['Nodo','Express', 'MongoDB']

full_stuck=front_end+back_end
print(full_stuck)

full_stuck.insert(5, 'Python')
print(full_stuck)
full_stuck.insert(6, 'SQL')
print(full_stuck)
























