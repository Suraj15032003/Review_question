import pandas as pd 
import re 

data ={
        'Firstname':[],
        'Lastname':[],
        'Age': [],
        'PhoneNumber':[]
    }
while True:
    fname=input("First Name : ")
    if re.match(r'^[A-Za-z]{3,}$|[A-Za-z]{3,}$',fname):
        data['Firstname'].append(fname)
        break
    print("Letters only, min 3 chars")

while True:
    lname=input("Last Name : ")
    if re.match(r'^[A-Za-z]{3,}$|[A-Za-z]{3,}$',lname):
        data['Lastname'].append(lname)
        break
    print("Letters only, min 3 chars")

while True:
    age=input("Age : ")
    if re.match(r'^(1[8-9]|[2-9][0-9])$',age):
        data['Age'].append(int(age))
        break
    print("18-99 only")
    
while True:
    phone=input("Phone number : ")
    if re.match(r'^\d{10}$',phone):
        #for encryption
        masked_phone = phone[:3]+ 'xxxxxxx'
        data['PhoneNumber'].append(masked_phone)
        #data['PhoneNumber'].append(phone)
        break
    print("10 digits ")
    
df = pd.DataFrame(data)
print(df)
    

