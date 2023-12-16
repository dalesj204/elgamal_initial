from __future__ import print_function

p = 103875884360103211991897586898037781183899818694169088324836118209929355028883
g = 19337813427646184739424464459107629746680173987835432904634899380776619812079
H = 6343087477697406215547913137244545421914737047273749624341349833379509687087
b = 46434048098888938362095095444967125024438409723853932409707374167548736061787  
    

# pulverizer/extended Euclidean algo
def pulverizer(a, b):
    # basis
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = pulverizer(b % a, a)
    
    # update x and y after recursive calls
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y
    

def decrypt_num(A, y):
    _, _, inverse_A = pulverizer(p, A)
    # msg = (y * int(pow(inverse_A, b))) % p
    msg = (y * pow(inverse_A, b, p)) % p
    return chr(msg)
    

f = open('cipher23.txt', 'r')
lines = f.readlines()
ascii_list = []
for line in lines:
    split_line = line.split('   ')
    half_mask = int(split_line[0])
    cipher = int(split_line[1])
    # print(half_mask)
    # print(cipher)
    ascii_list.append(decrypt_num(half_mask, cipher))

for letter in ascii_list:
    print(letter, end ="")
# print(ascii_list)

file = open("elgamal_decrypted.txt", "w")
for element in ascii_list:
        file.write(element)
            
file.close()
    