import math

f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"
S1 = "What are you doing while sending "  # ends with a space
S2 = " Are you busy? Will you send "      # starts with a space

def is_k_within(n, k):
    if k < 1:
        return False
    if n == 0:
        return k <= len(f0)
    required = (k + 68) / 143
    if required <= 1:
        return True
    needed_exponent = math.ceil(math.log2(required))
    return n >= needed_exponent

def get_char(n, k)