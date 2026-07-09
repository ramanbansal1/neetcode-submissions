from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        data = deque([['0000',0]])
        deadends = set(deadends)
        assessed = set()
        while data:
            curr, t = data.popleft()
            if curr in deadends or curr in assessed:
                continue
            if curr == target:
                return t
            
            assessed.add(curr)

            for i, s in enumerate(curr):
                temp = list(curr)
                if s == '9':
                    temp[i] = '0'
                    temp1 = ''.join(temp)
                    data.append((temp1, t+1))
                else:
                    temp[i] = str(int(s) + 1)
                    temp1 = ''.join(temp)
                    data.append((temp1, t+1))
                if s == '0':
                    temp[i] = '9'
                    temp1 = ''.join(temp)
                    data.append((temp1, t+1))
                else:
                    temp[i] = str(int(s) - 1)
                    temp1 = ''.join(temp)
                    data.append((temp1, t+1))

        return -1