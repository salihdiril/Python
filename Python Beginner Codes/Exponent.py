print(2**7)

def exponent(base, pow):
    return base**pow

def raise_to_power(base, pow):
    result = 1
    for i in range(pow):
        result *= base
    return result

print(exponent(2,7))
print(raise_to_power(2,7))