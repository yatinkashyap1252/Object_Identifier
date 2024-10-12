# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# def sum(c,d):
#     return c+d
# def min(a,b):
#     pass
# def max(c,d):
#     if c>d:
#         return "A is greater"
#     else:
#         return "B is greater"
# func=sum(a,b)
# ans=a+b
# print("The ans is from function called:",func)
# print("The greatest is from function called:",max(a,b))
# print("The summation of two number is:",ans)
# p=int(input("Enter the principle amount:"))
# r=int(input("Enter the rate of interest:"))
# n=int(input("Enter the time interval:"))
# i=(p*r*n)/100
# t=i+p
# print("Interest will be:",i,"of time interval:",n)
# print("the total amountwill be:",t)
# n=int(input("Enter the number:"))
# ans=1
# for i in range (1,n+1):
#     ans=ans*i
# print(ans)
# def compound_interest(principle,rate,time):
#     a=principle*(pow((1+rate/100),time))
#     i=a-principle
#     print(i,"and",a)
# p=int(input("Enter the principle amount:"))
# r=float(input("Enter the rate of interest:"))
# n=int(input("Enter the time interval(in years):"))
# compound_interest(p,r,n)
# n=int(input("Enter the number:"))
# temp=n
# ans=0
# while temp>0:
#     a=int(temp%10)
#     # print(a)
#     ans=ans+(a*a*a)
#     temp=int(temp/10)
# # print(ans)
# def armstrong(a,b):
#     if a-b==0:
#         print("it is")
#     else:
#         print("it is not")
# armstrong(n,ans)
# a=int(input("Enter the starting number:"))
# b=int(input("Enter the ending number:"))
# for i in range (a,b+1):
#     count=0
#     # print("i is",i)
#     for j in range(2,int((i/2)+1)):
#         # print("j is",j)
#         if i%j==0:
#             count=count+1
#     if(count==0):
#         print(f"it is a prime number {i}")
#     else:
#         print(f"it is not {i}")
# n=int(input("Enter the terms:"))
# a=0
# b=1
# if n==1:
#     print("the terms are:",a)
# elif n==2:
#     print("the terms are :",a,b)
# elif n<0:
#     print("the serires is not possible")
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         print(c)
#         a=b
#         b=c
# n=input("Enter the character:")
# print(ord(n))
# a=int(input("Enter the starting number:"))
# b=int(input("Enter the ending number:"))
# ans=0
# for i in range(a,b+1):
#     # ans=ans+(i*i)
#     ans=ans+(i*i*i)
# print(ans)
# a=[]
# for i in range (0,5):
#     a.append(input("Enter the number:"))
# for i in range (0,5):
#     print(a[i],end=",")
# a=[3,7,5,2,3,77,55,44,9,1]
# n=len(a)
# max=a[0]
# for i in range(1,n):
#     if a[i]>max:
#         max=a[i]
# print(max)
