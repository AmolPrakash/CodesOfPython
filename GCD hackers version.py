def _gcd(a, b):
    """Euclid's algorithm for greatest common
divisor (hacker's version)."""
    (a, b) = (max(a, b), min(a, b))
    while b > 0:
        (a, b) = (b, a % b)
    return a

def main():
    a= int(input("A: "))
    b= int (input ("B: "))
    print( _gcd(a,b))

if __name__ == "__main__":
    main()
    
