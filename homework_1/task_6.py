km_day_1 = int(input("Введите: сколько километров спортсмен пробежал за первый день: "))
km_day_n = int(input("Какого результата спортсмен должен достичь?: "))
n_day = 1

while km_day_1 < km_day_n:
    km_day_1 *= 1.1
    n_day +=1

print(f"на {n_day}-й день спортсмен достиг результата — не менее {km_day_n} км")
