def minDeletionSize(A):
    n = len(A)
    if n <= 1:
        return 0
    m = len(A[0])
    unfixed = set(range(n - 1))
    deletions = 0
    for col in range(m):
        conflict = False
        for i in unfixed:
            if A[i][col] > A[i+1][col]:
                conflict = True
                break
        if conflict:
            deletions += 1
        else:
            to_remove = set()
            for i in unfixed:
                if A[i][col] < A[i+1][col]:
                    to_re