import collections

filename = "d2.txt"

def d2_1():
    ans = 0
    test = {
    "red": 12,
    "green": 13,
    "blue": 14
    }
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            game, result = line.split(": ")
            id = int(game.split(" ")[1])
            sets = result.split("; ")
            for set in sets:
                failed = False
                record = collections.defaultdict(int)
                pairs = set.split(", ")
                for pair in pairs:
                    num, color = pair.split(" ")
                    record[color] = int(num)
                    if record[color] > test[color]:
                        failed = True
                        break
                if failed:
                    break
            if not failed:
                ans += id
    print(ans)

def d2_2():
    ans = 0
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            game, result = line.split(": ")
            sets = result.split("; ")
            record = collections.defaultdict(int)
            for set in sets:
                pairs = set.split(", ")
                for pair in pairs:
                    num, color = pair.split(" ")
                    if int(num) > record[color]:
                        record[color] = int(num)
            mul = 1
            for color in record:
                mul *= record[color]
            ans += mul
    print(ans)

d2_1()
d2_2()