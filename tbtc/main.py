from tbtc import BitcoinHelpers


def isMainnet(web3):
    return web3.net.version == "1"


def isTestnet(web3):
    return not isMainnet(web3)


class TBTC(object):

    satoshisPerTbtc = 10 ** 10

    def __init__(self, depositFactory, config, networkMatchCheck=True):
        """"""
        if networkMatchCheck and (
            (
                (
                    isMainnet(config.web3)
                    and config.bitcoinNetwork == BitcoinHelpers.Network.TESTNET
                )
                or (
                    isTestnet(config.web3)
                    and config.bitcoinNetwork == BitcoinHelpers.Network.MAINNET
                )
            )
        ):
            raise Exception(
                f"""Ethereum network {config.web3.net.version} and Bitcoin network {config.bitcoinNetwork} are not both
                on testnet or both on  mainnet. Quitting while we're ahead. Developers can also pass false as the
                networkMatchCheck parameter to suppress this error.
                """
            )

        self.depositFactory = depositFactory
        self.config = config
