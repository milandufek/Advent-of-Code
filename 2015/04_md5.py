from hashlib import md5


key = 'ckczppom'
leading_zeros = '0' * 6

for i in range(999999999):
    s = key + str(i)
    hash = md5(s.encode()).hexdigest()

    if hash.startswith(leading_zeros):
        print(f'{i} ({s} -> {hash})')
        break
