def gen_fact(number):
    cur = 1
    for i in range(1, number + 1):
        cur *= i
        yield cur


n = 10
for el in gen_fact(n):
    print(el)
