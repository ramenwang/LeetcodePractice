# reverse-integer
class Solution:
    def __init__(self):
        self.int32_len = 2**31

    def reverse(self, x: int) -> int:

        if x>=0:
            x_inv = ''.join(list(str(x))[::-1])
            x_inv = int(x_inv)
            if x_inv > self.int32_len - 1:
                return 0

        if x<0:
            x_inv = '-' + ''.join(list(str(-1 * x))[::-1])
            x_inv = int(x_inv)

            if x_inv < -self.int32_len:
                return 0

        return int(x_inv)
