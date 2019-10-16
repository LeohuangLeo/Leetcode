class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        #print(arr)
        #print(len(arr))
        min_ = arr[1] - arr[0]
        Global = [[arr[0], arr[1]]]
        for i in range(1,len(arr)-1):
            if arr[i+1]-arr[i] < min_:
                Global = [[arr[i], arr[i+1]]]
                min_ = arr[i+1]-arr[i]
            elif arr[i+1]-arr[i] == min_:
                Global += [[arr[i], arr[i+1]]]
        
        return Global 