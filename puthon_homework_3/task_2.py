def user_data(f_name, l_name, birth_d, city, email, phone):
    return {'Имя': f_name, 'Фамилия': l_name,
            'Дата рождения': birth_d, 'Город': city,
            'Эл. почта': email, 'Телефон': phone}


user_dict = user_data(f_name='Иван',
                      l_name='Иванов',
                      birth_d='01.01.1991',
                      city='Чехов',
                      email='Ivan@ya.ru',
                      phone='304-18-95')

for key, value in user_dict.items():
    print(f'{key}: {value}')
