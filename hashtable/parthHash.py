class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # given a string of just parentheses
        # go through the string
        # keep track if something is the correct closing parentheses
        # O(N) where n is length of the string
        # {[]}
        stack = []
        par_mapping = {"}": "{", "]": "[", ")": "("}
        for p in s:
            if p in par_mapping:
                if len(stack) == 0:
                    return False
                most_recent = stack.pop()
                if par_mapping[p] != most_recent:
                    return False
            else:
                stack.append(p)
        if len(stack) != 0:
            return False
        return True
