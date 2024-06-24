class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):

        maximumDifferenceCalculation = 0

        # Find the maximum absolute difference between 2 numbers in __elements
        for i in range(len(a) - 1):
            for j in range(len(a) - 1):
                absoluteDifference = abs(a[i] - a[j + 1])
                if absoluteDifference > maximumDifferenceCalculation:
                    maximumDifferenceCalculation = absoluteDifference

        # Store it in maximiumDifference
        self.maximumDifference = maximumDifferenceCalculation

        return maximumDifferenceCalculation


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
