

def gcd(a, b):
    assert a >= 0 and int(a) == a and b >= 0 and int(b) == b, f"Incorrect value {a} {b}"
    if b == 0:
        return a
    else:
        return gcd(b, a % b)



print(gcd(48, 18))

# gcd(18, 48 % 18) → gcd(18, 12)
# gcd(12, 18 % 12) → gcd(12, 6)
# gcd(6, 12 % 6) → gcd(6, 0)
# gcd(6, 0)