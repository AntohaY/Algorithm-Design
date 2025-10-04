def shortest_common_supersequence(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # print(A[i-1])
            # print(B[j-1])
            if A[i-1] == B[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

    # Backtrack to build result
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            result.append(A[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] < dp[i][j-1]:
            result.append(A[i-1])
            i -= 1
        else:
            result.append(B[j-1])
            j -= 1

    # Add leftovers
    while i > 0:
        result.append(A[i-1])
        i -= 1
    while j > 0:
        result.append(B[j-1])
        j -= 1
    print("".join(reversed(result)))
    return "".join(reversed(result))

A = input()
B = input()
shortest_common_supersequence(A, B)
