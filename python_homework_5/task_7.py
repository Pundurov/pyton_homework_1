import json
with open('task_7.txt', 'r', encoding='utf-8') as f_obj:
    n_lines = len(f_obj.readlines())
    i = 0
    j = 0
    average = 0
    sum_average_positive = 0
    average_profit = {}
    f_obj.seek(0)
    firm_average = {}

    while i < n_lines:
        n_str = f_obj.readline()
        n_words = n_str.split()
        i += 1
        average = float(n_words[2]) - float(n_words[3])
        if average > 0:
            sum_average_positive += average
            j += 1
        firm_average[n_words[0]] = average

average_profit['average_profit'] = sum_average_positive / j
list_firm = [firm_average, average_profit]

with open('task_7.json','w') as write_f:
    json.dump(list_firm, write_f)