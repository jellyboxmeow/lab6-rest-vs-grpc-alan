#!/usr/bin/env python3


import time
import io
import argparse
import base64

import requests
import json
import time
import base64
import random
import argparse

import grpc
import lab6_pb2
import lab6_pb2_grpc

####################################################################

def make_add_msg(num1, num2):
    return lab6_pb2.addMsg(
        a = num1,
        b = num2,
    )

def make_raw_msg():
    img_val = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    return lab6_pb2.rawImageMsg(
        img = img_val,
    )

def make_dot_msg():
    length = 100
    a_list = [random.random() for i in range(length)]
    b_list = [random.random() for i in range(length)]
    return lab6_pb2.dotProductMsg(
        a = a_list,
        b = b_list,
    )

def make_json_msg():
    img = base64.b64encode(open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read())
    img_val = img.decode("utf-8")
    return lab6_pb2.jsonImageMsg(
        img = img_val,
    )

####################################################################


def doAdd(addr, debug=False):
    # with grpc.insecure_channel(addr) as channel:
    #     stub = lab6_pb2_grpc.Lab6ServStub(channel)
    add_msg = make_add_msg(5, 10)
    add_reply = stub.add(add_msg)
    if debug:
        print(f"Add message worked, got {add_reply.sum} as response")

def doRawImage(addr, debug=False):
    # with grpc.insecure_channel(addr) as channel:
    #     stub = lab6_pb2_grpc.Lab6ServStub(channel)
    rawImage_msg = make_raw_msg()
    raw_imageReply = stub.rawimage(rawImage_msg)
    if debug:
        print(f"Raw Image message worked, got w: {raw_imageReply.width}, h: {raw_imageReply.height}")

def doDotProduct(addr, debug=False):
    # with grpc.insecure_channel(addr) as channel:
    #     stub = lab6_pb2_grpc.Lab6ServStub(channel)
    dot_msg = make_dot_msg()
    dot_reply = stub.dotproduct(dot_msg)
    if debug:
        print(f"Dot message worked got {dot_reply.dotproduct} as response")


def doJsonImage(addr, debug=False):
    # with grpc.insecure_channel(addr) as channel:
    #     stub = lab6_pb2_grpc.Lab6ServStub(channel)
    jsonImage_msg = make_json_msg()
    json_imageReply = stub.jsonimage(jsonImage_msg)
    if debug:
        print(f"Json Image message worked, got w: {json_imageReply.width}, h: {json_imageReply.height}")

# def run():
#     with grpc.insecure_channel("localhost:5000") as channel:
#         stub = lab6_pb2_grpc.Lab6ServStub(channel)
#         print("----------Add----------")
#         add_msg = make_add_msg(5, 10)
#         add_reply = stub.add(add_msg)
#         if add_reply is not None:
#             print(f"Add message worked got {add_reply.sum} as response")
        
#         print("\n----------Raw Image----------")
#         rawImage_msg = make_raw_msg()
#         raw_imageReply = stub.rawimage(rawImage_msg)
#         if raw_imageReply is not None:
#             print(f"Raw Image message worked, got w: {raw_imageReply.width}, h: {raw_imageReply.height}")

#         print("\n----------Dot Product----------")
#         dot_msg = make_dot_msg()
#         dot_reply = stub.dotproduct(dot_msg)
#         if dot_reply is not None:
#             print(f"Dot message worked got {dot_reply.dotproduct} as response")
        
#         print("\n----------Json Image----------")
#         jsonImage_msg = make_json_msg()
#         json_imageReply = stub.jsonimage(jsonImage_msg)
#         if json_imageReply is not None:
#             print(f"Json Image message worked, got w: {json_imageReply.width}, h: {json_imageReply.height}")

# if __name__ == "__main__":
#     run()

# ---------------------------------------------------------
# Parse command-line arguments
# ---------------------------------------------------------

parser = argparse.ArgumentParser(
    description='gRPC client for measuring server operations'
)

parser.add_argument(
    'host',
    help='IP address or hostname of the gRPC server'
)

parser.add_argument(
    'cmd',
    choices=['add', 'rawImage', 'dotProduct', 'jsonImage'],
    help='Operation to perform'
)

parser.add_argument(
    'reps',
    type=int,
    help='Number of repetitions for measurement'
)

parser.add_argument(
    '-p', '--port',
    type=int,
    default=5000,
    help='Server port (default: 5000)'
)

parser.add_argument(
    '-d', '--debug',
    action='store_true',
    help='Print the response from the server'
)

args = parser.parse_args()


# ---------------------------------------------------------
# Build server address
# ---------------------------------------------------------

# MODIFIED
addr = f"{args.host}:{args.port}"

print(f"Running {args.reps} reps against {addr}")

channel = grpc.insecure_channel(addr)
stub = lab6_pb2_grpc.Lab6ServStub(channel)

# ---------------------------------------------------------
# Perform requested operation
# ---------------------------------------------------------

if args.cmd == 'rawImage':

    start = time.perf_counter()

    for x in range(args.reps):
        doRawImage(addr, debug=args.debug)

    delta = ((time.perf_counter() - start) / args.reps) * 1000
    print("Took", delta, "ms per operation")


elif args.cmd == 'add':

    start = time.perf_counter()

    for x in range(args.reps):
        doAdd(addr, debug=args.debug)

    delta = ((time.perf_counter() - start) / args.reps) * 1000
    print("Took", delta, "ms per operation")


elif args.cmd == 'jsonImage':

    start = time.perf_counter()

    for x in range(args.reps):
        doJsonImage(addr, debug=args.debug)

    delta = ((time.perf_counter() - start) / args.reps) * 1000
    print("Took", delta, "ms per operation")


elif args.cmd == 'dotProduct':

    start = time.perf_counter()

    for x in range(args.reps):
        doDotProduct(addr, debug=args.debug)

    delta = ((time.perf_counter() - start) / args.reps) * 1000
    print("Took", delta, "ms per operation")

channel.close()
