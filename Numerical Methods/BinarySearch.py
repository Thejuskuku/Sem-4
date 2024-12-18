def BinarySearch(arr,num,lb,ub):
    if(lb<=ub):
        mid=(lb+ub)//2
        if(arr[mid]==num):
            print(f"Element found at : {mid}")
        elif(arr[mid]<num):
            return(BinarySearch(arr,num,mid+1,ub))
        else:
            return(BinarySearch(arr,num,lb,mid-1))
    else:
        print("Element not found")

a=eval(input("Enter the number of elements : "))
arr=[]
for i in range(a):
    arr.append(int(input("Enter value : ")))
num=eval(input("Enter the element to search for : "))
BinarySearch(arr,num,0,a)
