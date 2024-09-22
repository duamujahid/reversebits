def reverse_bits(num, bit_size=32):
    result = 0
    for i in range(bit_size):
        result = (result << 1) | (num & 1)
        num >>= 1
    return result

num1 = int(input("Enter the first number : "))
bit_size = int(input("Enter the bit size : "))

reversed_num = reverse_bits(num1, bit_size)

print("Original number:", num1)
print("Reversed bits number:", reversed_num)
