class Solutions:

    def myPow1(self,x,n):
        return pow(x,n)

    def myPow2(self,x,n):
        if not n:
            return 1
        if n%2 :
            return x*self.myPow2(x,n-1)
        if n < 0:
            return 1/ self.myPow2(x,-n)
        return self.myPow2(x*x,n/2)