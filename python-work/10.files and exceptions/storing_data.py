#stroring a list of numbers.py

import json

numbers =  [2,3,4,5,7,8,9]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)