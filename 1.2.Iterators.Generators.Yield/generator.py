import hashlib


class Country:

    def __init__( self, file_name ):
        with open(file_name) as file_data:
            self.data = []
            for r_line in file_data.readlines():
                self.data.append(hashlib.md5(r_line.encode('UTF-8')).hexdigest())

    def __iter__( self ):
        return self

    def __next__( self ):
        if not self.data:
            raise StopIteration
        return self.data.pop()


for item in Country('country.urls'):
    print(item)
