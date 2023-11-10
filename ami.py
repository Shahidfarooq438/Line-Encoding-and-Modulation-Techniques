import matplotlib.pyplot as plt
import numpy as np

# AMI (Alternate Mark Inversion) Encoding
def ami_encoding(bits):
    encoded_bits = []
    current_level = 1  # Initial level

    for bit in bits:
        if bit == '0':
            # Represent binary 0 as a zero level
            encoded_bits.append(0)
        elif bit == '1':
            # Represent binary 1 as an alternating positive and negative level
            encoded_bits.append(current_level)
            current_level = -current_level  # Invert the level for the next bit

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

#Calling functions and printing output.
binary_data =input("Enter the data: ")
ami_data = ami_encoding(binary_data)
palindrome=longestPalindrome(binary_data)
print("Binary Data:", list(binary_data))
print("AMI Encoded Data:", ami_data)
print("Longest palindrome in dataStream: ",palindrome)


#Plotting values on a graph
def plot(ami_data):
    plt.step(range(len(ami_data)), ami_data, where='post', color='blue', linewidth=4)
    plt.title('AMI Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0,color='red')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    for i in range(0, len(ami_data)):
        plt.axvline(i, color='grey', linestyle='--')
    plt.show()

plot(ami_data)