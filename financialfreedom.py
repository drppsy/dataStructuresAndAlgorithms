def automaticInvestment(m,r,y):
    sum = m*(1-pow(r,y))/(1-r)
    return sum

m = 13
r = 1.25
y = 24

s = automaticInvestment(m,r,y)
print(s)

r = pow(1.25,21)
s = 100 * r
print(s)