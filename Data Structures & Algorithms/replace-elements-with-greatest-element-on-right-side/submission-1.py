class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest_right_num = 0
        right_of_val = arr[:]

        for i in range(len(arr)):
            if i+1 == len(arr):
                arr[i] = -1
                return arr
            
            right_of_val = arr[i+1:]

            arr[i] = max(right_of_val)
            
            largest_right_num = 0
        return arr