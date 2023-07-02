import secrets
import string

#defining variables and password length
letters = string.ascii_letters
numbers = string.digits
spec_char = string.punctuation

all = letters + numbers + spec_char
passw_length = 12


#making the password
password =""
for x in range (passw_length):
    password +="".join(secrets.choice(all))


#password criterias
while True:
    password=""

    for x in range (passw_length):
        password +="".join(secrets.choice(all))
    
    if (any(char in spec_char for char in password) and 
        sum(char in numbers for char in password) >= 1 and 
        sum(1 for i in password if i.isupper() >=1)):
        break

#final password
print(password)
