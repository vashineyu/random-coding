"""
You are given a nested list of integers nestedList.
Each element is either an integer or a list whose elements may also be integers or other lists.
Implement an iterator to flatten it.

Implement the NestedIterator class:

- NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
- int next() Returns the next integer in the nested list.
- boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
"""
import typing as t


# Example
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(lst):
            for item in lst:
                if not item.isInteger():
                    yield from flatten(item.getList())
                else:
                    yield item.getInteger()

        self.flat_list = list(flatten(nestedList))
        self.counter = 0

    def next(self) -> int:
        value = self.flat_list[self.counter]
        self.counter += 1
        return value


    def hasNext(self) -> bool:
        return self.counter < len(self.flat_list)