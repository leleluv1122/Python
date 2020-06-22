import math

def Point(p1, p2):
    x = (p2[0] - p1[0]) ** 2
    y = (p2[1] - p1[1]) ** 2
    z = (p2[2] - p1[2]) ** 2

    result = math.sqrt(x + y + z)

    return result

def main():
    points = [[-1, 0, 3], [-1, -1, -1], [4, 1, 1],
              [2, 0.5, 9], [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2],
              [5.5, 4, -0.5]]
    total_len = 987654321
    for i in range(len(points)):
        for j in range(len(points[i])):
            if i == j:
                continue
            c = Point(points[i], points[j])
            if total_len > c:
                total_len = c
                a = points[i]
                b = points[j]
    print("a : ", end='')
    for i in range(3):
        print(a[i], end=' ')
    print()
    print("b : ", end='')
    for i in range(3):
        print(b[i], end=' ')

main()