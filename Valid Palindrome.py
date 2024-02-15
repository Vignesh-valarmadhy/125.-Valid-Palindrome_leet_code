class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and remove non-alphanumeric characters
        alphanumeric_str = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the alphanumeric string is equal to its reverse
        return alphanumeric_str == alphanumeric_str[::-1]

# Example usage:
solution = Solution()
input_str = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(input_str))  # Output: True
