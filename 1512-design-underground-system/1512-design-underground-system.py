class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.average = collections.defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = [stationName, t]   

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customers:
            return
        startStation, startTime = self.customers.pop(id)
        self.average[(startStation, stationName)][0] += (t - startTime)
        self.average[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, legs = self.average[(startStation,  endStation)]
        return total / legs