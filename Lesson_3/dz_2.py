def user_info(first_name, last_name, year_birth, city, email, phone):
    return f'{first_name} {last_name}, родился {year_birth}, проживает в городе {city}, ' \
           f'связаться можно по телефону {phone} и электронной почте{email}'


print(user_info(first_name=input('Ваше Имя: '),
                last_name=input('Ваша фамилия: '),
                year_birth=input('Дата рождения: '),
                city=input('Город проживания: '),
                email=input('Адрес электронной почты: '),
                phone=input('Контактный номер телефона: ')
                ))
