def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    cycle_length = 2 * numRows - 2
    rows = [''] * numRows
    for i, char in enumerate(s):
        pos = i % cycle_length
        row = pos if pos < numRows else cycle_length - pos
        rows[row] += char
    return ''.join(rows)