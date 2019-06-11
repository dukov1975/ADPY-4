class Contact:
    def __init__(self, first_name, last_name, phone_number, favorite=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite = favorite
        self.arg = args
        self.kwarg = kwargs

    def __str__(self):
        favorite = (lambda x: 'Да' if x else 'Нет')
        print_additional = ''
        for additional in self.kwarg:
            print_additional += f'\n\t\t{additional} : {self.kwarg[additional]}'
        return_contact_string = f'Имя: {self.first_name}\n' \
                                f'Фамилия: {self.last_name}\n' \
                                f'Телефон: {self.phone_number}\n' \
                                f'В избранных: {favorite(self.favorite)}\n' \
                                f'Дополнительная информация: {print_additional}'
        return return_contact_string





