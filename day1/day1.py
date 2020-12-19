#!/usr/bin/env python 


def part1():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    numbers = []
    for line in Lines:
        numbers.append (int(line))
    for i in range (len(numbers)):
        for j in range ( i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum == 2020:
                product = numbers[i] * numbers[j]
                print product
                return
        
def main():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    numbers = []
    for line in Lines:
        numbers.append (int(line))
    for i in range (len(numbers)):
        for j in range ( i+1, len(numbers)):
            for k in range ( j+1, len(numbers)):
                sum = numbers[i] + numbers[j] + numbers[k]
                if sum == 2020:
                    product = numbers[i] * numbers[j] * numbers[k]
                    print product
                    return    

if __name__ == '__main__':
    main()