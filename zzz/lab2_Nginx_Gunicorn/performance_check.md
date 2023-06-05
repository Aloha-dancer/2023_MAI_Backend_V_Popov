---- without proxy ----  
Running 10s test @ http://localhost:80
  10 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   126.91ms  261.18ms   1.46s    88.57%
    Req/Sec     1.26k     0.94k    7.34k    77.15%
  Latency Distribution
     50%   25.48ms
     75%   69.26ms
     90%  470.08ms
     99%    1.21s 
  122096 requests in 10.07s, 60.89MB read
Requests/sec:  12127.51
Transfer/sec:      6.05MB
---- with proxy ----  
Running 10s test @ http://localhost/api/
  10 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   128.66ms   49.87ms 363.20ms   71.41%
    Req/Sec   313.26    147.59   738.00     69.48%
  Latency Distribution
     50%  120.79ms
     75%  156.10ms
     90%  189.63ms
     99%  277.17ms
  31168 requests in 10.10s, 34.21MB read
Requests/sec:   3085.74
Transfer/sec:      3.39MB
