def main():
    n=int(input())
    print(fact(n))

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

main()