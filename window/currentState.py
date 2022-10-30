
class currentState:
    def __init__(self, cpuTemp, cpuUsage, cpuPowerDraw, gpuTemp, gpuUsage, gpuPowerDraw):
        self.cpuTemp = cpuTemp
        self.cpuUsage = cpuUsage
        self.cpuPowerDraw = cpuPowerDraw
        self.gpuTemp = gpuTemp
        self.gpuUsage = gpuUsage
        self.gpuPowerDraw = gpuPowerDraw

    def getCPUTemp(self):
        return self.cpuTemp    