# coding:utf-8
from web3 import Web3, HTTPProvider
from web3.personal import Personal
from web3.auto import w3

infuraRopsten = HTTPProvider('https://ropsten.infura.io/CXduySaW5b61XIZBnh7Y')
etherscanRopsten = HTTPProvider('http://api-ropsten.etherscan.io')
etherscanKey = 'Q4XIJ8287JNPRUZG1WSBWB3H4YH1AIY6G7'
localAmd = HTTPProvider('http://192.168.1.33:8545')
LanUbuntu = HTTPProvider('http://192.168.1.22:8545')

wp3 = Web3([infuraRopsten])

ok_key = '91f155d4ca2474ab855a8e3a8b4213200b8d6639d147091dd66264cfc37491f8'

class web3test:

    def __init__(self):
        from eth_account import Account
        self.Jdata = '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0xB8DC8bD7005b6EeBced32F80C2a541CB864EB6ae", "latest"],"id":1}'
        w3.eth.enable_unaudited_features()
        print("web3 version is : ",wp3.version.api)
    def numbertest(self):
        print(Web3.toHex(9), Web3.sha3(0x23456))
        aA = wp3.eth.getBlock('latest')
        print(aA)

    def get_estimategas_etherscan(self):
        import requests
        print(wp3.eth.gasPrice)
        res = requests.get(
            "https://ropsten.etherscan.io/api?module=proxy&action=eth_estimateGas&to=0xf0160428a8552ac9bb7e050d90eeade4ddd52843&value=0xff22&gasPrice=0x051da038cc&gas=0xffffff&apikey=Q4XIJ8287JNPRUZG1WSBWB3H4YH1AIY6G7")
        value = eval(res.text)
        return int(value['result'],16)
    def getblocknumber(self):
        a = wp3.eth.blockNumber
        return a
    def getBalance(self,account="0x8aA4c17EA21804f7c27E2f0BB1444C7941171319"):
        print('%s 账户的金额'%account)
        a = wp3.eth.getBalance(account)
        return a
    def loadkey(self,file='88888'):
        with open(file) as keyfile:
            encrypted_key = keyfile.read()
            try:
                private_key = w3.eth.account.decrypt(encrypted_key,'yaozai1983')
                return Web3.toHex(private_key)
            except:
                print('解锁失败')
    def circle(self,ob=None):
        import time
        while 1:
            time.sleep(1)
            self.getBalance()
    def newAccount(self,passwd='123456'):    #不好使
        from web3.module import (
            Module,
        )
        a = Personal(Module)
        b = a.newAccount(password=passwd)
        return b

    def signTrans(self,target='0xaaD7CB0Ad13e4a77e95E03e8984f800e2e9695a4',key=''):
        key =self.loadkey()
        transaction = {'to': target,'value': 1000000000000000000,'gas': 2000000,'gasPrice': wp3.eth.gasPrice,'nonce': 0, 'chainId': 1}
        signed = w3.eth.account.signTransaction(transaction,key)
        return signed.rawTransaction
    def sendRawTransaction(self,from_add='0x8aA4c17EA21804f7c27E2f0BB1444C7941171319',pri_key=None,target=None,value=None):
        import rlp
        from ethereum.transactions import Transaction

        tx = Transaction(nonce=wp3.eth.getTransactionCount(from_add),gasprice=wp3.eth.gasPrice,startgas=100000,to=target,value=value,data=b'',)
        print('nonce 是', wp3.eth.getTransactionCount(from_add))
        tx.sign(pri_key)
        print ('生成tx ',tx)
        rawtx = rlp.encode(tx)
        print (rawtx)
        rawtx_hex = Web3.toHex(rawtx)
        print(rawtx_hex)
        wp3.eth.sendRawTransaction(rawtx_hex)
if __name__ == '__main__':
    tt = web3test()
    print(Web3.fromWei(tt.getBalance(),'ether'))
    #dir(Web3)
    re = tt.sendRawTransaction(pri_key=tt.loadkey(),target='0xaaD7CB0Ad13e4a77e95E03e8984f800e2e9695a4',value=1000000000000000000)
    print(re)

