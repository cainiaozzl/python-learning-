def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "on"
    else:
        return "off"

a = 0b10111011

mask = 0b100
desired = a | mask
print(bin(desired))

a = 0b11101110

mask = 0b11111111
desired = a ^ mask

print(bin(desired))

def flip_bit(number, n):
    bit_to_flip = 0b1 << (n -1)
    result = number ^ bit_to_flip
    return bin(result)
