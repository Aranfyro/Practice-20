# Дополнительное практическое задание по модулю: "Подробнее о функциях."

def calculate_structure_sum(a):
    sum_ = 0
    def recursive_(b):
        nonlocal sum_
        if isinstance(b, (int, float)):
            sum_ += b
        elif isinstance(b, str):
            sum_ += len(b)
        elif isinstance(b, (list, tuple, set)):
            for i in b:
                recursive_(i)
        elif isinstance(b, dict):
            for key, value in b.items():
                recursive_(key)
                recursive_(value)

    recursive_(a)
    return sum_

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


