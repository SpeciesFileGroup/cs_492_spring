# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import my_service_pb2 as my__service__pb2


class MyServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.MyMethod1 = channel.unary_unary(
        '/handson.MyService/MyMethod1',
        request_serializer=my__service__pb2.MyRequest.SerializeToString,
        response_deserializer=my__service__pb2.MyResponse.FromString,
        )
    self.MyMethod2 = channel.unary_unary(
        '/handson.MyService/MyMethod2',
        request_serializer=my__service__pb2.InitialRequest.SerializeToString,
        response_deserializer=my__service__pb2.InitialResponse.FromString,
        )
    self.MyMethod3 = channel.stream_stream(
        '/handson.MyService/MyMethod3',
        request_serializer=my__service__pb2.MyRequest.SerializeToString,
        response_deserializer=my__service__pb2.MyResponse.FromString,
        )
    self.MyMethod4 = channel.stream_stream(
        '/handson.MyService/MyMethod4',
        request_serializer=my__service__pb2.QueryRequest.SerializeToString,
        response_deserializer=my__service__pb2.QueryResponse.FromString,
        )


class MyServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def MyMethod1(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MyMethod2(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MyMethod3(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MyMethod4(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MyServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'MyMethod1': grpc.unary_unary_rpc_method_handler(
          servicer.MyMethod1,
          request_deserializer=my__service__pb2.MyRequest.FromString,
          response_serializer=my__service__pb2.MyResponse.SerializeToString,
      ),
      'MyMethod2': grpc.unary_unary_rpc_method_handler(
          servicer.MyMethod2,
          request_deserializer=my__service__pb2.InitialRequest.FromString,
          response_serializer=my__service__pb2.InitialResponse.SerializeToString,
      ),
      'MyMethod3': grpc.stream_stream_rpc_method_handler(
          servicer.MyMethod3,
          request_deserializer=my__service__pb2.MyRequest.FromString,
          response_serializer=my__service__pb2.MyResponse.SerializeToString,
      ),
      'MyMethod4': grpc.stream_stream_rpc_method_handler(
          servicer.MyMethod4,
          request_deserializer=my__service__pb2.QueryRequest.FromString,
          response_serializer=my__service__pb2.QueryResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'handson.MyService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
