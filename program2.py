def decode_message(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    # DP table where dp[i][j] represents if s[:i] matches p[:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty pattern matches empty message
    dp[0][0] = True
    
    # Initialize dp for the case where the message is empty (dp[0][j])
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # Star can match zero or more characters
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
    
    return dp[m][n]

# Example usage:
print(decode_message("aa", "a"))        # Output: False
print(decode_message("aa", "*"))        # Output: True
print(decode_message("cb", "?a"))       # Output: False
print(decode_message("adceb", "*a*b"))  # Output: True
print(decode_message("acdcb", "a*c?b")) # Output: False
