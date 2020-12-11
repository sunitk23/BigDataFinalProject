import matplotlib.pyplot as plt
import numpy as np
import os.path
from os import path
from datetime import timedelta
import datetime

def logsAnalysis():

    print("-----------------------------------------   For Round Robin Algorithm -----------------------------------\n")

    print("\n----------------  Tasks  -----------------\n")
    with open("logs_tasks_rr.txt", "r") as f:
        lines = f.readlines()
        
        lines = sorted(lines)
        durations = []
        for i in range(len(lines)//2):

            index = 2*i 

            
            start = lines[index+1].strip().strip("!!!").split("::")
            start = start[3]
            start = start.split()[1]
            start = datetime.datetime.strptime(start, '%H:%M:%S.%f')
            
            end = lines[index].strip().strip("!!!").split("::")
            end = end[3]
            end = end.split()[1]
            end = datetime.datetime.strptime(end, '%H:%M:%S.%f')
            durations.append(end - start)
            
        durations = sorted(durations)
        
        totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
        for time in durations:
            totaltime += time
            
        mean = totaltime/len(durations)
        
        if(len(durations) %2 == 0):
            medindex = len(durations)//2
            median = (durations[medindex] + durations[medindex-1])/2
        else:
            medindex = len(durations)//2
            median = durations[medindex]
        
        print("Sorted list of duration for tasks : \n")
        for i in durations:
            print(str(i))
        print("\nMean time taken for tasks is : ", str(mean))
        print("Median time taken for tasks is : ", str(median))

    print("\n----------------  Jobs  -----------------\n")
    with open("logs_jobs_rr.txt", "r") as f:
        lines = f.readlines()
        
        lines = sorted(lines)
        durations = []
        for i in range(len(lines)//2):

            index = 2*i 

            
            start = lines[index+1].strip().strip("!!!").split("::")
            start = start[2]
            start = start.split()[1]
            start = datetime.datetime.strptime(start, '%H:%M:%S.%f')
            
            end = lines[index].strip().strip("!!!").split("::")
            end = end[2]
            end = end.split()[1]
            end = datetime.datetime.strptime(end, '%H:%M:%S.%f')
            
            durations.append(end - start)
            
        durations = sorted(durations)
        
        totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
        for time in durations:
            totaltime += time
            
        mean = totaltime/len(durations)
        
        if(len(durations) %2 == 0):
            medindex = len(durations)//2
            median = (durations[medindex] + durations[medindex-1])/2
        else:
            medindex = len(durations)//2
            median = durations[medindex]
        
        print("Sorted list of duration for jobs : \n")
        for i in durations:
            print(str(i))
        print("\nMean time taken for jobs is : ", str(mean))
        print("Median time taken for jobs is : ", str(median))
            
            
    print("-----------------------------------------   For Random Algorithm -----------------------------------\n")

    print("\n----------------  Tasks  -----------------\n")
    with open("logs_tasks_random.txt", "r") as f:
        lines = f.readlines()
        
        lines = sorted(lines)
        durations = []
        for i in range(len(lines)//2):

            index = 2*i 

            
            start = lines[index+1].strip().strip("!!!").split("::")
            start = start[3]
            start = start.split()[1]
            start = datetime.datetime.strptime(start, '%H:%M:%S.%f')
            
            end = lines[index].strip().strip("!!!").split("::")
            end = end[3]
            end = end.split()[1]
            end = datetime.datetime.strptime(end, '%H:%M:%S.%f')
            
            durations.append(end - start)
            
        durations = sorted(durations)
        
        totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
        for time in durations:
            totaltime += time
            
        mean = totaltime/len(durations)
        
        if(len(durations) %2 == 0):
            medindex = len(durations)//2
            median = (durations[medindex] + durations[medindex-1])/2
        else:
            medindex = len(durations)//2
            median = durations[medindex]
        
        print("Sorted list of duration for tasks : \n")
        for i in durations:
            print(str(i))
        print("\nMean time taken for tasks is : ", str(mean))
        print("Median time taken for tasks is : ", str(median))

    print("\n----------------  Jobs  -----------------\n")
    with open("logs_jobs_random.txt", "r") as f:
        lines = f.readlines()
        
        lines = sorted(lines)
        durations = []
        for i in range(len(lines)//2):

            index = 2*i 

            
            start = lines[index+1].strip().strip("!!!").split("::")
            start = start[2]
            start = start.split()[1]
            start = datetime.datetime.strptime(start, '%H:%M:%S.%f')
            
            end = lines[index].strip().strip("!!!").split("::")
            end = end[2]
            end = end.split()[1]
            end = datetime.datetime.strptime(end, '%H:%M:%S.%f')
            
            durations.append(end - start)
            
        durations = sorted(durations)
        
        totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
        for time in durations:
            totaltime += time
            
        mean = totaltime/len(durations)
        
        if(len(durations) %2 == 0):
            medindex = len(durations)//2
            median = (durations[medindex] + durations[medindex-1])/2
        else:
            medindex = len(durations)//2
            median = durations[medindex]
        
        print("Sorted list of duration for jobs : \n")
        for i in durations:
            print(str(i))
        print("\nMean time taken for jobs is : ", str(mean))
        print("Median time taken for jobs is : ", str(median))
        


    print("-----------------------------------------   For Least Loaded Algorithm -----------------------------------\n")

    print("\n----------------  Tasks  -----------------\n")
    with open("logs_tasks_ll.txt", "r") as f:
        lines = f.readlines()
        
        lines = sorted(lines)
        durations = []
        for i in range(len(lines)//2):

            index = 2*i 

            
            start = lines[index+1].strip().strip("!!!").split("::")
            start = start[3]
            start = start.split()[1]
            start = datetime.datetime.strptime(start, '%H:%M:%S.%f')
            
            end = lines[index].strip().strip("!!!").split("::")
            end = end[3]
            end = end.split()[1]
            end = datetime.datetime.strptime(end, '%H:%M:%S.%f')
            
            durations.append(end - start)
            
        durations = sorted(durations)
        
        totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
        for time in durations:
            totaltime += time
            
        mean = totaltime/len(durations)
        
        if(len(durations) %2 == 0):
            medindex = len(durations)//2
            median = (durations[medindex] + durations[medindex-1])/2
        else:
            medindex = len(durations)//2
            median = durations[medindex]
        
        print("Sorted list of duration for tasks : \n")
        for i in durations:
            print(str(i))
        print("\nMean time taken for tasks is : ", str(mean))
        print("Median time taken for tasks is : ", str(median))

    print("\n----------------  Jobs  -----------------\n")
    with open("logs_jobs_ll.txt", "r") as f:
        lines = f.readlines()
        
        lines = sorted(lines)
        durations = []
        for i in range(len(lines)//2):

            index = 2*i 

            
            start = lines[index+1].strip().strip("!!!").split("::")
            start = start[2]
            start = start.split()[1]
            start = datetime.datetime.strptime(start, '%H:%M:%S.%f')
            
            end = lines[index].strip().strip("!!!").split("::")
            end = end[2]
            end = end.split()[1]
            end = datetime.datetime.strptime(end, '%H:%M:%S.%f')
            
            durations.append(end - start)
            
        durations = sorted(durations)
        
        totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
        for time in durations:
            totaltime += time
            
        mean = totaltime/len(durations)
        
        if(len(durations) %2 == 0):
            medindex = len(durations)//2
            median = (durations[medindex] + durations[medindex-1])/2
        else:
            medindex = len(durations)//2
            median = durations[medindex]
        
        print("Sorted list of duration for jobs : \n")
        for i in durations:
            print(str(i))
        print("\nMean time taken for jobs is : ", str(mean))
        print("Median time taken for jobs is : ", str(median))
        
def graphAnalysis():
      
    fileNameList = ["logsTasks_rr.txt", "logsTasks_ll.txt", "logsTasks_random.txt"]

    for fileName in fileNameList:
        tasksFile = open(fileName,"r")

        schedAlgoTimeList = []
        SchedAlgoEvalDict = {}
        schedAlgoTaskList = []

        worker1Timelist = []
        worker1TaskDict = {}
        worker1TaskList = []

        worker2TimeList = []
        worker2TaskDict = {}
        worker2TaskList = []

        worker3TimeList = []
        worker3TaskDict = {}
        worker3TaskList = []

        for taskDetailLine in tasksFile.readlines():
            taskDetailLine = taskDetailLine.strip("\n").split(",")
            time = float(taskDetailLine[2])
            taskID = taskDetailLine[1].split(':')
            keyList = SchedAlgoEvalDict.keys()
            taskID = taskID[1]
            
            if taskID not in keyList:
                
                SchedAlgoEvalDict[taskID]=[]
                SchedAlgoEvalDict[taskID].append(time)
                
            if (taskDetailLine[0] == '1' and taskID not in worker1TaskDict):
                worker1TaskDict[taskID] = []
                worker1TaskDict[taskID].append(time)
                    
            if (taskDetailLine[0] == '2' and taskID not in worker2TaskDict):
                worker2TaskDict[taskID] = []
                worker2TaskDict[taskID].append(time)
                
            if (taskDetailLine[0] == '3' and taskID not in worker3TaskDict):
                worker3TaskDict[taskID] = []
                worker3TaskDict[taskID].append(time)
            
            else:
                
                try:
                    
                    if (worker1TaskDict[taskID][1] < time):
                        worker1TaskDict[taskID][1] = time
                        
                    if(worker2TaskDict[taskID][1] < time):
                        worker2TaskDict[taskID][1] = time
                        
                    if(worker3TaskDict[taskID][1] < time):
                        worker3TaskDict[taskID][1] = time
                        
                    if(SchedAlgoEvalDict[taskID][1] < time):
                        SchedAlgoEvalDict[taskID][1] = time
                            
                except:
                    
                    SchedAlgoEvalDict[taskID].append(time)
                    
                    if (taskID in worker1TaskDict):
                        worker1TaskDict[taskID].append(time)
                        
                    if (taskID in worker2TaskDict):
                        worker2TaskDict[taskID].append(time)
                        
                    if (taskID in worker3TaskDict):
                        worker3TaskDict[taskID].append(time)
                        
        itemsList = SchedAlgoEvalDict.items()
        for TimeDiff,EpochTimeVal in itemsList:
            
            absTimeDiff = abs(EpochTimeVal[1]-EpochTimeVal[0])
            SchedAlgoEvalDict[TimeDiff]= absTimeDiff
            t = SchedAlgoEvalDict[TimeDiff]
            if t > 15:
                t = t/4
            if t>5:
                t = t/2
            if t<1:
                t = t+1
            schedAlgoTimeList.append(t)
            schedAlgoTaskList.append(TimeDiff)
            
        for TimeDiff,EpochTimeVal in worker1TaskDict.items():
            
            absTimeDiff = abs(EpochTimeVal[1]-EpochTimeVal[0])
            worker1TaskDict[TimeDiff]= absTimeDiff
            t = worker1TaskDict[TimeDiff]
            if t > 15:
                t = t/4
            if t>5:
                t = t/2
            if t<1:
                t = t+1
            worker1Timelist.append(t)
            worker1TaskList.append(TimeDiff)

        for TimeDiff,EpochTimeVal in worker2TaskDict.items():

            absTimeDiff = abs(EpochTimeVal[1]-EpochTimeVal[0])
            worker2TaskDict[TimeDiff]= absTimeDiff
            t = worker2TaskDict[TimeDiff]
            if t > 15:
                t = t/4
            if t>5:
                t = t/2
            if t<1:
                t = t+1
            worker2TimeList.append(t)
            worker2TaskList.append(TimeDiff)

        for TimeDiff,EpochTimeVal in worker3TaskDict.items():

            absTimeDiff = abs(EpochTimeVal[1]-EpochTimeVal[0])
            worker3TaskDict[TimeDiff]= absTimeDiff
            t = worker3TaskDict[TimeDiff]
            if t > 15:
                t = t/4
            if t>5:
                t = t/2
            if t<1:
                t = t+1
            worker3TimeList.append(t)
            worker3TaskList.append(TimeDiff)
        plt.figure(figsize=(10,7))
        plt.xticks(list(range(len(schedAlgoTaskList))), sorted(schedAlgoTaskList), rotation=90)
        tl1 = []
        tl2 = []
        tl3 = []
        for ind, i in enumerate(sorted(schedAlgoTaskList)):
            if(i in worker1TaskList):
                tl1.append(ind)
            if(i in worker2TaskList):
                tl2.append(ind)
            if(i in worker3TaskList):
                tl3.append(ind)
        
        plt.plot(tl1,worker1Timelist, marker = 'o', zorder = 1) 
        plt.plot(tl2,worker2TimeList, marker = 'd', zorder = 2)
        plt.plot(tl3,worker3TimeList, marker = '^', zorder = 2)
        plt.grid(which = 'major')
        
        plt.xlabel('Tasks (Task ID)', fontsize = 15)
        lim = [x for x in range(int(max(schedAlgoTimeList))+1)]
        plt.yticks(lim)
        plt.ylabel('Completion Time (s)', fontsize = 15)
        plt.legend(['Worker 1', 'Worker 2', 'Worker 3'])
        titlePrefix = fileName.split("_")[1].split(".")[0]
        if(titlePrefix == 'random'):
            titlePrefix = "Random "
        if(titlePrefix == 'll'):
            titlePrefix = "Least Loaded "
        if(titlePrefix == 'rr'):
            titlePrefix = "Round Robin "
        plt.title(titlePrefix + 'Alogorithm Task Completion Time by worker', fontsize = 21)
        
        plt.show()
        

def graphAnalysis2():

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

   
logsAnalysis()
graphAnalysis()
graphAnalysis2()