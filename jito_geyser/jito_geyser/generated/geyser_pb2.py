# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geyser.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import confirmed_block_pb2 as confirmed__block__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cgeyser.proto\x12\rsolana.geyser\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x15\x63onfirmed_block.proto\"\xa9\x01\n\x14PartialAccountUpdate\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\x0e\n\x06pubkey\x18\x02 \x01(\x0c\x12\r\n\x05owner\x18\x03 \x01(\x0c\x12\x12\n\nis_startup\x18\x04 \x01(\x08\x12\x0b\n\x03seq\x18\x05 \x01(\x04\x12\x19\n\x0ctx_signature\x18\x06 \x01(\tH\x00\x88\x01\x01\x12\x17\n\x0freplica_version\x18\x07 \x01(\rB\x0f\n\r_tx_signature\"\xed\x01\n\rAccountUpdate\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\x0e\n\x06pubkey\x18\x02 \x01(\x0c\x12\x10\n\x08lamports\x18\x03 \x01(\x04\x12\r\n\x05owner\x18\x04 \x01(\x0c\x12\x15\n\ris_executable\x18\x05 \x01(\x08\x12\x12\n\nrent_epoch\x18\x06 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x07 \x01(\x0c\x12\x0b\n\x03seq\x18\x08 \x01(\x04\x12\x12\n\nis_startup\x18\t \x01(\x08\x12\x19\n\x0ctx_signature\x18\n \x01(\tH\x00\x88\x01\x01\x12\x17\n\x0freplica_version\x18\x0b \x01(\rB\x0f\n\r_tx_signature\"u\n\nSlotUpdate\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\x18\n\x0bparent_slot\x18\x02 \x01(\x04H\x00\x88\x01\x01\x12/\n\x06status\x18\x03 \x01(\x0e\x32\x1f.solana.geyser.SlotUpdateStatusB\x0e\n\x0c_parent_slot\"o\n\x15TimestampedSlotUpdate\x12&\n\x02ts\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\x0bslot_update\x18\x02 \x01(\x0b\x32\x19.solana.geyser.SlotUpdate\"x\n\x18TimestampedAccountUpdate\x12&\n\x02ts\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x0e\x61\x63\x63ount_update\x18\x02 \x01(\x0b\x32\x1c.solana.geyser.AccountUpdate\"$\n\"SubscribeTransactionUpdatesRequest\"\x1e\n\x1cSubscribeBlockUpdatesRequest\"\x91\x01\n\x19MaybePartialAccountUpdate\x12\x45\n\x16partial_account_update\x18\x01 \x01(\x0b\x32#.solana.geyser.PartialAccountUpdateH\x00\x12&\n\x02hb\x18\x02 \x01(\x0b\x32\x18.solana.geyser.HeartbeatH\x00\x42\x05\n\x03msg\"\x0b\n\tHeartbeat\"\x0e\n\x0c\x45mptyRequest\"\xc2\x01\n\x0b\x42lockUpdate\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\x11\n\tblockhash\x18\x02 \x01(\t\x12\x36\n\x07rewards\x18\x03 \x03(\x0b\x32%.solana.storage.ConfirmedBlock.Reward\x12.\n\nblock_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x0c\x62lock_height\x18\x05 \x01(\x04H\x00\x88\x01\x01\x42\x0f\n\r_block_height\"r\n\x16TimestampedBlockUpdate\x12&\n\x02ts\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x62lock_update\x18\x02 \x01(\x0b\x32\x1a.solana.geyser.BlockUpdate\"\x96\x01\n\x11TransactionUpdate\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\x11\n\tsignature\x18\x02 \x01(\t\x12\x0f\n\x07is_vote\x18\x03 \x01(\x08\x12\x0e\n\x06tx_idx\x18\x04 \x01(\x04\x12?\n\x02tx\x18\x05 \x01(\x0b\x32\x33.solana.storage.ConfirmedBlock.ConfirmedTransaction\"}\n\x1cTimestampedTransactionUpdate\x12&\n\x02ts\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x0btransaction\x18\x02 \x01(\x0b\x32 .solana.geyser.TransactionUpdate\"\x1c\n\x1aSubscribeSlotUpdateRequest\"2\n\x1eSubscribeAccountUpdatesRequest\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0c\"3\n\x1fSubscribeProgramsUpdatesRequest\x12\x10\n\x08programs\x18\x01 \x03(\x0c\"C\n%SubscribePartialAccountUpdatesRequest\x12\x1a\n\x12skip_vote_accounts\x18\x01 \x01(\x08\"=\n\x1cGetHeartbeatIntervalResponse\x12\x1d\n\x15heartbeat_interval_ms\x18\x01 \x01(\x04*<\n\x10SlotUpdateStatus\x12\r\n\tCONFIRMED\x10\x00\x12\r\n\tPROCESSED\x10\x01\x12\n\n\x06ROOTED\x10\x02\x32\xc4\x06\n\x06Geyser\x12\x62\n\x14GetHeartbeatInterval\x12\x1b.solana.geyser.EmptyRequest\x1a+.solana.geyser.GetHeartbeatIntervalResponse\"\x00\x12u\n\x17SubscribeAccountUpdates\x12-.solana.geyser.SubscribeAccountUpdatesRequest\x1a\'.solana.geyser.TimestampedAccountUpdate\"\x00\x30\x01\x12v\n\x17SubscribeProgramUpdates\x12..solana.geyser.SubscribeProgramsUpdatesRequest\x1a\'.solana.geyser.TimestampedAccountUpdate\"\x00\x30\x01\x12\x84\x01\n\x1eSubscribePartialAccountUpdates\x12\x34.solana.geyser.SubscribePartialAccountUpdatesRequest\x1a(.solana.geyser.MaybePartialAccountUpdate\"\x00\x30\x01\x12k\n\x14SubscribeSlotUpdates\x12).solana.geyser.SubscribeSlotUpdateRequest\x1a$.solana.geyser.TimestampedSlotUpdate\"\x00\x30\x01\x12\x81\x01\n\x1bSubscribeTransactionUpdates\x12\x31.solana.geyser.SubscribeTransactionUpdatesRequest\x1a+.solana.geyser.TimestampedTransactionUpdate\"\x00\x30\x01\x12o\n\x15SubscribeBlockUpdates\x12+.solana.geyser.SubscribeBlockUpdatesRequest\x1a%.solana.geyser.TimestampedBlockUpdate\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'geyser_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SLOTUPDATESTATUS._serialized_start=1960
  _SLOTUPDATESTATUS._serialized_end=2020
  _PARTIALACCOUNTUPDATE._serialized_start=88
  _PARTIALACCOUNTUPDATE._serialized_end=257
  _ACCOUNTUPDATE._serialized_start=260
  _ACCOUNTUPDATE._serialized_end=497
  _SLOTUPDATE._serialized_start=499
  _SLOTUPDATE._serialized_end=616
  _TIMESTAMPEDSLOTUPDATE._serialized_start=618
  _TIMESTAMPEDSLOTUPDATE._serialized_end=729
  _TIMESTAMPEDACCOUNTUPDATE._serialized_start=731
  _TIMESTAMPEDACCOUNTUPDATE._serialized_end=851
  _SUBSCRIBETRANSACTIONUPDATESREQUEST._serialized_start=853
  _SUBSCRIBETRANSACTIONUPDATESREQUEST._serialized_end=889
  _SUBSCRIBEBLOCKUPDATESREQUEST._serialized_start=891
  _SUBSCRIBEBLOCKUPDATESREQUEST._serialized_end=921
  _MAYBEPARTIALACCOUNTUPDATE._serialized_start=924
  _MAYBEPARTIALACCOUNTUPDATE._serialized_end=1069
  _HEARTBEAT._serialized_start=1071
  _HEARTBEAT._serialized_end=1082
  _EMPTYREQUEST._serialized_start=1084
  _EMPTYREQUEST._serialized_end=1098
  _BLOCKUPDATE._serialized_start=1101
  _BLOCKUPDATE._serialized_end=1295
  _TIMESTAMPEDBLOCKUPDATE._serialized_start=1297
  _TIMESTAMPEDBLOCKUPDATE._serialized_end=1411
  _TRANSACTIONUPDATE._serialized_start=1414
  _TRANSACTIONUPDATE._serialized_end=1564
  _TIMESTAMPEDTRANSACTIONUPDATE._serialized_start=1566
  _TIMESTAMPEDTRANSACTIONUPDATE._serialized_end=1691
  _SUBSCRIBESLOTUPDATEREQUEST._serialized_start=1693
  _SUBSCRIBESLOTUPDATEREQUEST._serialized_end=1721
  _SUBSCRIBEACCOUNTUPDATESREQUEST._serialized_start=1723
  _SUBSCRIBEACCOUNTUPDATESREQUEST._serialized_end=1773
  _SUBSCRIBEPROGRAMSUPDATESREQUEST._serialized_start=1775
  _SUBSCRIBEPROGRAMSUPDATESREQUEST._serialized_end=1826
  _SUBSCRIBEPARTIALACCOUNTUPDATESREQUEST._serialized_start=1828
  _SUBSCRIBEPARTIALACCOUNTUPDATESREQUEST._serialized_end=1895
  _GETHEARTBEATINTERVALRESPONSE._serialized_start=1897
  _GETHEARTBEATINTERVALRESPONSE._serialized_end=1958
  _GEYSER._serialized_start=2023
  _GEYSER._serialized_end=2859
# @@protoc_insertion_point(module_scope)
