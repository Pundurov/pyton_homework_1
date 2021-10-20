from sys import argv

print('Заработная плата: ')

script_name, user_num_of_hours, user_rate, user_prize = argv

int_user_num_of_hours = int(user_num_of_hours)
int_user_rate = int(user_rate)
int_user_prize = int(user_prize)

print(f'{int_user_num_of_hours * int_user_rate + int_user_prize} р.')

