def main():
    import sys

    base_str = "What are you doing at the end of the world? Are you busy? Will you save us?"
    A_str = "What are you doing while sending "  # Length 33
    B_str = "? Are you busy? Will you send "    # Length 30
    E_char = '?'

    threshold = 55  # chosen based on when L_prev surpasses 1e18

    def process_query(n, k):
        if k == 0:
            return '.'  # 1-based indexing, so 0 is invalid
        if n < threshold:
            L_n = 143 * (2 ** n) - 68
  