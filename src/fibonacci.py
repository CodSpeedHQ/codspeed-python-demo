def fibonacci(n: int) -> int:
    calls = 0

    def inner(n: int) -> int:
        nonlocal calls
        calls += 1
        if n in [0, 1]:
            return n
        return inner(n - 1) + inner(n - 2)

    res = inner(n)
    print(f"fibonacci({n}) -> calls={calls}")
    return res
