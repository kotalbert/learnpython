print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
print int("0b11001001", 2)
 
shift_right = 0b1100
shift_left = 0b1
 
# Your code here!
shift_right  = shift_right >> 2
shift_left = shift_left << 2
 
print bin(shift_right)
print bin(shift_left)
 
def check_bit4(input):
    mask = 0b1000
    if input & mask > 0:
        return "on"
    else:
        return "off"
     
a = 0b10111011
mask = 0b100
print bin(a | mask)
 
a       = 0b11101110
mask    = 0b11111111
print bin(a ^ mask)

def flip_bit(number, n):
    mask = (0b1 << n-1)
    result = number ^ mask
    return bin(result)

print flip_bit(0b111,2)