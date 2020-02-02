"""
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.

Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
"""


def minTimeToVisitAllPoints(points):
    time = 0
    for i in range(len(points)-1):
        # compare diff x1 to x2, x2 to x3, and so on...
        # compare diff y1 to y2, y2 to y3, and so on...
        # then the total time is max(x, y)
        x = abs(points[i][0] - points[i+1][0])
        y = abs(points[i][1] - points[i+1][1])
        time += max(x, y)
    return time


points = [[1, 1], [3, 4], [-1, 0]]
print(minTimeToVisitAllPoints(points))
