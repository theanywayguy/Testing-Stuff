import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Test cases
if __name__ == "__main__":
    print(f"99 is prime: {is_prime(99)}")  # Should be False
    print(f"97 is prime: {is_prime(97)}")  # Should be True
    print(f"5 is prime: {is_prime(5)}")    # Should be True