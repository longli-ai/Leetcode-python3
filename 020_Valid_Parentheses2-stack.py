class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {'[':']', '{':'}', '(':')'}
        list1 = []
        for i in s:
            if len(list1) > 0:
                if list1[-1] in dict1:
                    if i == dict1[list1[-1]]:
                        list1.pop()
                    else:
                        list1.append(i)
                        pass
                    pass
                else:
                    list1.append(i)
                    pass
                pass    
            else:
                list1.append(i)
                pass
            pass
        if len(list1) == 0:
            return True
        return False
'''
Runtime: 52 ms, faster than 18.42% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.1 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
'''
