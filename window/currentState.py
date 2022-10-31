import math
from scipy.interpolate import interp1d

class currentState:
    def __init__(self, cpuTemp, cpuUsage, cpuPowerDraw, gpuTemp, gpuUsage, gpuPowerDraw):
        self.cpuTemp = cpuTemp
        self.cpuUsage = cpuUsage
        self.cpuPowerDraw = cpuPowerDraw
        self.gpuTemp = gpuTemp
        self.gpuUsage = gpuUsage
        self.gpuPowerDraw = gpuPowerDraw

    def cpuTempScore(self, value):
        pointsForTempsCPU = interp1d([29,110],[33,0])
        return pointsForTempsCPU(value)
    
    def cpuUsageScore(self, value):
        pointsForUtilCPU = interp1d([0,100],[33,0])
        return pointsForUtilCPU(value)
    
    def cpuPowerDrawScore(self, value):
        pointsForPowerDrawCPU = interp1d([20,155],[33,0])
        return pointsForPowerDrawCPU(value)
    
    def gpuTempScore(self, value):
        pointsForTempsGPU = interp1d([29,110],[33,0])
        return pointsForTempsGPU(value)
    
    def gpuUsageScore(self, value):
        pointsForUtilGPU = interp1d([0,100],[33,0])
        return pointsForUtilGPU(value)
    
    def gpuPowerDrawScore(self, value):
        pointsForPowerDrawGPU = interp1d([0,155],[33,0])
        return pointsForPowerDrawGPU(value)
    
    def getEcoScore(self):
        cpuScore = self.cpuTempScore(self.cpuTemp) + self.cpuUsageScore(self.cpuUsage) + self.cpuPowerDrawScore(self.cpuPowerDraw)
        gpuScore = self.gpuTempScore(self.gpuTemp) + self.gpuUsageScore(self.gpuUsage) + self.gpuPowerDrawScore(self.gpuPowerDraw)
        
        return str(math.floor(cpuScore + gpuScore))