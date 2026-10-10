
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|
|   REST add	|   6.159ms	|   2.788ms	|  	328.525ms |
|   gRPC add	|   1.727ms	|   2.817ms	|   488.789ms 	|
|   REST rawimg	|   9.733ms	|   13.917ms|   1303.267ms	|
|   gRPC rawimg	|   10.022ms|   24.651ms|   1502.016ms	|
|   REST dotproduct	|   2.477ms	|   4.128ms	|  335.526ms	|
|   gRPC dotproduct	|   1.892ms	|   2.798ms	|  484.414ms |
|   REST jsonimg	|   26.715ms|   43.138ms|  1528.700ms|
|   gRPC jsonimg	|   75.555ms|   47.854ms|  1646.584ms|
|   PING        |  0.035ms   |  0.329ms   |   177.749ms   |

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.