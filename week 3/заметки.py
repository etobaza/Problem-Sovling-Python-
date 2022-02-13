"""Parameter is a variable listed inside the parentheses in the function definition"""

"""
def my_function(fname):
   print(fname + " amogus")
my_function("Sus")
"""

"""
def my_function(*names):
    print(len(names))
my_function("a", "b", "c")
"""

"""
def auth(login, password):
    if login == "l1" and password == "p1": 
        print("ok")
    else:
        print("denied")

auth(password = "p1", login = "l1")
auth(login = "l1", password = "p1")
"""


#if number of keyword arguments is unknown, add a double ** before parameter name
"""
def my_func(**kid):
    print("His name" + kid["lname"])

my_func(fname = "Tobias", lname = "Dray")
"""

# A lambda function - anonymous function
# lambda arg : expression
# Лямбда удобно в другой функции (high-order function)
"""
x = lambda a : a+10
print(x(5))
"""

"""
def myfunc(n):
    return labmda a : a*n

mydoubler = myfunc(2)

print(mydoubler(11))
"""

#OOP

