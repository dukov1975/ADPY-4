from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
for contact in contacts_list[1:]:
    parse_fio = re.split('[\s+]', f'{contact[0]} {contact[1]} {contact[2]}')
    contact[0] = parse_fio[0]
    contact[1] = parse_fio[1]
    contact[2] = parse_fio[2]
    clean_number = re.sub('(\+7\s*|^8[\s*]|^8)([\d+]{1,3}|\(\d+\))\s*(\-|)', '', contact[5])
    clean_number = re.sub('(\-|\(|\)|[^\w\s])', '', clean_number)
    contact[5] = '' if clean_number == '' else f'+7(495){clean_number}'
out_list = list()
double_record = False
for item in contacts_list:
    if len(out_list) == 0:
        out_list.append(item)
    for out_item in out_list:
        if out_item[0] == item[0]:
            double_record = True
            if out_item[3] == '':
                out_item[3] = item[3]
            if out_item[4] == '':
                out_item[4] = item[4]
            if out_item[5] == '':
                out_item[5] = item[5]
            if out_item[6] == '':
                out_item[6] = item[6]
    if not double_record:
        out_list.append(item)
    else:
        double_record = False


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
# Вместо contacts_list подставьте свой список
  datawriter.writerows(out_list)
