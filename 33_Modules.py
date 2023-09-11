import converters


print(converters.kg_to_lbs(55))

import converters
from converters import kg_to_lbs
#instead of importing the entire module, we can also import specific functions from that module

print(kg_to_lbs(100))           #i.e., no need to prefix the module name
#instead of writing all functions in 1 file, we break our code across multiple files
