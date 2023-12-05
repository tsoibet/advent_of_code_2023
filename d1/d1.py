filename = "d1.txt"

def d1_1():
    ans = 0
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            first = ""
            last = ""
            for i in range(len(line)):
                if line[i].isdigit():
                    first = line[i]
                    break
            for j in range(len(line) - 1, -1, -1):
                if line[j].isdigit():
                    last = line[j]
                    break
            ans += int(first + last)
    print(ans)

def d1_2():
    ans = 0
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:

            first_index = len(line)
            first_digit = 0
            for key in numbers:
                temp = line.find(key)
                if temp > -1 and temp < first_index:
                    first_index = temp
                    first_digit = numbers[key]
            if int(first_digit) > 0:
                line = line[:first_index] + line[first_index:].replace(line[first_index], first_digit, 1)

            last_index = -1
            last_digit = 0
            for key in numbers:
                temp = line.rfind(key)
                if temp > last_index:
                    last_index = temp
                    last_digit = numbers[key]
            if int(last_digit) > 0:
                line = line[:last_index] + line[last_index:].replace(line[last_index], last_digit, 1)

            first = ""
            last = ""
            for i in range(len(line)):
                if line[i].isdigit():
                    first = line[i]
                    break
                for key in numbers:
                    if key in line[i: i+5]:
                        first = numbers[key]
                        break
            for j in range(len(line) - 1, -1, -1):
                if line[j].isdigit():
                    last = line[j]
                    break
            ans += int(first + last)
    print(ans)

d1_2()