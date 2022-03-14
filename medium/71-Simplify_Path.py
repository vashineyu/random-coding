"""71
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system,
convert it to the simplified canonical path.

In a Unix-style file system,
    - a period '.' refers to the current directory,
    - a double period '..' refers to the directory up a level,
    - and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.
For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:
- The path starts with a single slash '/'.
- Any two directories are separated by a single slash '/'.
- The path does not end with a trailing '/'.
- The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_segments = path.split('/')

        result = []
        for path_segment in path_segments:
            if path_segment in ['', '.']:
                continue

            if path_segment != '..':
                result.append(path_segment)
            elif path_segment == '..':
                if len(result) > 0:
                    result.pop()
            else:
                assert False, f'Unexpected segment: {path_segment}'

        return '/' + '/'.join(i for i in result)


if __name__ == '__main__':
    testcases = [
        "/home/",
        "/../",
        "/home//foo/",
    ]
    answers = [
        "/home",
        "/",
        "/home/foo",
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.simplifyPath(testcase)
        print(f'Input: {testcase}\nOutput: {result}\nIsCorrect: {ans==result}')
