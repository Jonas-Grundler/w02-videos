'Assessed Quiz 1'

'Ex 1'
def my_function(x):
    value = int(x)
    a = value%3
    b = value%5
    c = value%7
    l = [a,b,c]
    return l

my_function(165.1)

'Ex 2'
def temp_convert(deg_far):
    temp_new = ((5*(deg_far-32))/9)
    res = round(temp_new,2)
    print(res)

temp_convert(32)

'Ex 3'
def every_other_num(x1,x2):
    my_list = []
    for i in range(x1,x2+1,2):
        my_list.append(i)
    return my_list

print(every_other_num(2,4))

'Ex 4'
def time_converter(milliseconds):

    years = floor(milliseconds/(365*30*24*60*60*1000))
    remainder = milliseconds%(365*30*24*60*60*1000)
    months = remainder%(30*24*60*60*1000)
    remainder = remainder - months* (30*24*60*60*1000)
    days = remainder%(24*60*60*1000)
    remainder = remainder - days* (24*60*60*1000)
    hours = remainder%(60*60*1000)
    remainder = remainder - hours* (60*60*1000)
    minutes = remainder%(60*1000)
    remainder = remainder - minutes* (60*1000)
    seconds = remainder%(1000)
    remainder = remainder - seconds* (1000)
    milliseconds = remainder

    # Print the result
    print(f'{years} years,')
    print(f'{months} months,')
    print(f'{days} days,')
    print(f'{hours} hours,')
    print(f'{mins} minutes,')
    print(f'{secs} seconds,')
    print(f'and {ms} milliseconds.')

time_converter(1000000000)


7%2
