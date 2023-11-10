import matplotlib.pyplot as plt
import numpy as np

# NRZ_I (Non Return to Zero_Inverted) Encoding
def nrz_i_encoding(bits):
    encoded_bits = []
    current_level = 1  # Start with a high level

    for bit in bits:
        if bit=='1':
            current_level = -current_level  # Invert the level for a binary 1
        encoded_bits.append(current_level)
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


# Function Calling and printing values 
binary_data =input("Enter the data: ")
nrz_i_data = nrz_i_encoding(binary_data)
palindrome=longestPalindrome(binary_data)
print("Binary Data:", list(binary_data))
print("NRZ-I Encoded Data:", nrz_i_data)
print("Longest palindrome in dataStream: ",palindrome)


#Plotting values on a graph
def plot(nrz_i_data):
    plt.step(range(len(nrz_i_data)), nrz_i_data, where='post', color='blue', linewidth=4)
    plt.title('NRZ-I Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0,color='red')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    for i in range(0, len(nrz_i_data)):
        plt.axvline(i, color='grey', linestyle='--')
    plt.show()

plot(nrz_i_data)