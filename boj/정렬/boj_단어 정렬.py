


def fact_recur(n):
    if n <= 1:
        return 1
    return n * fact_recur(n-1)

print(fact_recur(5))



