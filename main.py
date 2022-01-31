import random
import string

length = int(input('enter length: '))
while True:
    chars = string.ascii_letters + string.digits + '-*!@#$%^&*(){}|><'
    password = ''.join([random.choice(chars) for i in range(length)])
    print('your password is \"{}\"'.format(password))
    while True:
        answer = input(' you like it? (N/Y)')
        if answer == 'y' or answer == 'Y' or answer == 'n' or answer == 'N':
            break
    if answer == 'y' or answer == 'Y':
        break
