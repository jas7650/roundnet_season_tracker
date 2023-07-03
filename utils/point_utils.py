from enum import Enum

class TournamentType(Enum):
    CHALLENGER = 0
    MAJOR = 1
    CHAMPIONSHIP = 2
    CONTENDER = 3

challenger_2022 = [500, 300, 190, 135, 110, 100, 90, 85, 80, 75, 70, 65, 60, 57, 55, 53, 51, 49, 47, 45, 43, 41, 39, 37, 35.5, 34, 32.5, 31, 29.5, 28, 26.5, 25, 23.5, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10.5, 10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6, 5.8, 5.6, 5.4, 5.2, 5, 4.8, 4.6, 4.4, 4.2, 4, 3.8, 3.6, 3.4, 3.2, 3, 2.9, 2.8, 2.7, 2.6, 2.5, 2.4, 2.3, 2.2, 2.1, 2, 1.9, 1.8, 1.7, 1.6, 1.5]
major_2022 = [875, 525, 332.5, 236.25, 192.5, 175, 157.5, 148.75, 140, 131.25, 122.5, 113.75, 105, 99.75, 96.25, 92.75, 89.25, 85.75, 82.25, 78.75, 75.25, 71.75, 68.25, 64.75, 62.125, 59.5, 56.875, 54.25, 51.625, 49, 46.375, 43.75, 41.125, 38.5, 36.75, 35, 33.25, 31.5, 29.75, 28, 26.25, 24.5, 22.75, 21, 19.25, 18.375, 17.5, 16.625, 15.75, 14.875, 14, 13.125, 12.25, 11.375, 10.5, 10.15, 9.8, 9.45, 9.1, 8.75, 8.4, 8.05, 7.7, 7.35, 7, 6.65, 6.3, 5.95, 5.6, 5.25, 5.075, 4.9, 4.725, 4.55, 4.375, 4.2, 4.025, 3.85, 3.675, 3.5, 3.325, 3.15, 2.975, 2.8, 2.625]
championship_2022 = [1500, 900, 570, 405, 330, 300, 270, 255, 240, 225, 210, 195, 180, 171, 165, 159, 153, 147, 141, 135, 129, 123, 117, 111, 106.5, 102, 97.5, 93, 88.5, 84, 79.5, 75, 70.5, 66, 63, 60, 57, 54, 51, 48, 45, 42, 39, 36, 33, 31.5, 30, 28.5, 27, 25.5, 24, 22.5, 21, 19.5, 18, 17.4, 16.8, 16.2, 15.6, 15, 14.4, 13.8, 13.2, 12.6, 12, 11.4, 10.8, 10.2, 9.6, 9, 8.7, 8.4, 8.1, 7.8, 7.5, 7.2, 6.9, 6.6, 6.3, 6, 5.7, 5.4, 5.1, 4.8, 4.5]
contender_2022 = [150, 90, 57, 40.5, 33, 30, 27, 25.5, 24, 22.5, 21, 19.5, 18, 17.1, 16.5, 15.9, 15.3, 14.7, 14.1, 13.5, 12.9, 12.3, 11.7, 11.1, 10.65, 10.2, 9.75, 9.3, 8.85, 8.4, 7.95, 7.5, 7.05, 6.6, 6.3, 6, 5.7, 5.4, 5.1, 4.8, 4.5, 4.2, 3.9, 3.6, 3.3, 3.15, 3, 2.85, 2.7, 2.55, 2.4, 2.25, 2.1, 1.95, 1.8, 1.74, 1.68, 1.62, 1.56, 1.5, 1.44, 1.38, 1.32, 1.26, 1.2, 1.14, 1.08, 1.02, 0.96, 0.9, 0.87, 0.84, 0.81, 0.78, 0.75, 0.72, 0.69, 0.66, 0.63, 0.6, 0.57, 0.54, 0.51, 0.48, 0.45]
points_2022 = [challenger_2022, major_2022, championship_2022, contender_2022]

challenger_2023_1_7 = [150, 90, 57, 40.5, 33, 30, 27]
challenger_2023_8_16 = [300, 180, 114, 81, 66, 60, 54, 51, 48, 45, 42, 39, 36, 34.2, 33, 31.8]
challenger_2023_17_32 = [500, 300, 190, 135, 110, 100, 90, 85, 80, 75, 70, 65, 60, 57, 55, 53, 51, 49, 47, 45, 43, 41, 39, 37, 35.5, 34, 32.5, 31, 29.5, 28, 26.5, 25]
challenger_2023_33 = [600, 360, 228, 162, 132, 120, 108, 102, 96, 90, 84, 78, 72, 68.4, 66, 63.6, 61.2, 58.8, 56.4, 54, 51.6, 49.2, 46.8, 44.4, 42.6, 40.8, 39, 37.2, 35.4, 33.6, 31.8, 30, 28.2, 26.4, 25.2, 24, 22.8, 21.6, 20.4, 19.2, 18, 16.8, 15.6, 14.4, 13.2, 12.6, 12, 11.4, 10.8, 10.2, 9.6, 9, 8.4, 7.8, 7.2, 6.96, 6.72, 6.48, 6.24, 6, 5.76, 5.52, 5.28, 5.04, 4.8, 4.56, 4.32, 4.08, 3.84, 3.6, 3.48, 3.36, 3.24, 3.12, 3, 2.88, 2.76, 2.64, 2.52, 2.4, 2.28, 2.16, 2.04, 1.92, 1.8]
major_2023 = [1100, 660, 418, 297, 242, 220, 198, 187, 176, 165, 154, 143, 132, 125.4, 121, 116.6, 112.2, 107.8, 103.4, 99, 94.6, 90.2, 85.8, 81.4, 78.1, 74.8, 71.5, 68.2, 64.9, 61.6, 58.3, 55, 51.7, 48.4, 46.2, 44, 41.8, 39.6, 37.4, 35.2, 33, 30.8, 28.6, 26.4, 24.2, 23.1, 22, 20.9, 19.8, 18.7, 17.6, 16.5, 15.4, 14.3, 13.2, 12.76, 12.32, 11.88, 11.44, 11, 10.56, 10.12, 9.68, 9.24, 8.8, 8.36, 7.92, 7.48, 7.04, 6.6, 6.38, 6.16, 5.94, 5.72, 5.5, 5.28, 5.06, 4.84, 4.62, 4.4, 4.18, 3.96, 3.74, 3.52, 3.3, 3.08, 2.86, 2.64, 2.42, 2.2]
championship_2023 = [1600, 960, 608, 432, 352, 320, 288, 272, 256, 240, 224, 208, 192, 182.4, 176, 169.6, 163.2, 156.8, 150.4, 144, 137.6, 131.2, 124.8, 118.4, 113.6, 108.8, 104, 99.2, 94.4, 89.6, 84.8, 80]
points_2023 = [challenger_2023_1_7, challenger_2023_8_16, challenger_2023_17_32, challenger_2023_33, major_2023, championship_2023]


def getTournamentType(type : str):
    if type == "challenger":
        return TournamentType.CHALLENGER.value
    if type == "major":
        return TournamentType.MAJOR.value
    if type == "championship":
        return TournamentType.CHAMPIONSHIP.value
    return TournamentType.CONTENDER.value


def getPoints(tounamentType : int, year : int, ranks : list, numTeams : int):
    if year == 2022:
        index = tounamentType
        points = []
        for point in points_2022[index]:
            points.append(point/2.0)
        return getActualPoints(ranks, points)
    if year == 2023:
        if tounamentType == TournamentType.CHALLENGER.value:
            if numTeams < 8:
                return getActualPoints(ranks, points_2023[0])
            if numTeams >= 8 and numTeams < 17:
                return getActualPoints(ranks, points_2023[1])
            if numTeams > 16 and numTeams < 33:
                return getActualPoints(ranks, points_2023[2])
            if numTeams > 32:
                return getActualPoints(ranks, points_2023[3])
        if tounamentType == TournamentType.MAJOR.value:
            return getActualPoints(ranks, points_2023[4])
        if tounamentType == TournamentType.CHAMPIONSHIP.value:
            return getActualPoints(ranks, points_2023[5])
    

def getActualPoints(ranks, points):
    previousRank = 0
    average = 0
    i = 0
    actual_points = []
    if len(ranks) != len(points):
        points = points[ranks[0]-1:]
    while i < len(ranks):
        rank = ranks[i]
        if rank != previousRank:
            average = getAverageValue(ranks, points, i)

        actual_points.append(average)
        previousRank = rank
        i = i + 1
    return actual_points


def getAverageValue(ranks, points, index):
    if index >= len(ranks) or index >= len(points):
        return 0
    if index == len(ranks)-1 or index == len(points)-1:
        return points[index]
    i = index+1
    numValues = 1
    sum = points[index]

    while ranks[i] == ranks[index]:
        sum += points[i]
        numValues += 1
        i += 1
        if (i == len(ranks)):
            break
    return sum/numValues
