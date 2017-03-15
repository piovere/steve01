# -*- coding: utf-8 -*-


def findFactors(number):
    l = []
    for i in range(1, number):
        if number % i == 0:
            l.append(i)

    return l


def isPerfectNumber(number):
    return sum(findFactors(number)) == number


def printPerfectNumber(number, perfect):
    print("The factors are: {0}".format(findFactors(number)))

    if perfect:
        a = "is"
    else:
        a = "is not"

    print("The number {0} {1} perfect".format(number, a))


if __name__ == "__main__":
    number = int(input('Enter Number: '))

    perfect = isPerfectNumber(number)

    printPerfectNumber(number, perfect)
