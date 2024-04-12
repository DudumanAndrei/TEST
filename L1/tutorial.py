#
# Python tutorial file.

from circle import Circle


print("Hello world!")

a = True
b = False

print(a and b)
print(a or b)
print(not a)

c = 20 
d = -3.5
e = 2 + 5j

print(20 / 3)
print(20 // 3)
print(20%3)

print(2**10)

list1 = [True, -20, "hello", 8.5]
tuplu1 = (20, -8912, "a")

#print(list1[2])
#print(list1[0:2]) #ne oprim la capat-1
print(list1[::-1])
#print(list1[-1])

print(list1)
print(tuplu1)

print(-20 in list1)
print(len(list1))

list1[2] = 8+9j
print(list1)

#tuplu1[2] = 8+9j don't allow
#print(tuplu1)

for x in list1:
    print(x)
    
#for x in range(5):
#    print(x)
    
for x in range(len(list1)):
    print(list1[x])
    
v = "hello world"
n = 'afeafjsa'
m = '''
    adnfna
    adasfda    
'''

print("hello" in v)

if len(v) > 3:
    print("string is long")
elif len(v) == 2:
    print(3+5)
else:
    print(10)
    
v=(403, 100)

match v:
    case (404, 0):
        print("page not found")
    case (403, x):
        print(f"Forbidden, result {x}")
    case _:
        print("Unknown error")
      
a = 5    
while a>0:
    print(a)
    a-=1
    
#default parameters should be in the end of the list
def add(a:int=0.0, b:int=0.0) -> int:
    '''
    Adds two numbers
    '''
    return a + b

print(add())



circle1 = Circle(1.0)
print(circle1.area())