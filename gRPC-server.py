#!/usr/bin/env python3

from concurrent import futures
import logging
import math
import time
#############
import io
import argparse
import base64
from PIL import Image

import grpc
import lab6_pb2
import lab6_pb2_grpc

class lab6Servicer(lab6_pb2_grpc.Lab6ServServicer):
    """Implementation methods"""

    def add(self, request, context):
        # response = lab6_pb2.addReply()
        response = lab6_pb2.addReply()
        response.sum = request.a + request.b
        print(f"Add response: \n{response}")
        return response
        # pass

    def rawimage(self, request, context):
        r = request
        # Convert the data to a PIL image type so we can extract dimensions
        try:
            ioBuffer = io.BytesIO(r.img)
            img = Image.open(ioBuffer)

            response = lab6_pb2.imageReply(
                width = img.size[0],
                height = img.size[1],
            )
        except:
            response = lab6_pb2.imageReply(
                width = 0,
                height = 0,
            )        
        print(f"Raw response: \n{response}")
        return response

    def dotproduct(self, request, context):
        # data = request.get_json()
        a_list = request.a
        b_list = request.b
        val = 0
        for i in range(len(a_list)):
            val += a_list[i]*b_list[i]
        
        # response = {'dotproduct': str(val)}
        response = lab6_pb2.dotProductReply(
                dotproduct = val,
            )
        print(f"Dot response: \n{response}")
        return response

    def jsonimage(self, request, context):
        b64img = request.img
        img_bytes = base64.b64decode(b64img.encode("utf-8"))
        # Convert the data to a PIL image type so we can extract dimensions
        try:
            ioBuffer = io.BytesIO(img_bytes)
            img = Image.open(ioBuffer)

            response = lab6_pb2.imageReply(
                width = img.size[0],
                height = img.size[1],
            )
        except:
            response = lab6_pb2.imageReply(
                width = 0,
                height = 0,
            )
        print(f"Json response: \n{response}")
        return response
        # pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lab6_pb2_grpc.add_Lab6ServServicer_to_server(lab6Servicer(), server)
    server.add_insecure_port("[::]:5000")
    server.start()
    print('Starting server. Listening on port 5000.')
    server.wait_for_termination()

if __name__ == "__main__":
    serve()








