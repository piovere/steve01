# -*- coding: utf-8 -*-


def findFactors(number):
    l = [i for i in range(1, number) if number % i == 0]
    return l


def isPerfectNumber(number):
    return sum(findFactors(number)) == number


def printPerfectNumber(number, perfect):
    print("The factors are: {0}".format(findFactors(number)))

    if perfect:
        a = "is"
    else:
        a = "is not"

    print(f"The number {number} {a} perfect")


def inputNumber():
    number = int(input('Enter Number: '))

    return number


def main():
    number = inputNumber()

    perfect = isPerfectNumber(number)

    printPerfectNumber(number, perfect)


if __name__ == "__main__":
    main()
