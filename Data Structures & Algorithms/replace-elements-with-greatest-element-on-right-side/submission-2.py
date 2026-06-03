class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest_right_num = 0
        right_of_val = arr[:]

        for i in range(len(arr)):
            #make the last value -1 and prematurely end
            if i+1 == len(arr):
                arr[i] = -1
                return arr
            
            #make an array of all the values to the right
            right_of_val = arr[i+1:]

            #assign the current value with the largest value to its right
            arr[i] = max(right_of_val)

            largest_right_num = 0
        return arr