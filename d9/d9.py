filename = "d9.txt"

def d9_1():
    ans = 0
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            value = 0
            prev = list(map(int, line.split(" ")))
            while not zero_only(prev):
                value += prev[-1]
                curr = []
                for i in range(1, len(prev)):
                    curr.append(prev[i] - prev[i - 1])
                prev = curr
            ans += value
    print(ans)

def zero_only(list):
    for item in list:
        if item != 0:
            return False
    return True

def d9_2():
    ans = 0
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            firsts = []
            prev = list(map(int, line.split(" ")))
            while not zero_only(prev):
                firsts.append(prev[0])
                curr = []
                for i in range(1, len(prev)):
                    curr.append(prev[i] - prev[i - 1])
                prev = curr
            temp = 0
            for i in range(len(firsts) - 1, -1, -1):
                temp = firsts[i] - temp
            ans += temp
    print(ans)

d9_1()
d9_2()