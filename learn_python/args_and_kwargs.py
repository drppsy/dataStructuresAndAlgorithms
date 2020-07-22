'''
精品文章
https://zhuanlan.zhihu.com/p/70649428
'''


def kw_dict(v,*args,**kwargs):
    # 可变参数*args在传入函数后，被封装成一个tuple来进行使用
    # 可变参数**kwargs，被封装成dict字典类型来进行使用
    return v,args,kwargs

mydict = kw_dict('21',12,34,a=1,b=2,c=3,d=4,e=5)
print(mydict)


def print_numbers(*args):
    print(type(args))  # tuple
    for n in args:
        print(type(n))   # int或其他类型，取决于tutle里是啥类型

l = [1, 2, 3, 4]
print(*l)
print_numbers(*l)  # *l，等价于 print_numbers(1, 2, 3, 4)
print_numbers(l)   # 将 l 作为一个整体传入，这样函数接受到的其实只有一个参数，且参数类型为 list



def register(name,email,**kwargs):
    print("name:%s,email:%s,other:%s" %(name,email,kwargs))

register('飞塔','feta6@qq.com')
register('年糕','niangao@qq.com',age='1岁')


def test1(a, b, c=0, *args, **kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kwargs)

def test2(a, b, c=0, *, d, **kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kwargs)

# 定义一个元组和字典用作参数传入
args = (1, 2, 3)
kw = {'d':'99','x': '#'}

test1(*args, **kw)
test2(*args,**kw)
