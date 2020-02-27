countries={'us':'USA','fr':'France','uk':'Eng'}
print(countries.get('zb','Unknown'))
# on the phone

countries['de']='Germany'
countries.update({'de':'Germany'})
print(countries.get('de'))

del countries['de']
print(countries)

print(countries.keys())
print(countries.items())

found1='ca' in countries
print(found1)

found2='us' in countries
print(found2)

print("fr" in countries)

for key, value in countries.items():
    print(key,value)

for key in countries.keys():
    print(key)

for value in countries.values():
    print(value)