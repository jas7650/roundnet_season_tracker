from enum import Enum

class TournamentType(Enum):
    CONTENDER = 0
    CHALLENGER = 1 
    MAJOR = 2
    CHAMPIONSHIP_PRO = 3
    CHAMPIONSHIP_PREMIER = 4

contender_2022 = [150, 90, 57, 40.5, 33, 30, 27, 25.5, 24, 22.5, 21, 19.5, 18, 17.1, 16.5, 15.9, 15.3, 14.7, 14.1, 13.5, 12.9, 12.3, 11.7, 11.1, 10.65, 10.2, 9.75, 9.3, 8.85, 8.4, 7.95, 7.5, 7.05, 6.6, 6.3, 6, 5.7, 5.4, 5.1, 4.8, 4.5, 4.2, 3.9, 3.6, 3.3, 3.15, 3, 2.85, 2.7, 2.55, 2.4, 2.25, 2.1, 1.95, 1.8, 1.74, 1.68, 1.62, 1.56, 1.5, 1.44, 1.38, 1.32, 1.26, 1.2, 1.14, 1.08, 1.02, 0.96, 0.9, 0.87, 0.84, 0.81, 0.78, 0.75, 0.72, 0.69, 0.66, 0.63, 0.6, 0.57, 0.54, 0.51, 0.48, 0.45]
challenger_2022 = [500, 300, 190, 135, 110, 100, 90, 85, 80, 75, 70, 65, 60, 57, 55, 53, 51, 49, 47, 45, 43, 41, 39, 37, 35.5, 34, 32.5, 31, 29.5, 28, 26.5, 25, 23.5, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10.5, 10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6, 5.8, 5.6, 5.4, 5.2, 5, 4.8, 4.6, 4.4, 4.2, 4, 3.8, 3.6, 3.4, 3.2, 3, 2.9, 2.8, 2.7, 2.6, 2.5, 2.4, 2.3, 2.2, 2.1, 2, 1.9, 1.8, 1.7, 1.6, 1.5]
major_2022 = [875, 525, 332.5, 236.25, 192.5, 175, 157.5, 148.75, 140, 131.25, 122.5, 113.75, 105, 99.75, 96.25, 92.75, 89.25, 85.75, 82.25, 78.75, 75.25, 71.75, 68.25, 64.75, 62.125, 59.5, 56.875, 54.25, 51.625, 49, 46.375, 43.75, 41.125, 38.5, 36.75, 35, 33.25, 31.5, 29.75, 28, 26.25, 24.5, 22.75, 21, 19.25, 18.375, 17.5, 16.625, 15.75, 14.875, 14, 13.125, 12.25, 11.375, 10.5, 10.15, 9.8, 9.45, 9.1, 8.75, 8.4, 8.05, 7.7, 7.35, 7, 6.65, 6.3, 5.95, 5.6, 5.25, 5.075, 4.9, 4.725, 4.55, 4.375, 4.2, 4.025, 3.85, 3.675, 3.5, 3.325, 3.15, 2.975, 2.8, 2.625]
championship_2022 = [1500, 900, 570, 405, 330, 300, 270, 255, 240, 225, 210, 195, 180, 171, 165, 159, 153, 147, 141, 135, 129, 123, 117, 111, 106.5, 102, 97.5, 93, 88.5, 84, 79.5, 75, 70.5, 66, 63, 60, 57, 54, 51, 48, 45, 42, 39, 36, 33, 31.5, 30, 28.5, 27, 25.5, 24, 22.5, 21, 19.5, 18, 17.4, 16.8, 16.2, 15.6, 15, 14.4, 13.8, 13.2, 12.6, 12, 11.4, 10.8, 10.2, 9.6, 9, 8.7, 8.4, 8.1, 7.8, 7.5, 7.2, 6.9, 6.6, 6.3, 6, 5.7, 5.4, 5.1, 4.8, 4.5]
points_2022 = [contender_2022, challenger_2022, major_2022, championship_2022]


def getPoints(tounamentType : int, year : int, ranks : list):
    if year == 2022:
        index = tounamentType
        if tounamentType == TournamentType.CHAMPIONSHIP_PREMIER.value:
            index = 3
        points = []
        for point in points_2022[index]:
            points.append(point/2.0)
        return getActualPoints(ranks, points)
    

def getActualPoints(ranks, points):
    previousRank = 0
    average = 0
    i = 0
    actual_points = []
    if (len(ranks) != len(points)):
        points = points[ranks[0]-1:]
    while (i < len(ranks)):
        rank = ranks[i]
        if (rank != previousRank):
            average = getAverageValue(ranks, points, i)

        actual_points.append(average)
        previousRank = rank
        i = i + 1
    return actual_points


def getAverageValue(ranks, points, index):
    if (index == len(ranks)-1):
        return ranks[index]
    i = index+1
    numValues = 1
    sum = points[index]

    while (ranks[i] == ranks[index]):
        sum += points[i]
        numValues += 1
        i += 1
        if (i == len(ranks)):
            break
    return sum/numValues
