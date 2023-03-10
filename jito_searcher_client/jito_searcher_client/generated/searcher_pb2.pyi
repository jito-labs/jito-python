"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import bundle_pb2
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import packet_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class SlotList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SLOTS_FIELD_NUMBER: builtins.int
    @property
    def slots(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        slots: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["slots", b"slots"]) -> None: ...

global___SlotList = SlotList

@typing_extensions.final
class SendBundleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUNDLE_FIELD_NUMBER: builtins.int
    @property
    def bundle(self) -> bundle_pb2.Bundle: ...
    def __init__(
        self,
        *,
        bundle: bundle_pb2.Bundle | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bundle", b"bundle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bundle", b"bundle"]) -> None: ...

global___SendBundleRequest = SendBundleRequest

@typing_extensions.final
class SendBundleResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    """server uuid for the bundle"""
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["uuid", b"uuid"]) -> None: ...

global___SendBundleResponse = SendBundleResponse

@typing_extensions.final
class ProgramSubscriptionV0(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROGRAMS_FIELD_NUMBER: builtins.int
    @property
    def programs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        programs: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["programs", b"programs"]) -> None: ...

global___ProgramSubscriptionV0 = ProgramSubscriptionV0

@typing_extensions.final
class WriteLockedAccountSubscriptionV0(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        accounts: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts", b"accounts"]) -> None: ...

global___WriteLockedAccountSubscriptionV0 = WriteLockedAccountSubscriptionV0

@typing_extensions.final
class MempoolSubscription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROGRAM_V0_SUB_FIELD_NUMBER: builtins.int
    WLA_V0_SUB_FIELD_NUMBER: builtins.int
    @property
    def program_v0_sub(self) -> global___ProgramSubscriptionV0: ...
    @property
    def wla_v0_sub(self) -> global___WriteLockedAccountSubscriptionV0: ...
    def __init__(
        self,
        *,
        program_v0_sub: global___ProgramSubscriptionV0 | None = ...,
        wla_v0_sub: global___WriteLockedAccountSubscriptionV0 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["msg", b"msg", "program_v0_sub", b"program_v0_sub", "wla_v0_sub", b"wla_v0_sub"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["msg", b"msg", "program_v0_sub", b"program_v0_sub", "wla_v0_sub", b"wla_v0_sub"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["msg", b"msg"]) -> typing_extensions.Literal["program_v0_sub", "wla_v0_sub"] | None: ...

global___MempoolSubscription = MempoolSubscription

@typing_extensions.final
class PendingTxSubscriptionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """list of accounts to subscribe to
        NOTE: the block-engine will only forward transactions that write lock the provided accounts here.
        """
    def __init__(
        self,
        *,
        accounts: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts", b"accounts"]) -> None: ...

global___PendingTxSubscriptionRequest = PendingTxSubscriptionRequest

@typing_extensions.final
class PendingTxNotification(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_SIDE_TS_FIELD_NUMBER: builtins.int
    EXPIRATION_TIME_FIELD_NUMBER: builtins.int
    TRANSACTIONS_FIELD_NUMBER: builtins.int
    @property
    def server_side_ts(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """server-side timestamp the transactions were generated at (for debugging/profiling purposes)"""
    @property
    def expiration_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """expiration time of the packet"""
    @property
    def transactions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[packet_pb2.Packet]:
        """list of pending transactions"""
    def __init__(
        self,
        *,
        server_side_ts: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        expiration_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        transactions: collections.abc.Iterable[packet_pb2.Packet] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expiration_time", b"expiration_time", "server_side_ts", b"server_side_ts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expiration_time", b"expiration_time", "server_side_ts", b"server_side_ts", "transactions", b"transactions"]) -> None: ...

global___PendingTxNotification = PendingTxNotification

@typing_extensions.final
class NextScheduledLeaderRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___NextScheduledLeaderRequest = NextScheduledLeaderRequest

@typing_extensions.final
class NextScheduledLeaderResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CURRENT_SLOT_FIELD_NUMBER: builtins.int
    NEXT_LEADER_SLOT_FIELD_NUMBER: builtins.int
    NEXT_LEADER_IDENTITY_FIELD_NUMBER: builtins.int
    current_slot: builtins.int
    """the current slot the backend is on"""
    next_leader_slot: builtins.int
    """the slot and identity of the next leader"""
    next_leader_identity: builtins.str
    def __init__(
        self,
        *,
        current_slot: builtins.int = ...,
        next_leader_slot: builtins.int = ...,
        next_leader_identity: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["current_slot", b"current_slot", "next_leader_identity", b"next_leader_identity", "next_leader_slot", b"next_leader_slot"]) -> None: ...

global___NextScheduledLeaderResponse = NextScheduledLeaderResponse

@typing_extensions.final
class ConnectedLeadersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ConnectedLeadersRequest = ConnectedLeadersRequest

@typing_extensions.final
class ConnectedLeadersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ConnectedValidatorsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___SlotList: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___SlotList | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    CONNECTED_VALIDATORS_FIELD_NUMBER: builtins.int
    @property
    def connected_validators(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___SlotList]: ...
    def __init__(
        self,
        *,
        connected_validators: collections.abc.Mapping[builtins.str, global___SlotList] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["connected_validators", b"connected_validators"]) -> None: ...

global___ConnectedLeadersResponse = ConnectedLeadersResponse

@typing_extensions.final
class GetTipAccountsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetTipAccountsRequest = GetTipAccountsRequest

@typing_extensions.final
class GetTipAccountsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        accounts: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts", b"accounts"]) -> None: ...

global___GetTipAccountsResponse = GetTipAccountsResponse

@typing_extensions.final
class SubscribeBundleResultsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___SubscribeBundleResultsRequest = SubscribeBundleResultsRequest
