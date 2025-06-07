class numbers:

    def __init__(self):
        self.value = int(input("enter value: "))

    def chkprime(self):
        factor=1
        for i in range(1,self.value+1):
            if self.value%i==0:
                factor=factor*i
        if factor==self.value:
            return True
        else:
            return False

    def factors(self):
        result=[]
        for i in range(1,self.value):
            if (self.value%i==0):
                result.append(i)
        print("factors are:",result)

    def sumfactors(self):
        result=0
        for i in range(1,self.value):
            if (self.value%i==0):
                result=result+i
        print("addition of factors is:",result)

    def chkperfect(self):
        result=0
        for i in range(1,self.value):
            if (self.value%i==0):
                result=result+i
        return self.value == result
    
def main():
    obj1 = numbers()
    ret1=obj1.chkprime()
    print("prime: ",ret1)
    ret2=obj1.chkperfect()
    print("perfect: ",ret2)
    obj1.factors()
    obj1.sumfactors()

if __name__ == "__main__":
    main()