BD project YACS

To run the files, execute in the following order :-

1. Open 5 terminals 
2. Run the master.py file as python3 master.py config.json <Scheduling_algorithm> on the 1st terminal
3. Run the worker.py file on 3 separate terminals for the 3 separate workers as: 
4. python3 worker.py 4500 1
5. python3 worker.py 4501 2
6. python3 worker.py 4502 3
7. Run the requests_eval.py file as python3 requests_eval.py <no_of_requests> on the 5th terminal and then enter the inter arrival time, number of mappers and reducers and duration.
8. Open another terminal and run the following command to observe the log analysis and graph analysis:
9. python3 analysis.py 

