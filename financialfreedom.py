#定投计算公式，m是每年定投金额，r是年化利率，y是连续投资年数
def automaticInvestment(m,r,y):
    sum = m*(1-pow(r,y))/(1-r)
    return sum

#每年投资13w，年化25%，定投24年，获得收益超过1.09亿
m = 13
r = 1.25
y = 24
s1 = automaticInvestment(m,r,y)
assert s1 > 10959

#每年投资20w，年化25%，定投22年，获得收益小于1.09亿
m = 20
r = 1.25
y = 22
s2 = automaticInvestment(m,r,y)
assert  s2 < 10790


#每年投资20w，年化25%，定投24年，获得收益超过1.68亿，小于1.7亿
m = 20
r = 1.25
y = 24
s3 = automaticInvestment(m,r,y)
assert 16800 < s3 < 17000


'''
工作10年，每年投资13w，年化25%，定投10年，获得收益约432万
432万每年25%，约108万，108万每年支出50万，还有50万可用来定投。432万继续投资20年（不考虑继续增加了），会有3.75亿元，投资30年，会有35亿元
'''
m = 13
r = 1.25
y = 10
s4 = automaticInvestment(m,r,y)
print(s4)

s5 = s4*pow(1.25,20)
print(s5)
