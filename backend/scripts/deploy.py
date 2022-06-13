from scripts.helpful_scripts import get_account
from brownie import PunkAlienPrincess, config, network
import os


def deploy_nft():
    account = get_account()

    # verfiying smart contract
    publish_source = config["networks"][network.show_active()]["verify"]

    print('deploying NFT contract ...')
    nft = PunkAlienPrincess.deploy(
        'PunkAlienPrincess',
        'PAP',
        'https://gateway.pinata.cloud/ipfs/QmNkA5TqeV8BTYmUQRntVF3bKwx51KNyd2A2WgQdVeeWSU/',
        'https://gateway.pinata.cloud/ipfs/QmNkA5TqeV8BTYmUQRntVF3bKwx51KNyd2A2WgQdVeeWSU/1.json',
        {"from": account},
        publish_source=publish_source
    )

    print(f'nft is deployed at {nft.address}')

    os.remove('address.txt')
    f = open('address.txt', 'a')
    f.write(f'nft deployed at {nft.address}')
    f.close()


def main():
    deploy_nft()
