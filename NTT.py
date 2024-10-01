def mod_exp(base, exp, mod):

    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def ntt(a, root, mod):

    n = len(a)
    if n == 1:
        return a
    a_even = ntt(a[0::2], (root * root) % mod, mod)
    a_odd = ntt(a[1::2], (root * root) % mod, mod)
    factor = 1
    y = [0] * n
    for i in range(n // 2):
        y[i] = (a_even[i] + factor * a_odd[i]) % mod
        y[i + n // 2] = (a_even[i] - factor * a_odd[i]) % mod
        factor = (factor * root) % mod
    return y

def intt(a, root, mod):
    n = len(a)
    inv_n = mod_exp(n, mod - 2, mod)
    a = ntt(a, mod_exp(root, mod - 2, mod), mod)
    return [(x * inv_n) % mod for x in a]


mod = 17
n = 8 
primitive_root = 3 
root = mod_exp(primitive_root, (mod - 1) // n, mod)

a = [3, 2, 5, 1, 7, 8, 4, 6]

ntt_result = ntt(a, root, mod)
intt_result = intt(ntt_result, root, mod)

print("NTT Result:", ntt_result)
print("Inverse NTT Result:", intt_result)
