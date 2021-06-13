#module should always be at the top of the program unless there is comments
import pizza
import pizza as p
from pizza import *
from pizza import make_pizza
from pizza import make_pizza as mp


#importing the entire module, it should always be
#module_name.function_name()
pizza.make_pizza(13, 'brocolli')
pizza.make_pizza(23, 'ginger', 'pineaple')

#importing specific functions,
#which should always be from module_name import function_name or,
#from module_name import fuction_0, function_1, function_2
make_pizza(45, 'brocolli')
make_pizza(61, 'ginger', 'pineaple', 'olives')

#using as to give a function an alias
#should always be from module_name import function_name as fn
mp(72, 'brocolli')
mp(8, 'ginger', 'pineaple', 'olives')

#using as to give a module an alias
#should always be import module_name as mn
p.make_pizza(13, 'brocolli')
p.make_pizza(23, 'ginger', 'pineaple')

#importing all functions in a module
#should be from module_name import *
make_pizza(45, 'brocolli')
make_pizza(61, 'ginger', 'pineaple', 'olives')