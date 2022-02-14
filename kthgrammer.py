#kth grammer using recursion
#problem url : https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k==1 and n==1:
            return 0
        mid = (2**(n-1))//2
        if k<=mid:
            return Solution().kthGrammar(n-1,k)
        else:
            if Solution().kthGrammar(n-1,k-mid) == 0:
                return 1
            else:
                return 0
