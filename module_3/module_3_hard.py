data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def sum_len(d_s):
    sum = 0
    for elem in d_s:
        if isinstance(elem, (tuple, list, set)):
            sum += sum_len(elem)
        elif isinstance(elem, dict):
            sum += sum_len(elem.keys())
            sum += sum_len(elem.values())
        elif isinstance(elem, str):
            sum += len(elem)
        else:
            sum += elem
    return sum

print(sum_len(data_structure))
