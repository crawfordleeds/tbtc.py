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
            raise Exception("")

        self.depositFactory = depositFactory
        self.config = config
