"""1700: queue
The school cafeteria offers circular and square sandwiches at lunch break,
 referred to by numbers 0 and 1 respectively.

All students stand in a queue.
Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students.
The sandwiches are placed in a stack. At each step:

- If the student at the front of the queue prefers the sandwich on the top of the stack,
 they will take it and leave the queue.
- Otherwise, they will leave it and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where
 sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and
 students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue).

Return the number of students that are unable to eat.
"""
import typing as t


class Solution:
    def countStudents(
        self,
        students: t.List[int],
        sandwiches: t.List[int]
    ) -> int:

        while True:
            if len(sandwiches) == 0:
                return 0

            sandwiche = sandwiches[0]

            go_to_end = []
            n_students = len(students)
            for i in range(n_students + 1):
                if i == n_students:
                    return n_students

                student = students.pop(0)
                if student == sandwiche:
                    students.extend(go_to_end)
                    break
                go_to_end.append(student)
            sandwiches = sandwiches[1:]


if __name__ == '__main__':
    testcases = [
        [
            [1, 1, 0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1],
        ],
    ]
    answers = [
        6,
    ]
    sol = Solution()
    for testcase, ans in zip(testcases, answers):
        result = sol.countStudents(*testcase)
        print(f'Output={result}, IsCorrect={result==ans}')