def factorint(n, limit=None):
    factors = {}
    divisor = 2

    while n > 1 and (limit is None or divisor <= limit):
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1

        if count > 0:
            factors[divisor] = count

        divisor += 1

    if n > 1:
        factors[n] = 1

    return factors

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)

def elliptic_curve_addition(P, Q, a, p):
    if P == 'O':
        return Q
    if Q == 'O':
        return P

    x_p, y_p = P
    x_q, y_q = Q

    if P != Q:
        m = (y_q - y_p) * extended_gcd(x_q - x_p, p)[1] % p
    else:
        m = (3 * x_p**2 + a) * extended_gcd(2 * y_p, p)[1] % p

    x_r = (m**2 - x_p - x_q) % p
    y_r = (m * (x_p - x_r) - y_p) % p

    return x_r, y_r

def elliptic_curve_scalar_multiply(k, P, a, p):
    result = 'O'
    while k > 0:
        if k % 2 == 1:
            result = elliptic_curve_addition(result, P, a, p)
        P = elliptic_curve_addition(P, P, a, p)
        k //= 2
    return result

def elliptic_curve_factorization(N, curve_params, max_iterations=1000):
    a, b, p = curve_params
    P = (0, 1)

    for iteration in range(1, max_iterations + 1):
        k = factorization_iteration(iteration, N, P, a, p)
        if k is not None and 1 < k < N:
            return k

    return None

def factorization_iteration(iteration, N, P, a, p):
    for i in range(2, iteration + 2):
        P = elliptic_curve_scalar_multiply(i, P, a, p)

    x = P[0]
    k = factorint(x, limit=2)
    if len(k) == 1 and k[list(k.keys())[0]] == 1:
        return None
    return list(k.keys())[0]

# Example usage:
N = 5959  # The integer to be factored
curve_params = (1, 1, 751)  # Elliptic curve parameters (a, b, p)

factor = elliptic_curve_factorization(N, curve_params)
print(f"A nontrivial factor of {N} is: {factor}")
