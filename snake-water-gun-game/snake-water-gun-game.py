#snake, water, gun

import random
choices=['snake','water','gun']
computer=random.choice(choices).lower()
user=input('enter your choice from (snake,water,gun)').lower()
print(f'user chose {user}')
print(f'computer chose {computer}')
if computer=='snake' and user=='water':
            print('computer won and user lost!')
elif computer=='water' and user=='snake':
            print('user won and computer lost!')
elif computer=='snake' and user=='gun':
            print('user won and computer lost!')
elif computer=='gun' and user=='snake':
            print('computer won and user lost!')
elif computer=='gun' and user=='water':
            print('user won and computer lost!')
elif computer=='water' and user=='gun':
            print('computer won and user lost!')
elif user not in choices:
        print(f'{user} is an invalid choice!')
else:
            print('its a draw!')



