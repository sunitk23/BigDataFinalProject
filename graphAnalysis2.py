import matplotlib.pyplot as plt
import numpy as np
import os.path
from os import path

schedAlgos = ["rr", "ll", "random"]
workers = ["1_", "2_", "3_"]
for algo in schedAlgos:
    for worker in workers:
        fileName = "tasks_per_worker_"
        fileName = fileName + worker + algo + ".txt"
        if(path.exists(fileName)):
            tasksFile = open(fileName,"r")
            
            times = tasksFile.readlines()
            
            
            for index,time in enumerate(times):
                time = time.strip()
                times[index] = time
                
            times = sorted(times)
            print(times)
            
            tasksList = [0]
            timestamps = []
            firsttime = float(times[0].split(",")[0]) - 2
            timestamps.append(firsttime)
            tasks = 0
            for time in times:
                timestamp = time.split(",")[0]
                char = time.split(",")[1]
                if char == 'r':
                    tasks += 1
                    tasksList.append(tasks)
                elif char == 'c':
                    tasks -= 1
                    tasksList.append(tasks)
                timestamps.append(float(timestamp))
            
            timestamps = np.array(timestamps)
            timestamps -= firsttime
            timestamps = list(timestamps)
            
            plt.figure(figsize=(12, 8))
            plt.plot(timestamps, tasksList)
            titlePrefix = algo
            if(titlePrefix == 'random'):
                titlePrefix = "Random "
            if(titlePrefix == 'll'):
                titlePrefix = "Least Loaded "
            if(titlePrefix == 'rr'):
                titlePrefix = "Round Robin "
            plt.title(titlePrefix + "Tasks over time for worker " + str(worker)[:-1], fontsize = 21)
            plt.ylabel("Tasks", fontsize = 15)
            lim = [x for x in range(max(tasksList) + 2)]
            plt.yticks(lim)
            timestamps = [round(x, 3) for x in timestamps]
            plt.xlabel("timestamp (s)", fontsize = 15)
            plt.xticks(timestamps, rotation = 90)
            plt.grid(which="both")
            plt.show()
                