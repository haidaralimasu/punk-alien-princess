from brownie import HumanTimeCry


def main():
    # nft = HumanTimeCry.at("0x22d276433b3b3566baef76700E7dD054421981Eb")
    nft = HumanTimeCry.at("0x22d276433b3b3566baef76700E7dD054421981Eb")
    HumanTimeCry.publish_source(nft)
