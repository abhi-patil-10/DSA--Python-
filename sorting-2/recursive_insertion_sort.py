class solution:
    def insertion_sort(self ,arr,i,n):
        if i == n:
            return
        
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j -= 1
        
        self.insertion_sort(arr,i+1,n)

arr = [5,4,3,2,1]
sol = solution()
sol.insertion_sort(arr,0,len(arr))
print(*arr)
        