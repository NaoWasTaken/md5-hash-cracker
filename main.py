import hashlib

flag = 0

pass_hash = input('Enter md5 Hash: ')

wordlist = input('File Name: ')

try:
    pass_file = open (wordlist, 'r')
except Exception as e:
    print(f'Error: {e}')
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print('Password Found')
        print(word)
        flag = 1
        break

if flag == 0:
    print('Password is not in list.')
