class DistanceCalculator:
    def __init__(self):
        self.goalDistance = 100
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

    def subDistance(self, numIn):
        if numIn > 0:
            if self.walkedDistance - numIn < 0:
                print("You cannot walk negative distance")
            else:
                self.walkedDistance -= numIn

class AppHandler:
    def __init__(self):
        self.calc = DistanceCalculator()

    

if __name__ == "__main__":
    print("running")