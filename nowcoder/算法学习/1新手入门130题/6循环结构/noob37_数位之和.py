# https://www.nowcoder.com/practice/5e85cc26475449648e668aa98e92d05b
n = abs(int(input()))
num_sum = 0
while n != 0:
    num_sum += n % 10
    n //= 10
print(num_sum)
