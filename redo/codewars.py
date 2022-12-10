def repeat_str(repeat, string):
    s = ''
    n = 1
    while n <= 6:
        s = s + string
        n= n+1
    return print(s)

repeat_str(4, 'hello')