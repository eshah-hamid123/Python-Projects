customer = {
    "name": "Eisha",
    "age" : 20,
    "verification" : True,
    'no' : 5
}
print(customer["name"])
print(customer["no"])
customer['old'] = 'yes'
print(customer)
print(customer.get('age'))
print(customer.get('ages'))
print(customer.get('verification'))
print(customer.get('DOB' , 'MArch 06, 2002'))
#create an empty dictonary
empty_dic = {}
customer['age'] = 19
print(customer)
#loop through dictonary
for key in customer:
    print(f'{key} : {customer[key]}')