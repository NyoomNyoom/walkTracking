class DistanceCalculator:
    def __init__(self, goalDist):
        self.goalDistance = goalDist
        self.walkedDistance = 0

        try:
            f = open("distanceWalked.txt", "r")
            line = f.read()
            self.walkedDistance = line
            f.close()
        except(FileNotFoundError):
            self.walkedDistance = 0
            f = open("distanceWalked", "w")
            f.close()

    def addDistance(self, numIn):
        if numIn > 0:
            self.walkedDistance += numIn

class AppHandler:
    def __init__(self):
        print('hello')

if __name__ == "__main__":
    print("running")