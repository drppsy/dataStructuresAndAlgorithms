#定投计算公式，m是每年定投金额，r是年化利率，y是连续投资年数，i是初始投资资本金
#递归调用的本质就是自己调用自己，再把第一个条件，最开始的自己返回出去，作为最初的条件
def automaticInvestment(m,r,y,i=0):
    i_sum = i*(1-pow(r,y))/(1-r)
    if y > 1:
        sum = m*(1-pow(r,y))/(1-r) + automaticInvestment(m,r,y-1)
        y -= 1
    else:
        return m
    return i_sum + sum

#每年投资20w，年化25%，定投6年，初始投资金为42w，获得收益约为1118w
m = 20
r = 1.25
y = 6
s1 = automaticInvestment(m,r,y,42)
print(s1)


#每年投资20w，年化25%，定投10年，初始投资金为42w，获得收益约为3920w
m = 20
r = 1.25
y = 10
s2 = automaticInvestment(m,r,y,42)
print(s2)

#每年投资20w，年化25%，定投15年，初始投资金为42w，获得收益约为9760w
m = 20
r = 1.25
y = 15
s3 = automaticInvestment(m,r,y)
print(s3)


#每年投资20w，年化25%，定投20年，初始投资金为42w，获得收益约为3.2亿元
m = 20
r = 1.25
y = 20
s4 = automaticInvestment(m,r,y)
print(s4)


'''
当前初始资金42w，工作6年，每年投资20w，年化25%，定投6年，获得收益约1118万
1118万每年25%，约279万，279万每年支出100万，还有179万可用来定投。1118万继续投资20年（不考虑继续增加了），会有9.7亿元，投资30年，会有39.2亿元
'''
