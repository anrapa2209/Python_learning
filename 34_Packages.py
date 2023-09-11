#package is a container for multiple modules
#either you can directly create a new Python package (which comes with a default __init__ python file,
#or you can create a directory and add a new '__init__' python file into it; to form a package

#import ecommerce.shipping
#ecommerce.shipping.calc_shipping()
#instead of typing import shipping, we have to prefix it with the name of its package
#however, with this approach, we need to call one of the functions everytime
#so intead,

from ecommerce.shipping import calc_shipping

calc_shipping()
calc_shipping()
calc_shipping()
#we can call this function multiple times in the module, so our code becomes a little bit shorter
# what if we want to use multiple functions in this shipping module?
#either ~
#from ecommerce.shipping import calc_shipping, calc_tax

#or ~
#import the entire module and access all the functions and classes in that module
print('')
from ecommerce import shipping

shipping.calc_shipping()
