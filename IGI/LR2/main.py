import square
import circle
import os 

env = float(os.environ.get('VALUE_TO_PUT', 0))

print("parametr: ", env)
print('square area: ', square.area(env))
print('square perimeter: ', square.perimeter(env))
print('circle are: ', circle.area(env))
print('circle perimeter:', circle.perimeter(env))

