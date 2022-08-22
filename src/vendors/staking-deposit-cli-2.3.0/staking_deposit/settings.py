from typing import Dict, NamedTuple


DEPOSIT_CLI_VERSION = '2.3.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes


MAINNET = 'mainnet'
TESTNET = 'testnet'
DEVNET = 'devnet'


# Mainnet setting
MainnetSetting = BaseChainSetting(NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'))
# Testnet setting
TestnetSetting = BaseChainSetting(NETWORK_NAME=TESTNET, GENESIS_FORK_VERSION=bytes.fromhex('00001000'))
# Devnet setting
DevnetSetting = BaseChainSetting(NETWORK_NAME=DEVNET, GENESIS_FORK_VERSION=bytes.fromhex('00002000'))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    TESTNET: TestnetSetting,
    DEVNET: DevnetSetting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]
