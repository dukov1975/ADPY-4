import datetime


def log(file_log):
    def func_decorator(func):
        def wrap_log(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_log + '.log', 'a') as log_file:
                log_file.write(f'{datetime.datetime.now()} '
                               f'{func.__name__} '
                               f'args{args} '
                               f'kwargs{kwargs} '
                               f'результат {result}\n')

            return result
        return wrap_log
    return func_decorator


# @log('clients')
# def client_add(cli_id, name):
#     print(cli_id, name)
#     return name
#
#
# @log('accounts')
# def account_add(acc_id, account):
#     print(acc_id, account)
#     return account
#
#
# client_add(9, 'ПАО РОСБАНК')
# account_add(9, '30101810000000000256')
