#import matplotlib.pyplot as plt
from datetime import timedelta
import datetime

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
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
        
        end = lines[index].strip().strip("!!!").split("::")
        end = end[3]
        end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
        
        durations.append(end - start)
        
    durations = sorted(durations)
    
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in durations:
        totaltime += time
        
    mean = totaltime/len(durations)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    
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
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
        
        end = lines[index].strip().strip("!!!").split("::")
        end = end[2]
        end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
        
        durations.append(end - start)
        
    durations = sorted(durations)
    
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in durations:
        totaltime += time
        
    mean = totaltime/len(durations)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    
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
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
        
        end = lines[index].strip().strip("!!!").split("::")
        end = end[3]
        end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
        
        durations.append(end - start)
        
    durations = sorted(durations)
    
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in durations:
        totaltime += time
        
    mean = totaltime/len(durations)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    
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
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
        
        end = lines[index].strip().strip("!!!").split("::")
        end = end[2]
        end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
        
        durations.append(end - start)
        
    durations = sorted(durations)
    
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in durations:
        totaltime += time
        
    mean = totaltime/len(durations)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    
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
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
        
        end = lines[index].strip().strip("!!!").split("::")
        end = end[3]
        end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
        
        durations.append(end - start)
        
    durations = sorted(durations)
    
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in durations:
        totaltime += time
        
    mean = totaltime/len(durations)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    
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
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
        
        end = lines[index].strip().strip("!!!").split("::")
        end = end[2]
        end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
        
        durations.append(end - start)
        
    durations = sorted(durations)
    
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in durations:
        totaltime += time
        
    mean = totaltime/len(durations)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    
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
        