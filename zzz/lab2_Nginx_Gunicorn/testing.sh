echo ---- without proxy ---- \ 
wrk -t 10 -c 400 -d10s --latency http://localhost:80 \ 
echo ---- with proxy ---- \ 
wrk -t 10 -c 400 -d10s --latency http://localhost/api/ \ 

