def factorial(n):
    num = 1
    for i in range(1,n+1):
        num = num * i
    return num 

def binom(n,k):
    if n<k:
        print("not valid")
        return None
    return factorial(n)/(factorial(k)*factorial(n-k))

def main():
    n = int (input ("enter n : "))
    k = int (input (" enter k : "))
    print(binom(n,k))

if __name__ == "__main__":
    main()
