from datetime import timedelta
import datetime

rrMeanJobs = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
rrMedianJobs = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
llMeanJobs = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
llMedianJobs = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
randMeanJobs = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
randMedianJobs = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)

rrMeanTasks = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
rrMedianTasks = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
llMeanTasks = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
llMedianTasks = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
randMeanTasks = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
randMedianTasks = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)

print("-----------------------------------------   For Round Robin Algorithm -----------------------------------\n")

print("----------------  Jobs  -----------------\n")
with open("logs_jobs_rr.txt", "r") as f:

    lines = f.readlines()

    job = {}
    for line in lines:
        line = line.strip().strip("!!!").split("::")

        if(line[0] not in job):
            job[line[0]] = [0,0]
        
        if(line[1] == 's'):
            job[line[0]][0] = line[2]
                
        else:
            job[line[0]][1] = line[2]
        
    nettimes = []
    for j in job:
        nettimes.append(datetime.datetime.strptime(job[j][1], '%Y-%m-%d %H:%M:%S.%f') - datetime.datetime.strptime(job[j][0], '%Y-%m-%d %H:%M:%S.%f'))

    nettimes = sorted(nettimes)
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in nettimes:
        totaltime += time
    
    mean = totaltime/len(nettimes)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)

    rrMedianJobs = median
    rrMeanJobs = mean
    
    if(len(nettimes) %2 == 0):
        medindex = len(nettimes)//2
        median = (nettimes[medindex] + nettimes[medindex-1])/2
    else:
        medindex = len(nettimes)//2
        median = nettimes[medindex]
    
    for i, time in enumerate(nettimes):
        print("Time of completion for job ", i, "is : ", str(time))
    print("\nThe mean completion time for jobs is : ", mean, "\n")
    print("The median completion time for jobs is : ", median, "\n")    
    
print("----------------  Tasks  -----------------\n")
with open("logs_tasks_rr.txt", "r") as f:

    lines = f.readlines()

    task = {}
    for line in lines:
        line = line.strip().strip("!!!").split("::")

        if(line[1] not in task):
            task[line[1]] = [0,0]
        
        if(line[2] == 's'):
            task[line[1]][0] = line[3]
                
        else:
            task[line[1]][1] = line[3]
        
    nettimes = []
    for j in task:
        nettimes.append(datetime.datetime.strptime(task[j][1], '%Y-%m-%d %H:%M:%S.%f') - datetime.datetime.strptime(task[j][0], '%Y-%m-%d %H:%M:%S.%f'))

    nettimes = sorted(nettimes)
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in nettimes:
        totaltime += time
    
    mean = totaltime/len(nettimes)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)

    rrMeanTasks = mean
    rrMedianTasks = median
    
    if(len(nettimes) %2 == 0):
        medindex = len(nettimes)//2
        median = (nettimes[medindex] + nettimes[medindex-1])/2
    else:
        medindex = len(nettimes)//2
        median = nettimes[medindex]
    
    for i, time in enumerate(nettimes):
        print("Time of completion for task ", i, "is : ", str(time))

    print("\nThe mean completion time for tasks is : ", mean, "\n")
    print("The median completion time for tasks is : ", median, "\n") 

print("------------------------------------------   For Random Algorithm ------------------------------------\n")

print("----------------  Jobs  -----------------\n")
with open("logs_jobs_random.txt", "r") as f:

    
    lines = f.readlines()
    

    job = {}
    for line in lines:
        line = line.strip().strip("!!!").split("::")

        if(line[0] not in job):
            job[line[0]] = [0,0]
        
        if(line[1] == 's'):
            job[line[0]][0] = line[2]
                
        else:
            job[line[0]][1] = line[2]
        
    nettimes = []
    for j in job:
        nettimes.append(datetime.datetime.strptime(job[j][1], '%Y-%m-%d %H:%M:%S.%f') - datetime.datetime.strptime(job[j][0], '%Y-%m-%d %H:%M:%S.%f'))

    nettimes = sorted(nettimes)
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in nettimes:
        totaltime += time
    
    mean = totaltime/len(nettimes)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)

    randMeanJobs = mean
    randMedianJobs = median

    if(len(nettimes) %2 == 0):
        medindex = len(nettimes)//2
        median = (nettimes[medindex] + nettimes[medindex-1])/2
    else:
        medindex = len(nettimes)//2
        median = nettimes[medindex]
    
    for i, time in enumerate(nettimes):
        print("Time of completion for job ", i, "is : ", str(time))
    print("\nThe mean completion time for jobs is : ", mean, "\n")
    print("The median completion time for jobs is : ", median, "\n")    
    
print("----------------  Tasks  -----------------\n")
with open("logs_tasks_random.txt", "r") as f:

    lines = f.readlines()

    task = {}
    for line in lines:
        line = line.strip().strip("!!!").split("::")

        if(line[1] not in task):
            task[line[1]] = [0,0]
        
        if(line[2] == 's'):
            task[line[1]][0] = line[3]
                
        else:
            task[line[1]][1] = line[3]
        
    nettimes = []
    for j in task:
        nettimes.append(datetime.datetime.strptime(task[j][1], '%Y-%m-%d %H:%M:%S.%f') - datetime.datetime.strptime(task[j][0], '%Y-%m-%d %H:%M:%S.%f'))

    nettimes = sorted(nettimes)
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in nettimes:
        totaltime += time
    
    mean = totaltime/len(nettimes)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)

    randMedianTasks = median
    randMeanTasks = mean

    if(len(nettimes) %2 == 0):
        medindex = len(nettimes)//2
        median = (nettimes[medindex] + nettimes[medindex-1])/2
    else:
        medindex = len(nettimes)//2
        median = nettimes[medindex]
    
    for i, time in enumerate(nettimes):
        print("Time of completion for task ", i, "is : ", str(time))

    print("\nThe mean completion time for tasks is : ", mean, "\n")
    print("The median completion time for tasks is : ", median, "\n") 

print("------------------------------------------   For Least Loaded Scheduling Algorithm -----------------------------------\n")

print("----------------  Jobs  -----------------\n")
with open("logs_jobs_ll.txt", "r") as f:

    lines = f.readlines()

    job = {}
    for line in lines:
        line = line.strip().strip("!!!").split("::")

        if(line[0] not in job):
            job[line[0]] = [0,0]
        
        if(line[1] == 's'):
            job[line[0]][0] = line[2]
                
        else:
            job[line[0]][1] = line[2]
        
    nettimes = []
    for j in job:
        nettimes.append(datetime.datetime.strptime(job[j][1], '%Y-%m-%d %H:%M:%S.%f') - datetime.datetime.strptime(job[j][0], '%Y-%m-%d %H:%M:%S.%f'))

    nettimes = sorted(nettimes)
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in nettimes:
        totaltime += time
    
    mean = totaltime/len(nettimes)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)

    llMeanJobs = mean
    llMedianJobs = median
    
    if(len(nettimes) %2 == 0):
        medindex = len(nettimes)//2
        median = (nettimes[medindex] + nettimes[medindex-1])/2
    else:
        medindex = len(nettimes)//2
        median = nettimes[medindex]
    
    for i, time in enumerate(nettimes):
        print("Time of completion for job ", i, "is : ", str(time))
    print("\nThe mean completion time for jobs is : ", mean, "\n")
    print("The median completion time for jobs is : ", median, "\n")    
    
print("----------------  Tasks  -----------------\n")
with open("logs_tasks_ll.txt", "r") as f:

    lines = f.readlines()

    task = {}
    for line in lines:
        line = line.strip().strip("!!!").split("::")

        if(line[1] not in task):
            task[line[1]] = [0,0]
        
        if(line[2] == 's'):
            task[line[1]][0] = line[3]
                
        else:
            task[line[1]][1] = line[3]
        
    nettimes = []
    for j in task:
        nettimes.append(datetime.datetime.strptime(task[j][1], '%Y-%m-%d %H:%M:%S.%f') - datetime.datetime.strptime(task[j][0], '%Y-%m-%d %H:%M:%S.%f'))

    nettimes = sorted(nettimes)
    totaltime = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)
    for time in nettimes:
        totaltime += time
    
    mean = totaltime/len(nettimes)
    median = timedelta(days=0, seconds=0, milliseconds= 0, minutes=0, hours=0)

    llMedianTasks = median
    llMeanTasks = mean

    if(len(nettimes) %2 == 0):
        medindex = len(nettimes)//2
        median = (nettimes[medindex] + nettimes[medindex-1])/2
    else:
        medindex = len(nettimes)//2
        median = nettimes[medindex]
    
    for i, time in enumerate(nettimes):
        print("Time of completion for task ", i, "is : ", str(time))

    print("\nThe mean completion time for tasks is : ", mean, "\n")
    print("The median completion time for tasks is : ", median, "\n")     
    
differentAlgoMeanJobTimings = []
differentAlgoMeanJobTimings.append([llMeanJobs, 0])
differentAlgoMeanJobTimings.append([rrMeanJobs, 1])
differentAlgoMeanJobTimings.append([randMeanJobs, 2])

differentAlgoMedianJobTimings = []
differentAlgoMedianJobTimings.append([llMedianJobs, 0])
differentAlgoMedianJobTimings.append([rrMedianJobs, 1])
differentAlgoMedianJobTimings.append([randMedianJobs, 2])

differentAlgoMeanJobTimings = sorted(differentAlgoMeanJobTimings)
differentAlgoMedianJobTimings = sorted(differentAlgoMedianJobTimings)

print("\n\nAscending Order of algorithms in terms of mean :")
for meantimings in differentAlgoMeanJobTimings:
    if(meantimings[1] == 0):
        print("Least Loaded : ", str(meantimings[0]), "\n")
    elif(meantimings[1] == 1):
        print("Round Robin : ", str(meantimings[0]), "\n")
    else:
        print("Random : ", str(meantimings[0]), "\n")
        
print("\n\nAscending Order of algorithms in terms of median :")
for mediantimings in differentAlgoMedianJobTimings:
    if(mediantimings[1] == 0):
        print("Least Loaded : ", str(mediantimings[0]), "\n")
    elif(mediantimings[1] == 1):
        print("Round Robin : ", str(mediantimings[0]), "\n")
    else:
        print("Random : ", str(mediantimings[0]), "\n")
        
differentAlgoMeanTaskTimings = []
differentAlgoMeanTaskTimings.append([llMeanTasks, 0])
differentAlgoMeanTaskTimings.append([rrMeanTasks, 1])
differentAlgoMeanTaskTimings.append([randMeanTasks, 2])

differentAlgoMedianTaskTimings = []
differentAlgoMedianTaskTimings.append([llMedianTasks, 0])
differentAlgoMedianTaskTimings.append([rrMedianTasks, 1])
differentAlgoMedianTaskTimings.append([randMedianTasks, 2])

differentAlgoMeanTaskTimings = sorted(differentAlgoMeanTaskTimings)
differentAlgoMedianTaskTimings = sorted(differentAlgoMedianTaskTimings)

print("\n\nAscending Order of algorithms in terms of mean task execution time :\n")
for meantimings in differentAlgoMeanTaskTimings:
    if(meantimings[1] == 0):
        print("Least Loaded : ", str(meantimings[0]), "\n")
    elif(meantimings[1] == 1):
        print("Round Robin : ", str(meantimings[0]), "\n")
    else:
        print("Random : ", str(meantimings[0]), "\n")
        
print("\n\nAscending Order of algorithms in terms of median task execution time :\n")
for mediantimings in differentAlgoMedianTaskTimings:
    if(mediantimings[1] == 0):
        print("Least Loaded : ", str(mediantimings[0]), "\n")
    elif(mediantimings[1] == 1):
        print("Round Robin : ", str(mediantimings[0]), "\n")
    else:
        print("Random : ", str(mediantimings[0]), "\n")
