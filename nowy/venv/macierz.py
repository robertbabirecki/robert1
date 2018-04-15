m=[[1,5,0],[9,1,0],[3,2,1]]

for i in range(3):
    print('\n')
    for j in range(3):
        m[j][i]=j+i+2
        print (m[j][i], end='          ')

