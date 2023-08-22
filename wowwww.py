# num = int(input('숫자 입력해라'))

# if 0<=num<60:
#     print('c')
# elif 60<=num<80:
#     print('b')
# elif 80<=num<=100:
#     print('a')
# else:
#     print('범위 초과')
# import random 
# num1 = random.randrange(1,100)
# num2 = random.randrange(1,100)
# num3 = random.randrange(1,100)

# a=[]
# a.insert(0,num1)
# a.insert(0,num2)
# a.insert(0,num3)
# a.sort()

# print(a[2])



# if num1<num2:
#     if num2<num3:
#         print(f"{num3}이 가장 큼")
#     else:
#         print(f"{num2}이 가장 큼")

# else:
#     if num1<num3:
#         print(f"{num3}이 가장 큼")
#     else:
#         print(f"{num1}이 가장 큼")

# import random 
# import time
# while True:
#     time.sleep(1)
#     num1 = random.randrange(1,100)
#     num2 = random.randrange(1,100)
#     num3 = random.randrange(1,100)

#     a=[]
#     a.insert(0,num1)
#     a.insert(0,num2)
#     a.insert(0,num3)
#     a.sort()
#     print(a)
#     if num1<num2:
#         if num2<num3:
            
#             print(f"{num2}이 두번째로 큼")
#             #print(a[1]==num2)
#         elif num1<num3:
#             print(f"{num3}이 두번째로 큼")
#             #print(a[1]==num3)
#         else:
#             print(f"{num1}이 두번째로 큼")
#             #print(a[1]==num1)

#     else:#num2<num1
#         if num1<num3:
#             print(f"{num1}이 두번째로 큼")
#             #print(a[1]==num1)
#         elif num2<num3:
#             print(f"{num3}이 두번째로 큼")
#             #print(a[1]==num3)
#         else:
#             print(f"{num2}이 두번째로 큼")
#             #print(a[1]==num2)





# data=[10,30,40,50,20,5,15]

# if data!=[]:
#   max = data[0]
# else:
#    print('데이터가 없습니다')
#    exit()
# for n in data:
#    if max<n:
#       max=n
# print(max)



# data=[50,40,30,10,20,5,15]
# max = -99999
# max2=-99999


# if data!=[]:
#   max = -99999
#   max2 = -99999
# else:
#    print('데이터가 없습니다')
#    exit()


# for n in data:
#    if max<=n:
     

#      if max2<=max:
#       max2=max
#      max=n
#    else:
#      if max2<=n:
#       max2=n
      
# print(max2)


# data=[50,40,30,10,20,5,15]
# process=[]
# while True:
    
#     if process ==[]:
#         process.insert(0,data)
#     len = process.__len__()-1
#     a=0
#     if process.__len__()==data.__len__():
#         break
#     while a>=len:
#         max1=process[len]
#         max2=data[a]
#         if max1<max2:
#             process.insert(0,data[a])

#         else:
#             process.insert(-1,data[a])
#         a=a+1
# print(process)
        


# for i in range(5):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# for i in range(5):
#     for j in range(5-i):  
#         print('*',end=' ')   
#     print()    



# for i in range(5):
#     for k in range(i):
#         print(' ',end=' ')
#     for j in range(5-i):   
#         print('*',end=' ')
#     print()
         
    
# for i in range(5):
#     for k in range(5-i):
#         print(' ',end=' ')
#     for j in range(i+1):   
#         print('*',end=' ')
#     print()
    

# for i in range(5):
    
#     for k in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(5):
    
#     for k in range(5-i-1):
#         print('*',end=' ')
#     print()
    
    
    

# data=[50,40,30,10,20,5,15]

# max1 = data[0]
# max2 = data[0]
# max3 = data[0]

# for n in data:
#     if max1<n:
#         max2=max1
#         max1=n
#     else:
#         max3=n
    

# max = int(input())


# n = int(input())
# if max<n:
#     max=n
# n = int(input())
# if max<n:
#     max=n
# n = int(input())
# if max<n:
#     max=n
# print(max)