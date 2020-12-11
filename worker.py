import sys
import math
from socket import AF_INET, SOCK_STREAM, error, socket
import threading
from ast import literal_eval
import time
import datetime
#from goto import goto, label

schedulingAlgoCode = ""
fileWriteOnce = 0
workersID = int(sys.argv[2])
worker1Tasks = 0
taskLists = list()
worker2Tasks = 0
thread_lock = threading.Lock()
worker3Tasks = 0
workersPort = int(sys.argv[1])
startTime = datetime.datetime.now()



def acceptRequest():
    global taskLists, worker1Tasks, worker2Tasks, worker3Tasks, schedulingAlgoCode, workersID, fileWriteOnce, thread_lock 
    TCPsocket = socket(AF_INET, SOCK_STREAM)
    TCPsocket.bind(('127.0.0.1',workersPort))
    TCPsocket.listen(100)

    while True:
        conn,_= TCPsocket.accept()
        jobRequest = conn.recv(1024)

        if jobRequest:
            jobRequest = jobRequest.decode()
            jobRequest, schedulingAlgoCode = jobRequest.split("::")
            jobRequest = literal_eval(jobRequest)
            filename = "logs_tasks_" + schedulingAlgoCode 

            jobReceiveTime = datetime.datetime.now()

            with open(filename + ".txt", "a") as f:
                f.write("{jid}::{tid}::{s}::{stime}!!!\n".format(jid = jobRequest[0], tid = jobRequest[1], s = "s", stime = jobReceiveTime))
            
            newJobReceiveTime = time.time()
            filename = "logsTasks_" + schedulingAlgoCode

            with open(filename + ".txt", "a") as f:
                f.write("{wid},completed:{tid},{etime}\n".format(wid = workersID, tid = jobRequest[1], etime = newJobReceiveTime))
 
            jobNum = str(jobRequest[0])
            printJob = " of job " + jobNum
            taskNum = str(jobRequest[1])
            printTask = "Executing task "+ taskNum
            print(jobReceiveTime, end = " ")
            print(printTask + printJob)
            thread_lock.acquire()
            filename = "tasks_per_worker_"
            if(workersID == 1):
                worker1Tasks += 1
                filename = filename + str(workersID) + "_" + schedulingAlgoCode
                with open(filename + ".txt", "a") as f:
                    f.write("{rcvtime},r\n".format(rcvtime = newJobReceiveTime))
            if(workersID == 2):
                worker2Tasks += 1
                filename = filename + str(workersID) + "_" + schedulingAlgoCode
                with open(filename + ".txt", "a") as f:
                    f.write("{rcvtime},r\n".format(rcvtime = newJobReceiveTime))
            if(workersID == 3):
                worker3Tasks += 1
                filename = filename + str(workersID) + "_" + schedulingAlgoCode
                with open(filename + ".txt", "a") as f:
                    f.write("{rcvtime},r\n".format(rcvtime = newJobReceiveTime))
            taskLists.append(jobRequest)
            thread_lock.release()

def performTask():
    global taskLists, worker1Tasks, worker2Tasks, worker3Tasks, thread_lock, workersID, startTime, workersID, schedulingAlgoCode
    while True:
        thread_lock.acquire()
        
        taskListLen = 0     
        for task in taskLists:
            taskListLen = taskListLen + 1

        #if(taskListLen > 0):
        #    print("executing tasks len : ", taskListLen, "\n")

        t = 0.4 - 0.06*(taskListLen**2)
        if(t < 0):
            t = 0.2
        time.sleep(t)
        index = 0 
        while(index < taskListLen):
            taskLists[index][2] = taskLists[index][2] - 1
            
            if taskLists[index][2] == 0:
                finishedTaskDetails = taskLists.pop(index)
                taskNum = str(finishedTaskDetails[1])
                jobNum = str(finishedTaskDetails[0])
                printTask = "Completed executing task " + taskNum
                printJob =" of job " + jobNum
                taskCompletionTime = datetime.datetime.now()
                
                filename = "logs_tasks_" + schedulingAlgoCode

                with open(filename + ".txt", "a") as f:
                    f.write("{jid}::{tid}::{end}::{etime}!!!\n".format(jid = finishedTaskDetails[0], tid = finishedTaskDetails[1], end = "e", etime = taskCompletionTime))
                
                newTaskCompletionTime = time.time() 
                filename = "logsTasks_" + schedulingAlgoCode

                with open(filename + ".txt", "a") as f:
                    f.write("{wid},completed:{tid},{etime}\n".format(wid = workersID, tid = finishedTaskDetails[1], etime = newTaskCompletionTime))
 
                print(taskCompletionTime, end = " ")
                print(printTask + printJob)
                
                filename = "tasks_per_worker_"
                if(workersID == 1):
                    worker1Tasks -= 1
                    filename = filename + str(workersID) + "_" + schedulingAlgoCode
                    with open(filename + ".txt", "a") as f:
                        f.write("{completiontime},c\n".format(completiontime = newTaskCompletionTime))
                if(workersID == 2):
                    worker2Tasks -= 1
                    filename = filename + str(workersID) + "_" + schedulingAlgoCode
                    with open(filename + ".txt", "a") as f:
                        f.write("{completiontime},c\n".format(completiontime = newTaskCompletionTime))
                if(workersID == 3):
                    worker3Tasks -= 1
                    filename = filename + str(workersID) + "_" + schedulingAlgoCode
                    with open(filename + ".txt", "a") as f:
                        f.write("{completiontime},c\n".format(completiontime = newTaskCompletionTime))
                
                TCPsocket=socket(AF_INET, SOCK_STREAM)
                TCPsocket.connect(('127.0.0.1',5001))

                finishedTaskDetails[2] = workersID
                stringfinishedTaskDetails = str(finishedTaskDetails)
                TCPsocket.send(stringfinishedTaskDetails.encode())
                TCPsocket.close()
                
                taskListLen = taskListLen - 1
                index -= 1
                
            index += 1
                

        thread_lock.release()
        

acceptJobFromMasterThread = threading.Thread(target = acceptRequest)
acceptJobFromMasterThread.start()

jobPerformThread = threading.Thread(target = performTask)
jobPerformThread.start()

acceptJobFromMasterThread.join()
jobPerformThread.join()
