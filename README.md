BD project YACS

To run the files, execute in the following order :-

1. Open 5 terminals 
2. Run the master.py file as python3 master.py /path/to/config.json <Scheduling_algorithm> on the 1st terminal
3. Run the 3 worker.py files as python3 worker.py <worker_port_no> <worker_id>
4. Run the requests_eval.py file as python3 requests_eval.py <no_of_requests> and then enter the inter arrival time, number of mappers and reducers and duration.
5. Open another terminal and run the following commands to observe the log analysis and graph analysis:
    python3 logAnalysis.py > logAnalysis.txt
    python3 graphAnalysis.py 
    python3 graphAnalysis2.py
