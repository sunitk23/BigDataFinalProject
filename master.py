import sys
import math
import threading
import random
from socket import AF_INET, SOCK_STREAM, error, socket
import time
import datetime
#from goto import goto, label
import json
from ast import literal_eval

cmdLineInput = sys.argv
jSonConfigFileLocation = cmdLineInput[1]
schedulingAlgorithmCode = cmdLineInput[2]

configFile = open(jSonConfigFileLocation)
configFileContents = configFile.read()
configFileContents = json.loads(configFileContents)

#Global variables
FileWriteOnce = 0
nMapTasksPerJob = {}
reducerTasksPerJob = {}
nRedTasksPerJob = {}
workerCondition = {}
workers = configFileContents['workers']
nWorkers = len(workers)
roundRobinCounter = -1

#for logs
jobCounterArrival = 0
jobCounterCompletion = 0

# Populating dictionary with <key : value> pair as <workerID : [nAvailableSlots, workerPortNumber]> 
for worker in workers:
    if(worker['worker_id'] not in workerCondition):
        workerCondition[worker['worker_id']] = [worker['slots'],worker['port']]
    else:
        error("Error : Duplicate worker IDs not allowed\n")
        sys.exit()

# Mutex to prevent race condition amongst threads
workerMutex = threading.Lock()
taskMutex = threading.Lock()


#Scheduling algorithms

def getList(dict): 
    li = [] 
    for key in dict.keys(): 
        li.append(key) 
          
    return sorted(li)

def getUnsortedList(dict): 
    li = [] 
    for key in dict.keys(): 
        li.append(key) 
          
    return li

def UpdateRoundRobinCounter(num, divisor): 
    return (num % divisor)

def roundRobinTaskScheduler(task):
    global roundRobinCounter, nWorkers, workerCondition, workerMutex

    TCPsocket = socket(AF_INET, SOCK_STREAM)
    
    workersIDList = getList(workerCondition)
    
    workerMutex.acquire()
    
    roundRobinCounter = UpdateRoundRobinCounter(roundRobinCounter + 1, nWorkers)
    slotsAvailable = workerCondition[workersIDList[roundRobinCounter]][0]
    cycleCount = 0
    while(not(slotsAvailable)):
        roundRobinCounter = UpdateRoundRobinCounter(roundRobinCounter + 1, nWorkers)
        slotsAvailable = workerCondition[workersIDList[roundRobinCounter]][0]
        cycleCount = cycleCount + 1
        if(cycleCount == nWorkers - 1):
            cycleCount = 0
            time.sleep(1)
        
    slotsAvailable = slotsAvailable - 1
    workerCondition[workersIDList[roundRobinCounter]][0] = slotsAvailable
    
    message = str(task)
    message = message + "::rr"
    TCPsocket.connect(('127.0.0.1',workerCondition[workersIDList[roundRobinCounter]][1]))
    TCPsocket.send(message.encode())
    #print(task[0], task[1], task[2], "sent to worker\n")
    TCPsocket.close()
    
    workerMutex.release()

def leastLoadedTaskScheduler(task):
    global workerCondition, workerMutex
    
    TCPsocket = socket(AF_INET, SOCK_STREAM)
    
    workersIDList = getUnsortedList(workerCondition)
    
    workerMutex.acquire()
    
    maximumFreeSlots = 0
    pos = 0
    while(not(maximumFreeSlots)):
        i = 0
        while(i < nWorkers):
            if workerCondition[workersIDList[i]][0] > maximumFreeSlots : 
                    maximumFreeSlots = workerCondition[workersIDList[i]][0]
                    pos = i
            i = i + 1
        
        if(not(maximumFreeSlots)):
            time.sleep(1)
        
    workerCondition[workersIDList[pos]][0] = workerCondition[workersIDList[pos]][0] - 1
    
    message = str(task)
    message = message + "::ll"
    TCPsocket.connect(('127.0.0.1',workerCondition[workersIDList[pos]][1]))
    TCPsocket.send(message.encode())
    TCPsocket.close()

    workerMutex.release()

def randomTaskScheduler(task):
    global workerCondition, workerMutex
    # Locking the following critical section
    workerMutex.acquire()
    
    TCPsocket = socket(AF_INET, SOCK_STREAM)
    
    workerDictKeys = list(workerCondition.keys())
    
    randomValue = random.randint(0, nWorkers - 1)
    randomSelectedWorkerId = workerDictKeys[randomValue]
    
    slotsAvailable = workerCondition[randomSelectedWorkerId][0]
    
    while(not(slotsAvailable)):
        randomValue = random.randint(0, nWorkers - 1)
        randomSelectedWorkerId = workerDictKeys[randomValue]
        slotsAvailable = workerCondition[randomSelectedWorkerId][0]
        
        if(not(slotsAvailable)):
            time.sleep(1)
        
    workerCondition[randomSelectedWorkerId][0] = workerCondition[randomSelectedWorkerId][0] - 1

    message = str(task)
    message = message + "::random"
    TCPsocket.connect(('127.0.0.1', workerCondition[randomSelectedWorkerId][1]))
    TCPsocket.send(message.encode())
    TCPsocket.close()
    
    workerMutex.release()
    # Lock released allowing other threads to access CS

def jobRequestsDataFromFile():
    global nMapTasksPerJob, jobCounterArrival, schedulingAlgorithmCode, reducerTasksPerJob, FileWriteOnce, taskMutex
    
    TCPsocket = socket(AF_INET, SOCK_STREAM)
    TCPsocket.bind(('127.0.0.1',5000))
    TCPsocket.listen(100)

    while True:
        conn, _ = TCPsocket.accept()
        if conn:
            
            jobRequest = conn.recv(1024)
            
            jobReceiveTime = datetime.datetime.now()
            

            filename = "logs_jobs_" + schedulingAlgorithmCode.lower()
            
            with open(filename + ".txt", "a+") as f:
                f.write("{id}::{start}::{stime}!!!\n".format(id = jobCounterArrival, start = "s", stime = jobReceiveTime))
            jobCounterArrival = jobCounterArrival + 1
            
            jobRequest = jobRequest.decode()
            jobRequest = json.loads(jobRequest)
            outputString = "Received Job " + str(jobRequest['job_id'])
            print(jobReceiveTime, end = " ")
            print(outputString)
            
            for mapTask in jobRequest['map_tasks']:
                taskDetails = [jobRequest['job_id'], mapTask['task_id'], mapTask['duration']]
                
                if schedulingAlgorithmCode.lower() == 'random':
                    randomTaskScheduler(taskDetails)
                elif(schedulingAlgorithmCode == 'LL' or schedulingAlgorithmCode == 'll'):
                    leastLoadedTaskScheduler(taskDetails)
                elif(schedulingAlgorithmCode == 'RR' or schedulingAlgorithmCode == 'rr'):
                    roundRobinTaskScheduler(taskDetails)
                else:
                    error('Unknown Scheduler : Program exiting with code : 1\n')
                    sys.exit()
                    
            taskMutex.acquire()
            
            nMapTasksPerJob[jobRequest['job_id']] = len(jobRequest['map_tasks'])
            reducerTasksPerJob[jobRequest['job_id']] = jobRequest['reduce_tasks']
            
            taskMutex.release()

def scheduleReduceTasks(jobRequestID, reducerTasksList):
    for reducerTask in reducerTasksList: 
        taskDetails = [str(jobRequestID), reducerTask['task_id'], reducerTask['duration']]

        if schedulingAlgorithmCode.lower() == 'random':
            randomTaskScheduler(taskDetails)        
        elif(schedulingAlgorithmCode == 'LL' or schedulingAlgorithmCode == 'll'):
            leastLoadedTaskScheduler(taskDetails)  
        elif(schedulingAlgorithmCode == 'RR' or schedulingAlgorithmCode == 'rr'):
            roundRobinTaskScheduler(taskDetails)
        else:
            error('Unknown Scheduler : Program exiting with code : 1\n')
            sys.exit()

def workerUpdataData():
 global workerCondition, nMapTasksPerJob, jobCounterCompletion, reducerTasksPerJob, taskMutex, workerMutex

 TCPsocket = socket(AF_INET, SOCK_STREAM)
 TCPsocket.bind(('localhost',5001))
 TCPsocket.listen(100)

 while True:
  conn, _ = TCPsocket.accept()
  taskUpdateData = conn.recv(1024)
        
        #print(task[0], task[1], task[2], "worker status received\n")
  if taskUpdateData:
   taskUpdateData = literal_eval(taskUpdateData.decode())


   workerMutex.acquire()
   jobRequestID = taskUpdateData[0]
   workerID = taskUpdateData[2]
   workerCondition[workerID][0] = workerCondition[workerID][0] + 1    
   workerMutex.release()

   taskMutex.acquire()

   listOfKeys = getList(nMapTasksPerJob)
   lengthOfReducerTasksList = 0
            
            
   if jobRequestID in listOfKeys:
    nMapTasksPerJob[jobRequestID] = nMapTasksPerJob[jobRequestID] - 1

    if nMapTasksPerJob[jobRequestID] == 0:
     nMapTasksPerJob.pop(jobRequestID)
     reducerTasksList = reducerTasksPerJob.pop(jobRequestID)
     for i in reducerTasksList:
      lengthOfReducerTasksList = lengthOfReducerTasksList + 1
     nRedTasksPerJob[jobRequestID] = lengthOfReducerTasksList

     scheduleReduceTasks(jobRequestID, reducerTasksList)
                        
   else:
    nRedTasksPerJob[jobRequestID] = nRedTasksPerJob[jobRequestID] - 1
    if nRedTasksPerJob[jobRequestID] == 0:
                    
     jobEndTime = datetime.datetime.now()
                    
     filename = "logs_jobs_" + schedulingAlgorithmCode.lower()
                    
     with open(filename + ".txt", "a") as f:
      f.write("{id}::{end}::{etime}!!!\n".format(id = jobCounterCompletion, end = "e", etime = jobEndTime))
     jobCounterCompletion += 1
     outputString = "Completed Job " + str(jobRequestID)
     print(jobEndTime, end=" ")
     print(outputString)
                    
     nRedTasksPerJob.pop(jobRequestID)

   taskMutex.release()

JobReceiverThread = threading.Thread(target = jobRequestsDataFromFile)
JobReceiverThread.start()

WorkerTaskUpdateThread = threading.Thread(target = workerUpdataData)
WorkerTaskUpdateThread.start()

JobReceiverThread.join()
WorkerTaskUpdateThread.join()
