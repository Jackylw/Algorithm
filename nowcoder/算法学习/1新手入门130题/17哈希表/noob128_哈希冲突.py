# https://www.nowcoder.com/practice/37594c5b299e495096a99cf6e4cdf2f5
from hashlib import sha256
from itertools import product

enc_len = int(input().strip())
enc_key = input().strip()

hashes = {}

for cs in product("abcdefghijklmnopqrstuvwxyz", repeat=enc_len):
    s = "".join(cs)
    full_str = enc_key + s
    h = sha256(full_str.encode("utf-8")).hexdigest()[:enc_len]

    if h in hashes:
        print(hashes[h], s)
        break
    else:
        hashes[h] = s
