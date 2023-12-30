from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_to_chars = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        LEN: int = len(digits)
        res: List[str] = []
        cur: List[str] = []

        def dfs(i):
            if i >= LEN:
                res.append(''.join(cur.copy()))
                return

            for char in num_to_chars[int(digits[i])]:
                cur.append(char)
                dfs(i + 1)
                cur.pop()

        dfs(0)

        return res
