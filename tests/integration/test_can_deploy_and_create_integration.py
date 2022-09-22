from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from brownie import network
import pytest
import time


def test_can_deploy_and_create_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    # account = get_account()
    advanced_collectible, tx = deploy_and_create()
    time.sleep(300)

    assert advanced_collectible.tokenCounter() == 1
