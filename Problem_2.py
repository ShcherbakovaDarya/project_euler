fib_row = [1, 2]
even_sum = 2
print(fib_row[-1])

while fib_row[-1]<=4e6:
    sum(fib_row[-2:])
    #print(sum(fib_row[-2:]))
    fib_row.append(sum(fib_row[-2:]))
    if fib_row[-1]%2 == 0:
        even_sum += fib_row[-1]
print(fib_row)
print(even_sum)
