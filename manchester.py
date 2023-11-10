import matplotlib.pyplot as plt
import numpy as np

#Manchester Encoding Technique
def manchester_encoding(bits):
    encoded_bits = []

    for bit in bits:
        if bit == '0':
            # Represent binary 0 as a high-to-low transition followed by a low-to-high transition
            encoded_bits.extend([1, -1])
        elif bit == '1':
            # Represent binary 1 as a low-to-high transition followed by a high-to-low transition
            encoded_bits.extend([-1, 1])

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

# Function calling and output printing
binary_data =input("Enter the data: ")
manchester_data = manchester_encoding(binary_data)
palindrome=longestPalindrome(binary_data)
print("Binary Data:", list(binary_data))
print("Manchester Encoded Data:", manchester_data)
print("Longest palindrome in dataStream: ",palindrome)


#Plotting values on a graph
def plot(manchester_data):
    plt.step(range(len(manchester_data)), manchester_data, where='post', color='blue', linewidth=4)
    plt.title('Manchester Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0,color='red')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    for i in range(0, len(manchester_data)):
        plt.axvline(i, color='grey', linestyle='--')
    plt.show()

plot(manchester_data)