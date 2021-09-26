def encrypt():
    strings = input('Enter your message to encrypt: ')
    even = strings[::2]
    odd = strings[1::2]
    print(even + odd)
encrypt()

def decrypt():
    string = input('what is your message to decrypt: ')
    length = len(string)
    half_length = (length+1)//2
    even = string[:half_length]
    odd = string[half_length:]

    msg = ''
    if length % 2 == 0:
        for i in range(half_length):
            join = even[i]+odd[i]
            msg = msg+join
    else:
        for i in range(1, half_length+1):
            start = i-1
            join = even[start:i]+odd[start:i]
            msg = msg + join
    print(msg)
decrypt()