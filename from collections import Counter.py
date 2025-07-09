from collections import Counter

my_list = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
my_counter = Counter(my_list)
print(my_counter)
#!===============================================
from collections import Counter

c = Counter(["ham", "eggs", "bread", "butter", "eggs", "ham", "bread", "eggs","ham","ham"])
result_ham = c["ham"]
result_eggs = c["eggs"]
result_bread = c["bread"]
print(f"Count of 'ham': {result_ham}")
print(f"Count of 'eggs': {result_eggs}")
print(f"Count of 'bread': {result_bread}")
#!=================================================
from collections import Counter

c = Counter("abracadabra additional words here")
result_five = c.most_common(5)
print(result_five)

result_ten = c.most_common(10)
print(result_ten)
#!=====================================================
from collections import Counter

my_list = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
my_counter = Counter(my_list)

print(my_counter)          # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(my_counter['apple'])  # 3
print(my_counter['grape'])  # 0

my_counter['banana'] += 1
del my_counter['orange']
my_counter['grape'] = 2

print(my_counter)          # Counter({'apple': 3, 'banana': 3, 'grape': 2})
#!=======================================================