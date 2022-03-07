"""784
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.
"""
import typing as t


class Solution:
    def letterCasePermutation(self, s: str) -> t.List[str]:
        def helper(current_s, path_str):
            for i in range(len(current_s)):
                char = current_s[i]
                if not char.isdigit():
                    # is character
                    helper(current_s[(i + 1):], path_str + char.upper())
                    helper(current_s[(i + 1):], path_str + char.lower())
                else:
                    path_str += char

            if len(path_str) == len(s):
                result.append(path_str)

        result = []
        helper(s, '')
        return result


if __name__ == '__main__':
    testcases = {
        'a1b2': ["a1b2","a1B2","A1b2","A1B2"],
        '3z4': ["3z4","3Z4"],
    }
    sol = Solution()
    for testcase, ans in testcases.items():
        result = sol.letterCasePermutation(testcase)
        print(f'Input: {testcase}\nOutput:{result}\nAnswer:{ans}')
