
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|
|   REST add	|   2.159ms	|   2.788ms	|  	328.525ms |
|   gRPC add	|   0.851ms	|   1.352ms	|   183.497ms 	|
|   REST rawimg	|   9.733ms	|   13.917ms|   1303.267ms	|
|   gRPC rawimg	|   7.922ms |   14.526ms|   229.979ms	|
|   REST dotproduct	|   2.477ms	|   4.128ms	|  335.526ms	|
|   gRPC dotproduct	|   0.939ms	|   1.446ms	|  164.323ms |
|   REST jsonimg	|   26.715ms|   43.138ms|  1528.700ms|
|   gRPC jsonimg	|   35.006ms|   46.907ms|  242.656ms|
|   PING        |  0.035ms   |  0.329ms   |   177.749ms   |

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.

## Short paragraph 
The performance difference between REST and gRPC is super noticable as we move the server-client systems further and further apart. Through it all gRPC is on average faster than REST for most actions. The only times that gRPC seems to struggle is sending large amounts of raw data or string data (jsonImage benchmark). However this elevated thanks to gRPC making a single TCP connection for all of its queries instead of making a new connection for each query as REST does.

## Test 1 - Local

As expected for the local test, it had the fastest times for every type of query out of the three test we ran. This makes sense since the device does not have to go through any other systems to get from the server to client or client to server. Between REST and gRPC, gRPC notably was faster than REST but that makes sense since gRPC can use the same TCP connection where as rest has to open up one for every query. The only exception being the jsonImage benchmark, this could be due to a multitude of things but one thing could be sending large string files could block or stall the serialized stream.

## Test 2 - Same Zone

For the same zone test, this was the average of the tests. Here we saw that things took a little longer but that could be due to the latency without the RPC or python overhead. The messages and responses had to take a couple of jumps before reaching another system. But not too many where it would take a while. 

## Test 3 - Different Region

For the final test, this was the most extreme of the tests and shows the issues with high latency. However, this also shows the benefits of gRPC compared to REST. As in this case, we saw gRPC way outperform REST in every action, this was definitely due to the fact that gRPC only opens one TCP connection for all its queries compared to REST opening one for every query.
