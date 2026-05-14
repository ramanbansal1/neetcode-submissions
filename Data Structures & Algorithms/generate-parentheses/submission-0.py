class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path):

            if len(path) == 2 * n:
                if check_path(path):
                    res.append(path)
                    return
                return
            
            for i in ['(', ')']:
                path += i
                backtrack(path)
                path = path[:-1]
        
        def check_path(path):
            stack = 0

            for i in path:
                if i == '(':
                    stack += 1
                
                if i == ')':
                    stack -= 1
                
                if stack < 0:
                    return False
            return not stack

        backtrack("")
        return res