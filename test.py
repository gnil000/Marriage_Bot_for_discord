from prettytable import PrettyTable
import database

x = PrettyTable()

x.field_names = ['Супруг 1',
                 'Супруг 2', 'Дней вместе']

x.add_row(('abc', 'opoprhdfhdfhdsshqp', '02.02.2002'))
x.add_row(('ojopdgd', 'hcb hbh', '94.22.9552'))
x.add_row(('sgjo gjoopp', 'ogjg', '24.15.6326'))
print(x)


# data = [('abc', 'opoprhdfhdfhdsshqp', '02.02.2002'), ('ojopdgd', 'hcb hbh',
#   '94.22.9552'), ('sgjo gjoopp', 'ogjg', '24.15.6326')]


# data = database.getAllData(1105632912294035508)


# print(tabulate(data, headers=['Супруг 1',
#       'Супруг 2', 'Дней вместе'], tablefmt='pretty'))
