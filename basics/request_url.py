import re
import requests

URL = 'https://en.wikipedia.org/wiki/"Hello,_World!"_program'


def do_hello():
    result = requests.get(URL)
    print(re.findall('<title>(.*?)</title>', result.text)[0])
    print('Done! 🚀💐')


if __name__ == '__main__':
    do_hello()
