def fibonacci(n: int) -> int:
    cache = {0: 0, 1: 1}

    def inner(n) -> int:
        if n in cache:
            return cache[n]
        cache[n] = inner(n - 1) + inner(n - 2)
        return cache[n]

    return inner(n)
