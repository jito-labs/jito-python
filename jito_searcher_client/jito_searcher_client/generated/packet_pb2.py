# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: packet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cpacket.proto\x12\x06packet\".\n\x0bPacketBatch\x12\x1f\n\x07packets\x18\x01 \x03(\x0b\x32\x0e.packet.Packet\"2\n\x06Packet\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x1a\n\x04meta\x18\x02 \x01(\x0b\x32\x0c.packet.Meta\"j\n\x04Meta\x12\x0c\n\x04size\x18\x01 \x01(\x04\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\"\n\x05\x66lags\x18\x04 \x01(\x0b\x32\x13.packet.PacketFlags\x12\x14\n\x0csender_stake\x18\x05 \x01(\x04\"p\n\x0bPacketFlags\x12\x0f\n\x07\x64iscard\x18\x01 \x01(\x08\x12\x11\n\tforwarded\x18\x02 \x01(\x08\x12\x0e\n\x06repair\x18\x03 \x01(\x08\x12\x16\n\x0esimple_vote_tx\x18\x04 \x01(\x08\x12\x15\n\rtracer_packet\x18\x05 \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'packet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PACKETBATCH._serialized_start=24
  _PACKETBATCH._serialized_end=70
  _PACKET._serialized_start=72
  _PACKET._serialized_end=122
  _META._serialized_start=124
  _META._serialized_end=230
  _PACKETFLAGS._serialized_start=232
  _PACKETFLAGS._serialized_end=344
# @@protoc_insertion_point(module_scope)
