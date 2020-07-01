def automaticInvestment(m,r,y):
    sum = m*(1-pow(r,y))/(1-r)
    return sum

m = 15
r = 1.25
y = 23

s = automaticInvestment(m,r,y)
print(s)