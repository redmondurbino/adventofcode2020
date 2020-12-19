#!/usr/bin/env python 


def part1():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    result = 0
    for line in Lines:
        splits = line.split()
        minmax = splits[0]
        min = int (minmax.split('-')[0])
        max = int (minmax.split('-')[1])
        letter = splits[1][0]
        password = splits[2]
        numletters = password.count(letter)
        if (min <= numletters and numletters <= max):
            result += 1
    print result
    return

# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter.

def part2():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    result = 0
    for line in Lines:
        splits = line.split()
        minmax = splits[0]
        firstIndex = int (minmax.split('-')[0]) - 1
        secondIndex = int (minmax.split('-')[1]) - 1
        letter = splits[1][0]
        password = splits[2]
        good_characters = 0
        if password[firstIndex] == letter:
            good_characters += 1
        if password[secondIndex] == letter:
            good_characters += 1
        if (good_characters == 1):
            result +=1
    
    print result
    return

if __name__ == '__main__':
    part2()