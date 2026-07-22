class solution:
    def bubble_sort(self,arr,n):
        if n==1:
            return
        
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                
        self.bubble_sort(arr,n-1)

arr = [6,5,4,3,2,1]
sol = solution()
n = len(arr)
sol.bubble_sort(arr,n)
print(*arr)
