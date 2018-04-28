# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='my_service.proto',
  package='handson',
  syntax='proto3',
  serialized_pb=_b('\n\x10my_service.proto\x12\x07handson\")\n\x0eInitialRequest\x12\x17\n\x0fnumber_of_pages\x18\x01 \x01(\x05\" \n\x0fInitialResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"\x1e\n\x0cQueryRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\"7\n\rQueryResponse\x12\x12\n\npage_names\x18\x01 \x03(\t\x12\x12\n\npage_count\x18\x02 \x03(\x03\">\n\tMyRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x10\n\x08\x66iletext\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\"?\n\nMyResponse\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x10\n\x08\x66iletext\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x32\x83\x02\n\tMyService\x12\x36\n\tMyMethod1\x12\x12.handson.MyRequest\x1a\x13.handson.MyResponse\"\x00\x12@\n\tMyMethod2\x12\x17.handson.InitialRequest\x1a\x18.handson.InitialResponse\"\x00\x12:\n\tMyMethod3\x12\x12.handson.MyRequest\x1a\x13.handson.MyResponse\"\x00(\x01\x30\x01\x12@\n\tMyMethod4\x12\x15.handson.QueryRequest\x1a\x16.handson.QueryResponse\"\x00(\x01\x30\x01\x42\x32\n\x18\x63om.alexandreesl.handsonB\x0eMyServiceProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_INITIALREQUEST = _descriptor.Descriptor(
  name='InitialRequest',
  full_name='handson.InitialRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number_of_pages', full_name='handson.InitialRequest.number_of_pages', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=70,
)


_INITIALRESPONSE = _descriptor.Descriptor(
  name='InitialResponse',
  full_name='handson.InitialResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='handson.InitialResponse.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=104,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='handson.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='handson.QueryRequest.offset', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=136,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='handson.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_names', full_name='handson.QueryResponse.page_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_count', full_name='handson.QueryResponse.page_count', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=193,
)


_MYREQUEST = _descriptor.Descriptor(
  name='MyRequest',
  full_name='handson.MyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='handson.MyRequest.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filetext', full_name='handson.MyRequest.filetext', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='handson.MyRequest.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=257,
)


_MYRESPONSE = _descriptor.Descriptor(
  name='MyResponse',
  full_name='handson.MyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='handson.MyResponse.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filetext', full_name='handson.MyResponse.filetext', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='handson.MyResponse.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=322,
)

DESCRIPTOR.message_types_by_name['InitialRequest'] = _INITIALREQUEST
DESCRIPTOR.message_types_by_name['InitialResponse'] = _INITIALRESPONSE
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['MyRequest'] = _MYREQUEST
DESCRIPTOR.message_types_by_name['MyResponse'] = _MYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitialRequest = _reflection.GeneratedProtocolMessageType('InitialRequest', (_message.Message,), dict(
  DESCRIPTOR = _INITIALREQUEST,
  __module__ = 'my_service_pb2'
  # @@protoc_insertion_point(class_scope:handson.InitialRequest)
  ))
_sym_db.RegisterMessage(InitialRequest)

InitialResponse = _reflection.GeneratedProtocolMessageType('InitialResponse', (_message.Message,), dict(
  DESCRIPTOR = _INITIALRESPONSE,
  __module__ = 'my_service_pb2'
  # @@protoc_insertion_point(class_scope:handson.InitialResponse)
  ))
_sym_db.RegisterMessage(InitialResponse)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYREQUEST,
  __module__ = 'my_service_pb2'
  # @@protoc_insertion_point(class_scope:handson.QueryRequest)
  ))
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYRESPONSE,
  __module__ = 'my_service_pb2'
  # @@protoc_insertion_point(class_scope:handson.QueryResponse)
  ))
_sym_db.RegisterMessage(QueryResponse)

MyRequest = _reflection.GeneratedProtocolMessageType('MyRequest', (_message.Message,), dict(
  DESCRIPTOR = _MYREQUEST,
  __module__ = 'my_service_pb2'
  # @@protoc_insertion_point(class_scope:handson.MyRequest)
  ))
_sym_db.RegisterMessage(MyRequest)

MyResponse = _reflection.GeneratedProtocolMessageType('MyResponse', (_message.Message,), dict(
  DESCRIPTOR = _MYRESPONSE,
  __module__ = 'my_service_pb2'
  # @@protoc_insertion_point(class_scope:handson.MyResponse)
  ))
_sym_db.RegisterMessage(MyResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030com.alexandreesl.handsonB\016MyServiceProtoP\001\242\002\003HLW'))

_MYSERVICE = _descriptor.ServiceDescriptor(
  name='MyService',
  full_name='handson.MyService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=325,
  serialized_end=584,
  methods=[
  _descriptor.MethodDescriptor(
    name='MyMethod1',
    full_name='handson.MyService.MyMethod1',
    index=0,
    containing_service=None,
    input_type=_MYREQUEST,
    output_type=_MYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MyMethod2',
    full_name='handson.MyService.MyMethod2',
    index=1,
    containing_service=None,
    input_type=_INITIALREQUEST,
    output_type=_INITIALRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MyMethod3',
    full_name='handson.MyService.MyMethod3',
    index=2,
    containing_service=None,
    input_type=_MYREQUEST,
    output_type=_MYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MyMethod4',
    full_name='handson.MyService.MyMethod4',
    index=3,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_QUERYRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MYSERVICE)

DESCRIPTOR.services_by_name['MyService'] = _MYSERVICE

# @@protoc_insertion_point(module_scope)