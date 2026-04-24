import grpc
from concurrent import futures
import os

import payload_pb2
import payload_pb2_grpc

from shared_logic import process_request_grpc


class Service(payload_pb2_grpc.ServiceServicer):

    def Process(self, request, context):
        result = process_request_grpc(
            request.user,
            request.events
        )
        return payload_pb2.Response(result=result)


def serve():
    max_workers = os.cpu_count() or 4

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=max_workers),
        options=[
            ("grpc.max_concurrent_streams", 1000),
            ("grpc.keepalive_time_ms", 10000),
            ("grpc.keepalive_timeout_ms", 5000),
        ]
    )

    payload_pb2_grpc.add_ServiceServicer_to_server(Service(), server)

    server.add_insecure_port("127.0.0.1:50051")

    server.start()
    print(f"gRPC server running with {max_workers} workers")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()