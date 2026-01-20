import random

# Parameter
p = 2089            # bilangan prima (harus > secret)
secret = 1234       # rahasia (a0)
k = 3               # threshold
n = 5               # jumlah share

# Bangun polinomial f(x) = a0 + a1*x + a2*x^2 mod p
coefficients = [secret] + [random.randint(1, p-1) for _ in range(k-1)]

def polynomial(x, coeffs, p):
    result = 0
    for i in range(len(coeffs)):
        result = (result + coeffs[i] * pow(x, i)) % p
    return result

# Membuat shares (x, f(x))
shares = []
for x in range(1, n+1):
    y = polynomial(x, coefficients, p)
    shares.append((x, y))

print("Shares:")
for s in shares:
    print(s)

# Lagrange Interpolation untuk rekonstruksi secret
def lagrange_interpolation(x, shares, p):
    total = 0
    for i, (xi, yi) in enumerate(shares):
        prod = yi
        for j, (xj, _) in enumerate(shares):
            if i != j:
                prod *= (x - xj) * pow(xi - xj, -1, p)
                prod %= p
        total += prod
    return total % p

# Rekonstruksi secret menggunakan k shares
recovered_secret = lagrange_interpolation(0, shares[:k], p)
print("\nRecovered Secret:", recovered_secret) 