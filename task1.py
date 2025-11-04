def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result
    return fibonacci


fib = caching_fibonacci()

print(fib(10))
print(fib(15))
