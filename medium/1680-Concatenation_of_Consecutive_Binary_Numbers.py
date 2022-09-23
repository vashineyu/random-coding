"""1680: bin and int
Given an integer n,
return the decimal value of the binary string formed by concatenating the binary representations of 
1 to n in order, modulo 10 ** 9 + 7.
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:

        binary = '0b'

        for i in range(1, n + 1):
            binary += bin(i)[2:]
        decimal = int(binary, 2)

        return decimal % (10 ** 9 + 7)


if __name__ == '__main__':
    testcases = [1, 3, 12]
    answers = [1, 27, 505379714]

    sol = Solution()
    for testcase, answer in zip(testcases, answers):
        result = sol.concatenatedBinary(testcase)
        print(f'Input: {testcase}, Output= {result}, IsCorrect={result == answer}')
