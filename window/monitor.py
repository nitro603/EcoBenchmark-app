import subprocess
import threading
import os
import currentState

cpuTemp = 0;
cpuUsage = 0;
cpuPowerDrawPackage = 0;
gpuTemp = 0;
gpuUsage = 0; 
gpuPowerDraw = 0;

def getData():
    abspath = os.path.abspath(os.getcwd())

    cmdLine = os.path.join(abspath, r"data\EcoHWMonitor\bin\Debug\EcoHWMonitor.exe")
    process = subprocess.Popen("\""+ r"D:\Desktop- SSD\COMP SCI\EXP Boost\Github\EcoBenchmark\EcoBenchmark\EcoBenchmark-app\data\EcoHWMonitor\bin\Debug\EcoHWMonitor.exe" + "\"", shell=True)
    process.communicate()
    with open(r'D:\Desktop- SSD\COMP SCI\EXP Boost\Github\EcoBenchmark\EcoBenchmark\EcoBenchmark-app\data\EcoHWMonitor\stats\data.txt') as d:
        lines = d.readlines()
        if len(lines) > 0:
            cpuTemp, cpuUsage, cpuPowerDraw, gpuTemp, gpuUsage, gpuPowerDraw = lines
            current = currentState.currentState(cpuTemp,cpuUsage,cpuPowerDraw,gpuTemp,gpuUsage,gpuPowerDraw)
            return current
              

getData()