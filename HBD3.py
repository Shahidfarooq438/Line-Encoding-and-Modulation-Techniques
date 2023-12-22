import matplotlib.pyplot as plt
import numpy as np

# HBD3 (Scrambled AMI Encoding)
def hdb3_encoding(bits):
    encoded_bits = []
    consecutive_zeros_count = 0
    last_substitution = 0
    current_level=1

    for bit in bits:
        if bit == '1':
            # Represent binary 1 as an alternating positive and negative level
            encoded_bits.append(current_level)
            consecutive_zeros_count = 0
            last_substitution = 0
            current_level=-current_level
        elif bit == '0':
            consecutive_zeros_count += 1
            if consecutive_zeros_count == 4:
                for _ in range(3):
                    encoded_bits.pop()
                # If there is an even number of 1s since the last substitution, substitute with B00V
                if last_substitution % 2 == 0:
                    current_level=-current_level
                    encoded_bits.extend([-current_level, 0, 0,-current_level])
                    last_substitution += 1
                # If there is an odd number of 1s since the last substitution, substitute with 000V
                else:
                    encoded_bits.extend([0, 0, 0,-current_level])
                    last_substitution += 1
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


#Calling Functions And printing values
binary_data =input("Enter the data: ")
hbd3_data = hdb3_encoding(binary_data)
palindrome=longestPalindrome(binary_data)
print("Binary Data:", list(binary_data))
print("HDB3 Encoded Data:", hbd3_data)
print("Longest palindrome in dataStream: ",palindrome)

#Plotting values on a graph
def plot(hbd3_data):
    plt.step(range(len(hbd3_data)), hbd3_data, where='post', color='blue', linewidth=4)
    plt.title('HBD3 Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0,color='red')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    for i in range(0, len(hbd3_data)):
        plt.axvline(i, color='grey', linestyle='--')
    plt.show()

plot(hbd3_data)