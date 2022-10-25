using System;
using System.Threading;
using System.IO;
using OpenHardwareMonitor.Hardware;

namespace PPSU_hwmonitor_c
{
    class StatsMonitor
    {
        /**
         *  Define vars to hold stats
         **/

        // CPU Temp
        static float cpuTemp;
        // CPU Usage
        static float cpuUsage;
        // CPU Power Draw (Package)
        static float cpuPowerDrawPackage;
        // CPU Frequency
        static float cpuFrequency;
        // GPU Temperature
        static float gpuTemp;
        // GPU Usage
        static float gpuUsage;
        // GPU Core Frequency
        static float gpuCoreFrequency;
        // GPU Memory Frequency
        static float gpuMemoryFrequency;
        // GPU Power Draw
        static float gpuPowerDraw;

        /**
         * Init OpenHardwareMonitor.dll Computer Object
         **/

        static Computer c = new Computer()
        {
            GPUEnabled = true,
            CPUEnabled = true,
            //RAMEnabled = true, // uncomment for RAM reports
            //MainboardEnabled = true, // uncomment for Motherboard reports
            //FanControllerEnabled = true, // uncomment for FAN Reports
            //HDDEnabled = true, // uncomment for HDD Report
        };

        /**
         * Pulls data from OHM
         **/

        static void ReportSystemInfo()
        {
            foreach (var hardware in c.Hardware)
            {
                
                // Targets AMD & Nvidia GPUS
                if (hardware.HardwareType == HardwareType.GpuAti || hardware.HardwareType == HardwareType.GpuNvidia)
                {
                    // only fire the update when found
                    
                    hardware.Update();
                    // loop through the data
                    foreach (var sensor in hardware.Sensors)
                    {
                        if (sensor.SensorType == SensorType.Temperature && sensor.Name.Contains("GPU Core"))
                        {
                            // store
                            gpuTemp = sensor.Value.GetValueOrDefault();
                            // print to console
                            /*System.Diagnostics.Debug.WriteLine("gpuTemp: " + sensor.Value.GetValueOrDefault());*/
                        }
                        else if (sensor.SensorType == SensorType.Load && sensor.Name.Contains("GPU Core"))
                        {
                            // store
                            gpuUsage = sensor.Value.GetValueOrDefault();
                            // print to console
                            /*System.Diagnostics.Debug.WriteLine("gpuUsage: " + sensor.Value.GetValueOrDefault());*/
                        }
                        else if (sensor.SensorType == SensorType.Clock && sensor.Name.Contains("GPU Core"))
                        {
                            // store
                            gpuCoreFrequency = sensor.Value.GetValueOrDefault();
                            // print to console
                            /*System.Diagnostics.Debug.WriteLine("gpuCoreFrequency: " + sensor.Value.GetValueOrDefault());*/
                        }
                        else if (sensor.SensorType == SensorType.Clock && sensor.Name.Contains("GPU Memory"))
                        {
                            // store
                            gpuMemoryFrequency = sensor.Value.GetValueOrDefault();
                            // print to console
                            /*System.Diagnostics.Debug.WriteLine("gpuMemoryFrequency: " + sensor.Value.GetValueOrDefault());*/
                        } else if(sensor.SensorType == SensorType.Power && sensor.Name.Contains("GPU Total"))
                        {
                            gpuPowerDraw = sensor.Value.GetValueOrDefault();
                            /*System.Diagnostics.Debug.WriteLine("gpuPowerDraw: " + sensor.Value.GetValueOrDefault());*/
                        }
                    }
                }

                if (hardware.HardwareType == HardwareType.CPU)
                {
                    // only fire the update when found
                    hardware.Update();

                    // loop through the data
                    foreach (var sensor in hardware.Sensors)
                        if (sensor.SensorType == SensorType.Temperature && sensor.Name.Contains("CPU Package"))
                        {
                            // store
                            cpuTemp = sensor.Value.GetValueOrDefault();
                            // print to console
                           /* System.Diagnostics.Debug.WriteLine("cpuTemp: " + sensor.Value.GetValueOrDefault());*/

                        }
                        else if (sensor.SensorType == SensorType.Load && sensor.Name.Contains("CPU Total"))
                        {
                            // store
                            cpuUsage = sensor.Value.GetValueOrDefault();
                            // print to console
                            /*System.Diagnostics.Debug.WriteLine("cpuUsage: " + sensor.Value.GetValueOrDefault());*/

                        }
                        else if (sensor.SensorType == SensorType.Power && sensor.Name.Contains("CPU Package"))
                        {
                            // store
                            cpuPowerDrawPackage = sensor.Value.GetValueOrDefault();
                            // print to console
                           /* System.Diagnostics.Debug.WriteLine("CPU Power Draw - Package: " + sensor.Value.GetValueOrDefault());*/


                        }
                        else if (sensor.SensorType == SensorType.Clock && sensor.Name.Contains("CPU Core #1"))
                        {
                            // store
                            cpuFrequency = sensor.Value.GetValueOrDefault();
                            // print to console
                            /*System.Diagnostics.Debug.WriteLine("cpuFrequency: " + sensor.Value.GetValueOrDefault());*/
                        }
                }


                



            }
        }

        static void Main(string[] args)
        {
            c.Open();
            ReportSystemInfo();
            
            
            string abspath = System.Reflection.Assembly.GetExecutingAssembly().Location.Substring(0,(System.Reflection.Assembly.GetExecutingAssembly().Location).IndexOf("bin"));
            string path = Path.Combine(abspath,"stats\\data.txt");
            
            using (StreamWriter writer = new StreamWriter(path))
                 {
                     writer.WriteLine(cpuTemp);
                     writer.WriteLine(cpuUsage);
                     writer.WriteLine(cpuPowerDrawPackage);

                     writer.WriteLine(gpuTemp);
                     writer.WriteLine(gpuUsage);
                     writer.WriteLine(gpuPowerDraw);
                 }

                
            
            
            



        }
    }
}