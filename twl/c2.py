#map

list_x = [1,2,3,4,5,6,7,8]

def square(x):
    return  x * x

#for x in list_x:
#    square(x)

r = map(square,list_x)
print(r)
print(list(r))
print()