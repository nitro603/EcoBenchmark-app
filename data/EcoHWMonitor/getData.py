import subprocess
import threading
import os

cpuTemp = 0;
cpuUsage = 0;
cpuPowerDrawPackage = 0;
gpuTemp = 0;
gpuUsage = 0; 
gpuPowerDraw = 0;

def getData():
    abspath = os.path.abspath(os.getcwd())

    threading.Timer(5.0, getData).start()
    cmdLine = os.path.join(abspath, r"data\EcoHWMonitor\bin\Debug\EcoHWMonitor.exe")
    print(cmdLine);
    process = subprocess.Popen("\""+ r"D:\Desktop- SSD\COMP SCI\EXP Boost\Github\EcoBenchmark\EcoBenchmark\EcoBenchmark-app\data\EcoHWMonitor\bin\Debug\EcoHWMonitor.exe" + "\"", shell=True)
    process.communicate()
    with open(r'D:\Desktop- SSD\COMP SCI\EXP Boost\Github\EcoBenchmark\EcoBenchmark\EcoBenchmark-app\data\EcoHWMonitor\stats\data.txt') as d:
          lines = d.readlines()
          if len(lines) > 0:
              cpuTemp, cpuUsage, cpuPowerDrawPackage, gpuTemp, gpuUsage, gpuPowerDraw = lines
             
            

getData()