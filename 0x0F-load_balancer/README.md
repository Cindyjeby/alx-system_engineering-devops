LOAD BALANCER

-> This distributes the workload ofyour system to multiple individual systems or group of systems to reduce the amount of loadon an individual system.

1. Weighted scheduling algorithm
work is assigned to the server according to thr weight assigned to the server.
so in shoert if there are 10 requests directed to 4 servers , say server 1 has weight 2 then it receives 2 requests, server 2 has weight 3 hence receives 3 requests.

2. Round robin scheduling
requests are served by the server sequentially one after another.after sending the request to the last server it starts from the first server again.

3. Least connection first scheduling
requests are served first to the server which is currently handling least number of persistent connections
