

import math
import sys
from os import rename

import requests

name = input('Your name?')
print("hello,",name)

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return(greeting)

#r = requests.get('https://www.irobot.com')
r = requests.get('https://coreyms.com')
print(r.status_code)
# print(greet('John'))
