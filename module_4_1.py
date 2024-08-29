from fake_math import divide as divide_f
from true_math import divide as divide_t

result1 = divide_f(69, 3)
result2 = divide_f(3, 0)
result3 = divide_t(49, 7)
result4 = divide_t(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
