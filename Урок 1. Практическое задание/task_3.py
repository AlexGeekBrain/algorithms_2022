"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


name_company = {
    'microsoft': 100000,
    'apple': 50000,
    'google': 90000,
    'yandex': 40000,
    'mail_group': 30000
}

# O(n) - линейная
def sorted_1(name_company):
    lst = {}                                               # O(n)
    list_d = dict(name_company)                            # O(n)
    for i in range(3):                                     # O(1)
        maximum = max(list_d.items(), key=lambda i: i[1])  # O(n)
        del list_d[maximum[0]]                             # O(n)
        lst[maximum[0]] = maximum[1]                       # O(n)
    print(lst)                                             # O(1)


sorted_1(name_company)


# O(n^2) - квадратичная
def sorted_2(name_company):
    lst = list(name_company.items())         # O(n)
    for i in range(len(lst)):                # O(n)
        val = i                              # +
        for n in range(i + 1, len(lst)):     # O(n) = O(n^2)
            if lst[n][1] > lst[val][1]:      # O(1)
                val = n                      # O(1)
        lst[i], lst[val] = lst[val], lst[i]  # O(1)
    print(lst[0:3])                          # O(1)


sorted_2(name_company)

"""
Первый вариант лучше, так как имеет минимальную вычислительную сложность
"""