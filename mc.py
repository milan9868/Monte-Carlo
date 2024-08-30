import random


def foo(x):
    if x <= 0.5:
        if random.choice([0,1]) == 0:
            return 0
        return foo(x+x/2)
    else:
        if random.choice([0,1]) == 1:
            return 1
        return foo(x-x/2)

def foo_iter(x):
    while True:
        if x <= 0.5:
            if random.choice([0,1]) == 0:
                return 0
            else:
                x = x + x/2
        else:
            if random.choice([0,1]) == 1:
                return 1
            else:
                x = x - x/2


counter_0 = 0
counter_1 = 0
for i in range(1000000):
    x = random.random()
    if foo(x) == 0:
        counter_0 += 1
    else:
        counter_1 += 1

prob_0 = counter_0 / 1000000
prob_1 = counter_1 / 1000000

print(f"P[0] = {prob_0}")
print(f"P[1] {prob_1}")




