def get_matrix(dim1,dim2):
    a=[]
    for i in range(dim1):
        b=[]
        for j in range(dim2):
            b.append(int(input("Enter the element : ")))
        a.append(b); 
    return a
def sub_matrix(arr1,arr2):
    for i in range(dim1):
        for j in range(dim2):
            arr1[i][j]-=arr2[i][j]
    return arr1
dim1=eval(input("Enter the number of rows : "))
dim2=eval(input("Enter the number of columns : "))
arr1=get_matrix(dim1,dim2)
arr2=get_matrix(dim1,dim2)
val=sub_matrix(arr1,arr2)
for i in val:
        print(i)