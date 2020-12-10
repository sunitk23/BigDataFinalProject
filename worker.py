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


schedulingAlgoCode = ""
fileWriteOnce = 0
workersID = int(sys.argv[2])
taskLists = list()
thread_lock = threading.Lock()
workersPort = int(sys.argv[1])


def acceptRequest():
    global taskLists, schedulingAlgoCode, fileWriteOnce, thread_lock 
    TCPsocket = socket(AF_INET, SOCK_STREAM)
    TCPsocket.bind(('127.0.0.1',workersPort))
    TCPsocket.listen(100)

    while True:
        conn,_= TCPsocket.accept()
        jobRequest = conn.recv(1024)

        if conn:
            #print(jobRequest.decode())
            jobRequest = jobRequest.decode()
            jobRequest, schedulingAlgoCode = jobRequest.split("::")
            jobRequest = literal_eval(jobRequest)
            filename = "logs_tasks_" + schedulingAlgoCode 

            jobReceiveTime = datetime.datetime.now()
            with open(filename + ".txt", "a+") as f:
                f.write("{jid}::{tid}::{s}::{stime}!!!\n".format(jid = jobRequest[0], tid = jobRequest[1], s = "s", stime = jobReceiveTime))

            jobNum = str(jobRequest[0])
            printJob = " of job " + jobNum
            taskNum = str(jobRequest[1])
            printTask = "Executing task "+ taskNum
            print(jobReceiveTime, end = " ")
            print(printTask + printJob)
            thread_lock.acquire()
            taskLists.append(jobRequest)
            #print(taskLists)
            thread_lock.release()

def performTask():
    global taskLists, thread_lock
    while True:
        thread_lock.acquire()
        taskListLen = 0
        for i in taskLists:
            taskListLen = taskListLen + 1
        #t = 0.4 - 0.01*len(taskLists)
        time.sleep(0.4)
        #for m in range(0,len(taskLists)):
        #taskListLen = len(taskLists)
        m = 0
        while (m<taskListLen):
            taskLists[m][2] = taskLists[m][2] - 1
            #print(taskLists)

            if taskLists[m][2] == 0:
            #print(taskLists[i])
                finishedTaskDetails = taskLists.pop(m)
                taskNum = str(finishedTaskDetails[1])
                jobNum = str(finishedTaskDetails[0])
                printTask = "Completed executing task " + taskNum
                printJob =" of job " + jobNum
                taskCompletionTime = datetime.datetime.now()
                
                filename = "logs_tasks_" + schedulingAlgoCode
                with open(filename + ".txt", "a") as f:
                    f.write("{jid}::{tid}::{end}::{etime}!!!\n".format(jid = finishedTaskDetails[0], tid = finishedTaskDetails[1], end = "e", etime = taskCompletionTime))
                print(taskCompletionTime, end = " ")
                print(printTask + printJob)
                TCPsocket=socket(AF_INET, SOCK_STREAM)
                TCPsocket.connect(('127.0.0.1',5001))

                finishedTaskDetails[2] = workersID
                stringfinishedTaskDetails = str(finishedTaskDetails)
                TCPsocket.send(stringfinishedTaskDetails.encode())
                TCPsocket.close()
                m -= 1
                taskListLen = taskListLen - 1
            m += 1
        thread_lock.release()
        

acceptMaster = threading.Thread(target = acceptRequest)
acceptMaster.start()

perform = threading.Thread(target = performTask)
perform.start()

acceptMaster.join ()
perform.join ()
