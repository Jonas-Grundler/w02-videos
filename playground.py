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

'Ex 9'
def miles_to_meters():
    speed_miles = input("Please input your speed in miles per hour: ")
    x = int(speed_miles)
    speed_new = round(x * (1609.34/3600),2)
    print(str(x)+" mph = "+str(speed_new)+" m/s.")

miles_to_meters()

'Ex 10'
import math

def infinite_series():
    a = 0
    for i in range(1,201):
        a = a + (1/(i**2))

    e = (math.pi**2)/6

    a = round(a,4)
    e = round(e,4)
    diff = round(e-a,4)

    print("The exact value of this infinite series is "+str(e)+".")
    print("The first 200 terms in the series give a total of "+str(a)+".")
    print("The difference between these two values is "+str(diff)+".")

infinite_series()


'Ex 11'
def string_rev_ext(x):
    return(x+":"+x[::-1])

print(string_rev_ext("abc"))

'Ex 12'
def geometric():
    res = 0
    a = 3
    r = 2
    for m in range(0,26):
        res = res + a*(r**m)
    print(res)

geometric()

'VSCode works'