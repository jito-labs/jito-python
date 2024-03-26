from solana.transaction import Transaction
from solders.transaction import VersionedTransaction

from jito_searcher_client.generated.packet_pb2 import Meta, Packet


def versioned_tx_to_protobuf_packet(tx: VersionedTransaction) -> Packet:
    """
    Converts a versioned transaction to a packet
    Note: setting packet.meta.size is required, the rest are optional
    """
    return Packet(
        data=bytes(tx),
        meta=Meta(size=len(bytes(tx)), addr="0.0.0.0", port=0, flags=None, sender_stake=0),
    )


def tx_to_protobuf_packet(tx: Transaction) -> Packet:
    """
    Converts a transaction to a packet
    Note: setting packet.meta.size is required, the rest are optional
    """
    return Packet(
        data=tx.serialize(),
        meta=Meta(size=len(tx.serialize()), addr="0.0.0.0", port=0, flags=None, sender_stake=0),
    )
