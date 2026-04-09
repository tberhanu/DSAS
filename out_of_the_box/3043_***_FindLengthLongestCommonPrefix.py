class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes, longest = set(), 0

        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])
        
        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                if s[: i] in prefixes:
                    longest = max(longest, i)
        return longest
        



class Solution2: # Time Limit Exceeded.     708 / 718 testcases passed
    def longestCommonPrefix2(self, arr1: List[int], arr2: List[int]) -> int:
        """
        double for loop, bruteforce
        arr1 = [1, 10, 100], 
            arr2 = [1000]
        convert to str and count prefix
        """
        longest = 0
        for num1 in arr1:
            num1 = str(num1)
            if len(num1) <= longest:
                continue
            for num2 in arr2:
                num2 =  str(num2)
                if len(num2) <= longest:
                    continue
                count = self.get_common_prefix_count(num1, num2)
                longest = max(longest, count)
        return longest
    
    def get_common_prefix_count(self, num1, num2):
        count = 0
        for n1, n2 in zip(num1, num2):
            if n1 == n2:
                count += 1
            else:
                return count
        return count

