

#optimalizace s cache
"""cache = {0:0, 1:1}

def fibonacci(n):
    print(f"pocitam fib z {n}")
    if n in cache:
        return cache[n]
    vysledek = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = vysledek
    return vysledek

print(fibonacci(10))"""

#optimalizace se seznamem

def fib(n):
    if n<=1:
        return n
    
    a=0
    b=1
    acc=1
    while acc<n:
        c=a+b
        a=b
        b=c
        acc+=1
    return c
    