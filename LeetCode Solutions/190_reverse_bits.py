

def reverseBits(n: int) -> int:
    binary=bin(n) # Change the int to binary
    binNum=binary[2:] # Remove the first two digits of the binary string
    rev=binNum[::-1] # Reverse the binary
    # Sum the first 2 digits of the original binary + the reverse binary 
    # fill the rest of the 32 positions with 0
    rev=binary[:2]+rev+'0'*(32-len(rev))
    return (int(rev,2))

print(reverseBits(43261596))