# for i in range(4):
#     for j in range(4-i):
#         print("*",end= ' ')
#     for k in range(2*i):
#         print(end= ' ')
#     for j in range(4-i):
#         print(end= ' ')
#     for l in range(1+i):
#         print("*",end= ' ')





#     print()






# for i in range(5):
#     for j in range(5-i):
#         print("*",end= ' ')
#     for k in range(2*i):
#         print(end= ' ')
#     for j in range(i):
#         print(' ',end= ' ')
#     for l in range(5-i):
#         print("*",end= ' ')



#     print()





# for i in range(5):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(4):
#     for j in range(4-i):
#         print('*',end=' ')
#     print()




# for i in range(5):
#     for j in range(4-i):
#         print(end= ' ')
#     for l in range(1+i):
#         print("*",end= ' ')


# for i in range(5):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for k in range(1+2*i):
#         print('*',end=' ')
#     print()
# for i in range(5):
#     for j in range(i+2):
#         print(' ',end=' ')
#     for k in range(9-2*(i+1)):
#         print('*',end=' ')
#     print()
\



# for i in range(10):
#     print(' ',end='')
# print('*')
# for i in range(4):
#     for k in range(4-i):
#         print(' ',end=' ')
#     print('*',end=' ')
    
#     for b in range(i*2+1):
#         print(' ',end=' ')
#     print('*',end='')
#     print()
# for i in range(3):
#     for k in range(i+2):
#         print(' ',end=' ')
#     print('*',end=' ')

#     for b in range(5-i*2):
#         print(' ',end=' ')
#     print('*',end='')
#     print()
# for i in range(10):
#     print(' ',end='')
# print('*')

# a= [[ 1, 2, 3, 4, 5],
#     [ 6, 7, 8, 9,10],
#     [11,12,13,14,15]]

# row = int(input('a'))
# col = int(input('b'))
# a =[[i for i in range(col)] for j in range(row)]

# for i in range(row):
#     for j in range(col):
#             if i%2==0:
#                 a[i][j]=(j+1)+i*col
#             else:
#                 a[i][-j-1]=(j+1)+i*col
                

# for i in range(row):
#     print(a[i])

# row = int(input('a'))
# col = int(input('b'))

# a =[[0 for i in range(row)] for j in range(col)]


# for i in range(row):
#     for j in range(col):
#                 a[i][j]=(j+1)+i*col
             

# for i in range(row):
#     print(a[i])




# row = int(input('a'))
# col = int(input('b'))
# a =[[i for i in range(col)] for j in range(row)]

# for i in range(col):
#     for j in range(row):
#             if i%2==0:
#                 a[j][i]=(j+1)+i*row
#             else:
#                 a[-j-1][i]=(j+1)+i*row

# for i in range(row):
#     print(a[i])

# row = int(input('a'))#세로
# col = int(input('b'))#가로

row=5
col=5
a =[[0 for i in range(col)] for j in range(row)]

cnt = 0

for j in range(5):
    cnt+=1
    a[0][j]=cnt
for i in range(1,5):
    cnt+=1
    a[i][j]=cnt
for j in range(3,-1,-1):
    cnt+=1
    a[i][j]=cnt

for i in range(3,0,-1):
    cnt+=1
    a[i][j]=cnt
for j in range(1,4,1):
    cnt+=1
    a[i][j]=cnt
for i in range(2,4,1):
    cnt+=1
    a[i][j]=cnt


for i in range(row):
    print(a[i])