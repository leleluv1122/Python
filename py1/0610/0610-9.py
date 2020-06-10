def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

def nearestPoints(points):
    p1, p2 = 0, 1

    shortestDistance = distance(points[p1][0], points[p1][1],
                points[p2][0], points[p2][1])

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i][0], points[i][1],
                        points[j][0], points[j][1])

            if shortestDistance > d:
                p1, p2 = i, j
                shortestDistance = d

    return p1, p2


def main():
    numberOfPoints = eval(input("Enter the number of points: "))

    points = []
    print("Enter", numberOfPoints, "points:", end='')
    for i in range(numberOfPoints):
        point = 2 * [0]
        point[0], point[1] = eval(input("Enter coordinates separated by a comma: "))
        points.append(point)

    p1, p2 = nearestPoints(points)

    print("the closest two points are (" +
          str(points[p1][0]) + ", " + str(points[p1][1]) + ") and ("  +
          str(points[p2][0]) + ", " + str(points[p2][1]) + ")")

main()