class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest_right_num = 0
        right_of_val = arr[:]

        for i in range(len(arr)):
            if i+1 == len(arr):
                arr[i] = -1
                return arr
            
            right_of_val = arr[i+1:]

            for item in right_of_val:
                if item > largest_right_num:
                    largest_right_num = item
            
            arr[i] = largest_right_num
            largest_right_num = 0
        return arr