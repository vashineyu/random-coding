"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = re.search(pattern=needle, string=haystack)
        
        if match:
            return match.start()
        else:
            return -1
