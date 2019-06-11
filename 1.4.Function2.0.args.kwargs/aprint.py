def adv_print(*args, **kwargs):

    def write_file(file_name, str_write):
        with open(file_name, 'a', encoding='utf-8') as write_file:
            write_file.write(str_write)

    start = ''
    max_line = 0
    position = 0
    line_position = 0
    in_file = ''
    text = []

    for arg in args:
        if len(arg) > 0:
            text = arg.split(' ')
    for kwarg in kwargs:
        if kwarg == 'max_line':
            max_line = int(kwargs[kwarg])
        elif kwarg == 'start':
            start = kwargs[kwarg]
        elif kwarg == 'in_file':
            in_file = kwargs[kwarg]

    if start != '':
        for item_start in text:
            if item_start == start:
                break
            position += 1

    for word in range(position, len(text)):
        if line_position + len(text[word]) + 5 > max_line:
            print(text[word])
            line_position = 0
            if in_file != '':
                write_file(in_file, text[word] + '\n')
        else:
            print(f'{text[word]} ', end='')
            line_position += len(text[word]) + 1
            if in_file != '':
                write_file(in_file, text[word] + ' ')
def main():
    adv_print('Подчеркивание - это соглашение на языке Python для обозначения неиспользуемой переменной '
              '(например, инструменты статического анализа не сообщают об этом как неиспользуемую переменную). '
              'В вашем случае аргумент лямбда не используется, но созданный объект - это функция с одним аргументом, '
              'которая всегда возвращает True. Итак, ваша лямбда несколько похожа на Constant Function в математике.',
               start='Python', max_line=50, in_file='text.log')


if __name__ == '__main__':
    main()