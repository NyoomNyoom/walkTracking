class DistanceCalculator:
    def __init__(self, goalDist):
        self.goalDistance = goalDist
        self.walkedDistance = 0

    def addDistance(self, numIn):
        if numIn > 0:
            self.walkedDistance += numIn
    

if __name__ == "__main__":
    print("running")