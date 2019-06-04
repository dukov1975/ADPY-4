import json
import wikipedia


class Country:

    def __init__(self):
        with open('countries.json') as jdata:
            self.data = list(json.load(jdata))

    def __iter__(self):
        return self

    def __next__(self):
        if not self.data:
            raise StopIteration
        return self.data.pop()


with open('country.urls', 'w') as write_file:

    for item in Country():
        try:
            page = wikipedia.page(item['name']['official'])
            write_file.write('{0} {1}\n'.format(item['name']['official'], page.url))
        except wikipedia.exceptions.PageError:
            write_file.write('{0} {1}\n'.format(item['name']['official'], 'Page Error'))
        except wikipedia.exceptions.DisambiguationError:
            write_file.write('{0} {1}\n'.format(item['name']['official'], 'DisambiguationError'))
        print(item['name']['official'])

