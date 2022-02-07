userName = 'shakhzodtojiyev'
userPassword = '12345678'

user_name = input('User name: ')
user_password = input('User password: ')
# print(type(user_password))

if user_name == userName and user_password == userPassword:
    print(f'Hello {userName}')
elif user_name != userName:
    print('Username wrong')
elif user_password != userPassword:
    print('Password wrong')
else:
    print('something wrong')