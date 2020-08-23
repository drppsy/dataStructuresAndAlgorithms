'''
魔法函数
    (1)内置类型class中，以双下划线开头、双下划线结尾的函数
    (2)使用python内定义的魔法函数，不要使用自定义的魔法函数
'''

class Company:

    def __init__(self,employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(['feta','niangao','zhuzhu'])

# (3)for循环其实拿到的是一个迭代器，如果有__iter__就拿__iter__，没有就去找__getitem__，再没有可迭代对象，就报错
for em in company.employee:
    print(em)

for em in company:
    print(em)

company1 = company[:2]
print(company1)
print(len(company1))
print(len(company))