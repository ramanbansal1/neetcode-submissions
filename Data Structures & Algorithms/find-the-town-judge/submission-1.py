class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        potential_judge = {i: 0 for i in range(1, n + 1)}
        for ai, bi in trust:
            if ai in potential_judge:
                potential_judge[ai] = -1
            
            if bi in potential_judge and potential_judge[bi] != -1:
                potential_judge[bi] += 1

        
        for k, v in potential_judge.items():
            if v == n-1:
                return k

        return -1

