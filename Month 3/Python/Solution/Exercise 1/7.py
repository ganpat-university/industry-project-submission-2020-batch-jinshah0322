a = int(input("Enter number 1:"))
b = int(input("Enter number 1:"))

bitwise_and = a & b

bitwise_or = a | b

bitwise_xor = a ^ b

bitwise_not_a = ~a
bitwise_not_b = ~b

left_shift = a << 1

right_shift = a >> 1

print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)
print("Bitwise NOT of a:", bitwise_not_a)
print("Bitwise NOT of b:", bitwise_not_b)
print("Left shift of a:", left_shift)
print("Right shift of a:", right_shift)