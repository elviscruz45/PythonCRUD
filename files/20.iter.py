def fibonacciaaa(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b
        

fib1 = fibonacciaaa(20)
fib_nums = [num for num in fib1]
...
#double_fib_nums = [num * 2 for num in fib1] # no va a funcionar
double_fib_nums = [num * 2 for num in fibonacciaaa(30)] # sí funciona

print(fib1)
print(fib_nums)
print(double_fib_nums)