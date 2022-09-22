from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from brownie import network
import pytest


def test_can_deploy_and_create():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    account = get_account()
    advanced_collectible, tx = deploy_and_create()
    vrf_coordinator = get_contract("vrf_coordinator")
    random_number = 777
    request_id = tx.events["requestedCollectible"]["requestId"]
    tx = vrf_coordinator.callBackWithRandomness(
        request_id, random_number, advanced_collectible, {"from": account}
    )
    tx.wait(1)

    assert advanced_collectible.tokenCounter() == 1
    # assert tx.events["breedAssigned"]["breed"] == random_number % 3
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3
