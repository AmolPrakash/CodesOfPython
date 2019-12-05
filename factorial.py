
def factorial(n):
    if n == 0:
        return 1
    else:
        #count += 1
        #print (count)
        return n * factorial(n-1)

def main():
    count = 0
    print(factorial(992))

if __name__ == "__main__":
    main()
