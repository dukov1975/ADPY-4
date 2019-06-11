from contact import Contact
from phonebook import Phonebook

def main():
    phone_book = Phonebook()
    phone_book.add_contact(Contact('Дмитрий', 'Дюков', '+70000000000',
                                   email='dukov@gmail.com', telegram='@dukov', email2='dukov@icloudpockeyt.ru', facebook='DyukovDmitry'))
    phone_book.add_contact(Contact('Эмануил', 'Виторган', '+70000000001',
                                   email='emavit@gmail.com', telegram='@emsvit'))
    phone_book.add_contact(Contact('Тюльпек', 'Ганджубасов', '+70000000002',
                                   favorite=True, email='gandzhubasov@gmail.com', telegram='@gandzhubasov'))
    phone_book.add_contact(Contact('Курмультук', 'Ильясов', '+70000000003',
                                   favorite=True, email='mudeni@gmail.com', telegram='@mudeni'))
    phone_book.add_contact(Contact('Зугинтульба', 'Иванова', '+70000000004',
                                   favorite=True, email='scuko@gmail.com', telegram='@eultubey'))

    print('=====================================Печать всех =====================================================')
    phone_book.print_contacts()
    print('=====================================Удаление по номеру ==============================================')
    phone_book.delete_contact('+70000000000')
    print('=====================================Показать избраных ===============================================')
    phone_book.print_favorite()
    print('=====================================Поиск по Имени и Фамилии ========================================')
    phone_book.search_contact('Тюльпек', 'Ганджубасов')

if __name__ == '__main__':
    main()
