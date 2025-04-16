# Solving a 3x3 system of linear equations using Gaussian Elimination

def gaussian_elimination(a, b):
    n = len(a)

    # Forward elimination
    for i in range(n):
        # Make the diagonal contain all non-zero elements
        if a[i][i] == 0:
            for j in range(i + 1, n):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    b[i], b[j] = b[j], b[i]
                    break

        # Make the diagonal element 1 and eliminate the column below
        factor = a[i][i]
        for k in range(i, n):
            a[i][k] = a[i][k] / factor
        b[i] = b[i] / factor

        for j in range(i + 1, n):
            factor = a[j][i]
            for k in range(i, n):
                a[j][k] -= factor * a[i][k]
            b[j] -= factor * b[i]

    # Back substitution
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]

    return x

# Example system:
# 2x + 3y - z = 5
# 4x + y + 2z = 6
# -2x + 5y - z = -4

a = [
    [2, 3, -1],
    [4, 1, 2],
    [-2, 5, -1]
]

b = [5, 6, -4]

solution = gaussian_elimination(a, b)
print("Solution:", solution)

# Coded by Suhail Fraj
