import subprocess
import threading

cpuTemp = 0;
cpuUsage = 0;
cpuPowerDrawPackage = 0;
gpuTemp = 0;
gpuUsage = 0; 
gpuPowerDraw = 0;

def getData():
    threading.Timer(5.0, getData).start()
    cmdLine = "data\\EcoHWMonitor\\bin\\Debug\\EcoHWMonitor.exe"
    process = subprocess.Popen(cmdLine, shell=True)
    process.communicate()
    with open('data\\EcoHWMonitor\\stats\\data.txt') as d:
         lines = d.readlines()
         if len(lines) > 0:
             cpuTemp, cpuUsage, cpuPowerDrawPackage, gpuTemp, gpuUsage, gpuPowerDraw = lines
             
            

getData()