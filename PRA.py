class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        Out = []
        arr3 = []
        for i in arr2:
            for j in arr1: 
                if j == i:
                    Out.append(j)
        for k in arr1:    
            if k not in arr2:
                arr3.append(k)
        arr3 = sorted(arr3)
        Out = Out + arr3
        print(Out)    
        return Out