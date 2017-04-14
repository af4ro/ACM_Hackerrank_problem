inputs = []
pr = []

def primes(n):
    for i in range(2,n):
        pr.append(i)
    for


def main():
    max = 0
    while True:
        temp = int(input())
        if max <= temp:
            max = temp
        if temp == 0:
            break
        inputs.append(temp)
    pr = primes(max)

main()