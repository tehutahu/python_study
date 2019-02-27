
while True:
    age = input('input your age\n')
    if age.isdecimal():
        break
    print('not number\n')

while True:
    password = input('input your password\n')
    if password.isalnum():
        break
    print('password must have alphabet or number')
