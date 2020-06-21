n, k = map(int, input().split())

def amount_of_combinations(a, b):
    if b == 0:
        return 1
    elif b > a:
        return 0
    else:
        return amount_of_combinations(a - 1, b) + amount_of_combinations(a - 1, b - 1)

print(amount_of_combinations(n, k))