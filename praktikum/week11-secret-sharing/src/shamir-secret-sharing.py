import random

# PRIME besar (harus lebih besar dari secret)
PRIME = 2**521 - 1

def string_to_int(text):
    return int.from_bytes(text.encode("utf-8"), "big")

def int_to_string(number):
    length = (number.bit_length() + 7) // 8
    return number.to_bytes(length, "big").decode("utf-8")

def split_secret(secret, k, n):
    secret_int = string_to_int(secret)

    coeffs = [secret_int] + [random.randrange(1, PRIME) for _ in range(k - 1)]

    def polynomial(x):
        return sum(coeffs[i] * pow(x, i, PRIME) for i in range(k)) % PRIME

    return [(i, polynomial(i)) for i in range(1, n + 1)]

def recover_secret(shares):
    def lagrange(x, points):
        total = 0
        for i, (xi, yi) in enumerate(points):
            term = yi
            for j, (xj, _) in enumerate(points):
                if i != j:
                    term *= (x - xj) * pow(xi - xj, -1, PRIME)
                    term %= PRIME
            total += term
        return total % PRIME

    secret_int = lagrange(0, shares)
    return int_to_string(secret_int)

# ============================
# MAIN
# ============================
secret = "Latihan-secret-sharing"

shares = split_secret(secret, 3, 5)
print("Shares:")
for s in shares:
    print(s)

recovered = recover_secret(shares[:3])
print("\nRecovered secret:", recovered)