from cmath import exp
from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

#print(expenses.read_expenses("data/spending_data.csv"))

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)

print(spending_counter)

top5 = spending_counter.most_common(5) 

print("Top 5 Categories: ")      
print(top5)

categories, count = zip(*top5)

print(categories, count)

fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()




# local testing module 
# pytest -k module2
# to run module
# python -m budget.FrequentExpenses
    
