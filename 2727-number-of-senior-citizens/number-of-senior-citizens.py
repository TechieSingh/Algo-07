class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result=0
        age_lst=[]
        for i in details:
            list(i)
            age_lst.append(int(i[11:13]))
        for i in age_lst:
            if i > 60:
                result+=1
        return result
        