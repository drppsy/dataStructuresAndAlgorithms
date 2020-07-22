def kw_dict(v,*args,**kwargs):
    return v,args,kwargs

mydict = kw_dict('21',12,34,a=1,b=2,c=3,d=4,e=5)
print(mydict)