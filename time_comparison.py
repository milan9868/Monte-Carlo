import random
import timeit

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

def benchmark(func, iterations=1000000):
    counter_0 = 0
    counter_1 = 0
    for _ in range(iterations):
        x = random.random()
        if func(x) == 0:
            counter_0 += 1
        else:
            counter_1 += 1
    return counter_0 / iterations, counter_1 / iterations

# Benchmark foo
time_foo = timeit.timeit(lambda: benchmark(foo, iterations=1000000), number=5)
prob_0_foo, prob_1_foo = benchmark(foo)

# Benchmark foo_iter
time_foo_iter = timeit.timeit(lambda: benchmark(foo_iter, iterations=1000000), number=5)
prob_0_foo_iter, prob_1_foo_iter = benchmark(foo_iter)

print(f"foo:")
print(f"  Time: {time_foo:.4f} seconds")
print(f"  P[0] = {prob_0_foo:.4f}")
print(f"  P[1] = {prob_1_foo:.4f}")
print(f"foo_iter:")
print(f"  Time: {time_foo_iter:.4f} seconds")
print(f"  P[0] = {prob_0_foo_iter:.4f}")
print(f"  P[1] = {prob_1_foo_iter:.4f}")
print(f"Speed-up: {time_foo / time_foo_iter:.2f}x")