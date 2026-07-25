class solution:
   def partition(self,arr,low,high):
       pivot = arr[low]
       i = low+1
       j = high
       
       while True:
           while i<= high and arr[i]<= pivot:
               i += 1
            
           while j >= low and arr[j]>pivot:
               j -= 1
             
           if i>=j:
               break
           
           arr[i],arr[j] = arr[j],arr[i]
           
       arr[low],arr[j] = arr[j],arr[low]
       return j


   def quick_sort(self,arr,low,high):
       if low < high:
           partition_index = self.partition(arr,low,high)
           self.quick_sort(arr,low,partition_index - 1)
           self.quick_sort(arr,partition_index + 1,high)
            
arr = [5,3,2,1,6,7]
sol = solution()
sol.quick_sort(arr,0,len(arr)-1)
print(*arr) 