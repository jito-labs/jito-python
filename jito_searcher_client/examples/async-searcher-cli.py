import asyncio
import time
from typing import List

import click
from grpc._cython.cygrpc import _AioCall
from grpc.aio import UnaryStreamCall
from solana.rpc.api import Client
from solana.rpc.commitment import Processed
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.system_program import TransferParams, transfer
from solders.transaction import Transaction, VersionedTransaction
from spl.memo.instructions import MemoParams, create_memo

from jito_searcher_client.async_searcher import get_async_searcher_client
from jito_searcher_client.convert import tx_to_protobuf_packet
from jito_searcher_client.generated.bundle_pb2 import Bundle
from jito_searcher_client.generated.searcher_pb2 import (
    ConnectedLeadersRequest,
    GetTipAccountsRequest,
    MempoolSubscription,
    NextScheduledLeaderRequest,
    NextScheduledLeaderResponse,
    PendingTxSubscriptionRequest,
    ProgramSubscriptionV0,
    SendBundleRequest,
    WriteLockedAccountSubscriptionV0,
)
from jito_searcher_client.generated.searcher_pb2_grpc import SearcherServiceStub

event_loop = asyncio.new_event_loop()


@click.group("cli")
@click.pass_context
@click.option(
    "--keypair-path",
    help="Path to a keypair that is authenticated with the block engine.",
    required=True,
)
@click.option(
    "--block-engine-url",
    help="Block Engine URL",
    required=True,
)
def cli(
    ctx,
    keypair_path: str,
    block_engine_url: str,
):
    """
    This script can be used to interface with the block engine as a jito_searcher_client.
    """
    with open(keypair_path) as kp_path:
        kp = Keypair.from_json(kp_path.read())
    ctx.obj = event_loop.run_until_complete(get_async_searcher_client(block_engine_url, kp))


@click.command("mempool-accounts")
@click.pass_obj
@click.argument("accounts", required=True, nargs=-1)
def mempool_accounts(client: SearcherServiceStub, accounts: List[str]):
    """
    Stream mempool transactions that write lock any of the provided accounts
    """
    leader: NextScheduledLeaderResponse = event_loop.run_until_complete(
        client.GetNextScheduledLeader(NextScheduledLeaderRequest())
    )
    print(
        f"next scheduled leader is {leader.next_leader_identity} in {leader.next_leader_slot - leader.current_slot} slots"
    )

    stream = client.SubscribeMempool(
        MempoolSubscription(wla_v0_sub=WriteLockedAccountSubscriptionV0(accounts=accounts))
    )
    while True:
        response = event_loop.run_until_complete(stream.read())
        print(response)


@click.command("mempool-programs")
@click.pass_obj
@click.argument("programs", required=True, nargs=-1)
def mempool_programs(client: SearcherServiceStub, programs: List[str]):
    """
    Stream mempool transactions that mention any of the provided programs
    """
    leader: NextScheduledLeaderResponse = event_loop.run_until_complete(
        client.GetNextScheduledLeader(NextScheduledLeaderRequest())
    )
    print(
        f"next scheduled leader is {leader.next_leader_identity} in {leader.next_leader_slot - leader.current_slot} slots"
    )

    stream = client.SubscribeMempool(MempoolSubscription(program_v0_sub=ProgramSubscriptionV0(programs=programs)))
    while True:
        response = event_loop.run_until_complete(stream.read())
        print(response)


@click.command("next-scheduled-leader")
@click.pass_obj
def next_scheduled_leader(client: SearcherServiceStub):
    """
    Find information on the next scheduled leader.
    """
    next_leader = event_loop.run_until_complete(client.GetNextScheduledLeader(NextScheduledLeaderRequest()))
    print(f"{next_leader=}")


@click.command("connected-leaders")
@click.pass_obj
def connected_leaders(client: SearcherServiceStub):
    """
    Get leaders connected to this block engine.
    """
    leaders = event_loop.run_until_complete(client.GetConnectedLeaders(ConnectedLeadersRequest()))
    print(f"{leaders=}")


@click.command("tip-accounts")
@click.pass_obj
def tip_accounts(client: SearcherServiceStub):
    """
    Get the tip accounts from the block engine.
    """
    accounts = event_loop.run_until_complete(client.GetTipAccounts(GetTipAccountsRequest()))
    print(f"{accounts=}")


if __name__ == "__main__":
    cli.add_command(mempool_accounts)
    cli.add_command(mempool_programs)
    cli.add_command(next_scheduled_leader)
    cli.add_command(connected_leaders)
    cli.add_command(tip_accounts)
    cli()
