'Ex 1'
def stringprint(string_argument):
    print(string_argument)


stringprint("How are you?")


'Ex 2'
def calculation_number1():
    answer = (0.87 + 3.14 + 0.63 + 297)**(3/2)
    return(answer)

print(calculation_number1())


'Ex 3'
def y_calculation():
    x = 0.45
    y = x**3 + 3*(x**2) + 2*x + 1
    return(y)

print(y_calculation())


'Ex 4'
def hello_user():
    username = input("What is your name? ")
    print("Hello " + username + "!")

hello_user()

'Ex 5'
def easy_sum():
    total = 0
    for i in range(1,11):
        total = total + (i+1)
    print(total)

easy_sum()

'Ex 6'
import math

def circle_properties(r):
    num_pi = math.pi
    d = 2*r
    c = round(2*r*num_pi,2)
    a = round((r**2)*num_pi,2)
    print("The diameter of the circle is "+str(d)+".")
    print("The circumference of the circle is "+str(c)+".")
    print("The area of the circle is "+str(a)+".")

circle_properties(5)

'Ex 7'
def fibonacci():
    fib = [0]*20
    fib[0] = 0
    fib[1] = 1
    for n in range(2,20):
        fib[n] = fib[n-1] + fib[n-2]
    print(fib)

fibonacci()


'Ex 8'
def floats(x,y,z):
    l = [x,y,z]
    a,b,c = (sorted(l))
    print(str(a)+', '+str(b)+', '+str(c))

floats(3.2,7.0,2.4)
