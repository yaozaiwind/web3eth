# coding:utf-8
from web3 import Web3, HTTPProvider

from web3.auto import w3
import json

infuraRopsten = HTTPProvider('https://ropsten.infura.io/CXduySaW5b61XIZBnh7Y')
etherscanRopsten = HTTPProvider('http://api-ropsten.etherscan.io')
etherscanKey = 'Q4XIJ8287JNPRUZG1WSBWB3H4YH1AIY6G7'
localAmd = HTTPProvider('http://192.168.1.33:8545')
LanUbuntu = HTTPProvider('http://192.168.1.22:8545')

wp3 = Web3([infuraRopsten])

ok_key = '91f155d4ca2474ab855a8e3a8b4213200b8d6639d147091dd66264cfc37491f8'
bbxRopsten = '0x21530a27E2be1f4E77171503D5255B8757A852A5'

class web3test:
    private_key = None
    def __init__(self):
        from web3.version import Version
        self.keyfile = '88888'
        self.keypasswd = 'yaozai1983'
        ver = Version(wp3)
        self.ethNet = ver.network
        self.Jdata = '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0xB8DC8bD7005b6EeBced32F80C2a541CB864EB6ae", "latest"],"id":1}'
        w3.eth.enable_unaudited_features()
        print("web3 version is : ", wp3.version.api)

    def numbertest(self):
        print(Web3.toHex(9), Web3.sha3(0x23456))
        aA = wp3.eth.getBlock('latest')
        print(aA)

    def get_estimategas_etherscan(self):
        import requests
        print(wp3.eth.gasPrice,'web3 属性价格')
        res = requests.get(
            "https://api-ropsten.etherscan.io/api?module=proxy&action=eth_estimateGas&to=0xf0160428a8552ac9bb7e050d90eeade4ddd52843&value=0xff22&gasPrice=0x051da038cc&gas=0xffffff&apikey=Q4XIJ8287JNPRUZG1WSBWB3H4YH1AIY6G7")
        value = eval(res.text)
        print(value,'etherscan 查询价格')
        res2 = requests.get("https://api-ropsten.etherscan.io/api?module=proxy&action=eth_gasPrice&apikey=YourApiKeyToken")
        etherscanGas = eval(res2.text)
        print(etherscanGas,type(etherscanGas),etherscanGas['result'],type(etherscanGas['result']))
        gas2 = wp3.toInt(hexstr=etherscanGas['result'])
        print(gas2)
        return int(value['result'], 16)

    def getblocknumber(self):
        a = wp3.eth.blockNumber
        return a

    def getListFromBlock(self,blocknum=wp3.eth.blockNumber):
        blockList = wp3.eth.getBlock(blocknum, full_transactions=True)
        return blockList['transactions']

    def getBalance(self, account="0x8aA4c17EA21804f7c27E2f0BB1444C7941171319"):
        print('%s 账户的金额' % account)
        a = wp3.eth.getBalance(account)
        return a

    def loadkey(self, file='88888',passwd='yaozai1983'):
        with open(file) as keyfile:
            encrypted_key = keyfile.read()
            try:
                private_key = w3.eth.account.decrypt(encrypted_key, passwd)
                return Web3.toHex(private_key)
            except:
                print('解锁失败')
                return None

    def getTansRes(self,hash):
        return wp3.eth.getTransactionReceipt(hash) # 通过hash 获取交易结果

    def newAccount(self, passwd='123456'):
        acc = w3.eth.account.create(passwd)
        acc_keystor = self.keyStoreGen(acc.privateKey,passwd)
        print (acc)
        return acc,acc_keystor

    def keyStoreGen(self,private_key,passwd='123456'):
        return w3.eth.account.encrypt(private_key,passwd)

    def signTrans(self, target='0xaaD7CB0Ad13e4a77e95E03e8984f800e2e9695a4', from_add='0x8aA4c17EA21804f7c27E2f0BB1444C7941171319',value =1000000000000000000,gas=2000000):
        key = self.private_key
        # chainId 见 chainID 文件
        transaction = {"to": target, "value": value, "gas": gas, "gasPrice": wp3.eth.gasPrice,
                       "nonce": wp3.eth.getTransactionCount(from_add), "chainId": int(self.ethNet),"data" : ""}
        signed = w3.eth.account.signTransaction(transaction, key)
        return (signed.rawTransaction)

    def sendRaw(self,rawdata):
        return wp3.toHex(wp3.eth.sendRawTransaction(rawdata))

    def sendRawTransaction(self, from_add='0x8aA4c17EA21804f7c27E2f0BB1444C7941171319', pri_key=None, target=None,value=None):
        import rlp
        from ethereum.transactions import Transaction

        tx = Transaction(nonce=wp3.eth.getTransactionCount(from_add), gasprice=wp3.eth.gasPrice, startgas=100000,
                         to=target, value=value, data=b'', )

        tx.sign(pri_key)
        print('生成tx ', tx)
        rawtx = rlp.encode(tx)
        print(rawtx)
        rawtx_hex = Web3.toHex(rawtx)
        print(rawtx_hex)
        a = wp3.eth.sendRawTransaction(rawtx_hex)
        return wp3.toHex(a)

    def pendingTrans(self):
        #infura  拒绝调用这个接口
        from web3.txpool import TxPool
        pool = TxPool(wp3)
        print('显示inspect',pool.inspect)
        print('显示status',pool.status)
        print('显示content',pool.content)

    def contract_Tans(self,fromacc ='0x8aA4c17EA21804f7c27E2f0BB1444C7941171319',toacc = "0xaaD7CB0Ad13e4a77e95E03e8984f800e2e9695a4",contract = bbxRopsten):
        from ethtoken.abi import EIP20_ABI
        coins = wp3.eth.contract(address = contract,abi=EIP20_ABI)
        balance = coins.functions.balanceOf(fromacc)
        print(balance)
        cointransTx =coins.functions.transfer(toacc,1000000000000000000,).buildTransaction\
            ({"chainId":self.ethNet,"gas": 70000,"gasPrice": wp3.eth.gasPrice,"nonce":wp3.eth.getTransactionCount(fromacc)})
        print(cointransTx)
        signed = w3.eth.account.signTransaction(cointransTx,self.private_key)
        print(signed.rawTransaction)
        print(signed.r)
        resTx = self.sendRaw(signed.rawTransaction)
        return resTx

    def tokenbalance(self,fromacc ='0x8aA4c17EA21804f7c27E2f0BB1444C7941171319',contract = bbxRopsten):
        from ethtoken.abi import EIP20_ABI
        coins = wp3.eth.contract(address = contract,abi=EIP20_ABI)
        balance = coins.functions.balanceOf(fromacc).call()
        print(balance)






if __name__ == '__main__':
    tt = web3test()
    tt.private_key=tt.loadkey()
    print(Web3.fromWei(tt.getBalance(), 'ether')) #账号余额

    #print(tt.getListFromBlock(),'块中所有内容')

#生成新账号，并保存到文件，文件名用公钥地址
    # acc ,keystore= tt.newAccount()
    # print(acc)
    # print(keystore)
    # with open(acc.address,'w') as f:
    #     f.write(json.dumps(keystore))


#  ethereum 库帮助生成签名信息发交易
  #   re = tt.sendRawTransaction(pri_key=tt.loadkey(),target='0xaaD7CB0Ad13e4a77e95E03e8984f800e2e9695a4',value=1000000000000000000)
  #   print(re)


 #用web3 发交易
    # key = tt.loadkey()
    # print (key,'账号')
    # a = tt.signTrans()
    # print(a)
    # r = tt.sendRaw(rawdata=a)
    # print(r)

    # res = tt.contract_Tans()
    # print(res,'收到的HASH')
    tt.tokenbalance()
