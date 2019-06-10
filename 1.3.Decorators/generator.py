import hashlib
from log import log


@log('hash_debug')
def hash_string(str_hash):
    return hashlib.md5(str_hash.encode('UTF-8')).hexdigest()


def gen_hash(file_name):
    with open(file_name) as file_data:
        for r_line in file_data.readlines():
            hash = hash_string(r_line)
            yield hash


for item in gen_hash('country.urls'):
    print(item)
