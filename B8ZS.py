import matplotlib.pyplot as plt
import numpy as np

# B8ZS (Scrambled AMI Encoding)
def b8zs_encoding(bits):
    encoded_bits = []
    consecutive_zeros_count = 0

    for bit in bits:
        if bit == '1':
            # Represent binary 1 as an alternating positive and negative level
            encoded_bits.append(1)
            consecutive_zeros_count = 0
        elif bit == '0':
            consecutive_zeros_count += 1
            if consecutive_zeros_count == 8:
                # Replace eight consecutive zeros with a special code (000VB0VB)
                encoded_bits.extend([0, 0, 0, 0, 0, 0, 0, 0])
                consecutive_zeros_count = 0
            else:
                # Represent binary 0 as a zero level
                encoded_bits.append(0)

    return encoded_bits

# Finding Longest Palindrome in the data-stream
def longestPalindrome(s):
    longest_palindrom = ''
    dp = [[0]*len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrom = s[i]
    for i in range(len(s)-1,-1,-1):
        for j in range(i+1,len(s)):  
            if s[i] == s[j]:
                if j-i ==1 or dp[i+1][j-1] is True:
                    dp[i][j] = True
                    if len(longest_palindrom) < len(s[i:j+1]):
                        longest_palindrom = s[i:j+1]                
    return longest_palindrom

# Printing values and function calling
binary_data =input("Enter the data: ")
b8zs_data = b8zs_encoding(binary_data)
palindrome=longestPalindrome(binary_data)
print("Binary Data:", list(binary_data))
print("B8ZS Encoded Data:", b8zs_data)
print("Longest palindrome in dataStream: ",palindrome)

#Plotting values on a graph
def plot(b8zs_data):
    plt.step(range(len(b8zs_data)), b8zs_data, where='post', color='blue', linewidth=4)
    plt.title('B8ZS Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0,color='red')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    for i in range(0, len(b8zs_data)):
        plt.axvline(i, color='grey', linestyle='--')
    plt.show()

plot(b8zs_data)