import numpy as np 
import matplotlib.pyplot as plt

# NRZ_L (Non Return to Zero_Level) Encoding
def nrz_l_encoding(data):
    encoded_data = []

    for bit in data:
        if bit == '1':
            encoded_data.append(1)  # High voltage for '1'
        else:
            encoded_data.append(-1)  # Low voltage for '0'

    return encoded_data


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

#calling Functions and printing values
binary_data =input("Enter the data: ")
nrz_l_data = nrz_l_encoding(binary_data)
palindrome=longestPalindrome(binary_data)
print("Binary Data:", list(binary_data))
print("NRZ-L Encoded Data:", nrz_l_data)
print("Longest palindrome in dataStream: ",palindrome)

#Plotting values on a graph
def plot(nrz_l_data):
    plt.step(range(len(nrz_l_data)), nrz_l_data, where='post', color='blue', linewidth=4)
    plt.title('NRZ-L Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0,color='red')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    for i in range(0, len(nrz_l_data)):
        plt.axvline(i, color='grey', linestyle='--')
    plt.show()


plot(nrz_l_data)