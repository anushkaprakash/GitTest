'''t=int(raw_input())
for x in range(t):
    info=[int(n) for n in raw_input().split()]
    N=info[0]
    K=info[1]
    arr=[int(a) for a in raw_input().split()]
    time=0
    for a in arr:
        if a<K:
            while a<K:
                time+=1
    print time'''
#print 'Hello World!'
'''n=int(raw_input())
arr1=[int(i) for i in raw_input().split()]
arr2=[int(i) for i in raw_input().split()]
for j in range(n):
    print arr1[j]+arr2[j], ' ',  '''
#from math import abs
test=int(raw_input())
for t in range(0,test):
    count=0
    strn=raw_input()
    n=int(strn)
    if n<9:
        print 9-n
    rem=n%9
    num=0
    if rem==0:
        print '0'
    else:
        if rem<=4:
            num=n-rem
        else:
            num=n+(9-rem)
    strnum=str(num)
    n1=[]
    num1=[]
    for i in strn:
        n1.append(int(i))
    for i in strnum:
        num1.append(int(i))
    #n1=list(n)
    print n1
    #num1=list(n)
    for i in range(0,len(n1)):
        if n1[i]!=num1[i]:
            count+=abs(n1[i]-num1[i])
    print count
    