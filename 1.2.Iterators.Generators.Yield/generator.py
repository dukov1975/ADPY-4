import hashlib


def gen_hash(file_name):
    with open(file_name) as file_data:
        for r_line in file_data.readlines():
            yield hashlib.md5(r_line.encode('UTF-8')).hexdigest()


for item in gen_hash('country.urls'):
    print(item)
