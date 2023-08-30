

start_col=0
end_col=int(input('행'))
# 
start_row=0
end_row=int(input('열'))
# int(input('열'))
n1=end_col+1
n2=end_row+1
cnt=0

map=[[0 for i in range(end_col)]for j in range(end_row)]

end_col-=1
end_row-=1
while cnt<=(n1*n2):

    for i in range(start_col,end_col+1):
        cnt +=1
        map[start_row][i]=cnt
    start_row+=1
    
    

    for i in range (start_row,end_row+1):
        cnt +=1
        map[i][end_col]=cnt
    end_col-=1
    
    
    

    for i in range (end_col,start_col-1,-1):
        cnt +=1
        map[end_row][i]=cnt
    end_row-=1


    for i in range (end_row,start_row-1,-1):
        cnt +=1
        map[i][start_col]=cnt
    start_col+=1
    
    if cnt>=(n1*n2):
        break

   


   


for i in range(n2-1):
    print(map[i])
