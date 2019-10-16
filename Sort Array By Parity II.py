#922
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        num_even = list(filter(lambda x:x%2==0, A))
        num_odd = list(filter(lambda x:x%2!=0, A))
        num_all = []
        for i in range(len(num_even)):
            num_all.append(num_even[i])
            num_all.append(num_odd[i])
        return num_all   
