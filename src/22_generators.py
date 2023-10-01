def gen_range(stop, start = 1, step = 1):
    num = start
    while num <= stop:
        yield num
        num += step

print(gen_range(10))
generator = gen_range(10)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# converting generator to lists
generator = gen_range(10)
print(list(generator))

def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b , a + b
        yield a

fib = gen_fib()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
# list(fib) sería infinito

fib = gen_fib()
print([next(fib) for _ in range(50)])
