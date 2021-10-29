import re

with open('task_6.txt', 'r', encoding='utf-8') as f_obj:
    n_lines = len(f_obj.readlines())
    i = 0
    j = 0
    f_obj.seek(0)
    n_tasks = {}
    while i < n_lines:
        n_str = f_obj.readline()
        nums_list = re.findall(r'\d+', n_str)
        sum_num = 0
        for j in nums_list:
            sum_num += float(j)
        list_str = n_str.split()
        n_tasks[list_str[0]] = (sum_num)
        i += 1

for key, value in n_tasks.items():
    print(f'{key} - {value}')