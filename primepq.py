import sys
import math

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(n):
    """Find two prime factors p and q such that n = p * q."""
    for i in range(2, n):
        if n % i == 0:  # Check divisibility
            p, q = i, n // i
            if is_prime(p) and is_prime(q):
                return p, q
    return None, None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 factorize.py <number>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n <= 0:
            raise ValueError("Number must be positive.")
        
        p, q = prime_factors(n)
        if p and q:
            print(f"Prime factors of {n} are p = {p}, q = {q}")
        else:
            print(f"No prime factors found for {n}.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
