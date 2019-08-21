def fib(n):
    a,b = 0,1
    result = []
    while a<n:
        result.append(b)
        a, b = b, a+b
    return result
