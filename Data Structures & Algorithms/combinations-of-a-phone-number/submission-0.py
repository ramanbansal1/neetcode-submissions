class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        data = {
            2 : 'abc',
            3 : 'def',
            4 : 'ghi',
            5 : 'jkl',
            6 : 'mno',
            7 : 'pqrs',
            8 : 'tuv',
            9 : 'wxyz'
        }
        if len(digits) == 0:
            return []

        result = []

        def backtrack(path):
            if len(path) == len(digits):
                result.append(path)
                return
            for i in data[int(digits[len(path)])]:
                path += i
                backtrack(path)
                path = path[:-1]
        
        backtrack('')

        return result
            