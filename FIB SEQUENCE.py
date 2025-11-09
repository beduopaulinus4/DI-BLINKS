def fibonacci_loop(n: int):
    """ Return the first n fibonacci numbers (starting with 0)"""
    if n <= 0:  # type: ignore
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq
#call the function to print the first 10 fibonanci numbers
print(fibonacci_loop(20))
