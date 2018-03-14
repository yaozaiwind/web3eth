# coding:utf-8
import requests,json,testrpc
from web3 import Web3, HTTPProvider,TestRPCProvider,IPCProvider

provider = HTTPProvider('https://ropsten.infura.io/CXduySaW5b61XIZBnh7Y')

web3 = Web3(HTTPProvider("192.168.1.33:8545"))
eth_p = Web3(HTTPProvider('https://ropsten.infura.io/CXduySaW5b61XIZBnh7Y'))
some_addr = '0xB8DC8bD7005b6EeBced32F80C2a541CB864EB6ae'
ok_key = '91f155d4ca2474ab855a8e3a8b4213200b8d6639d147091dd66264cfc37491f8'
data = {
  "from": " 0xb60e8dd61c5d32be8058bb8eb970870f07233155",
  "to": " 0xd46e8dd67c5d32be8058bb8eb970870f07244567",
  "gas": "0x76c0",
  "gasPrice": "0x9184e72a000",
  "value": "0x9184e72a",
}
a = web3.isChecksumAddress('0xb60e8dd61c5d32be8058bb8eb970870f07233155')

print(a)
r1 = '0xd5c1c43e890fc45a8c605091be5b05318b22179f759bd5ced734bf429909a3fc'
r2 = '0xa4d791c55d86ec4f802af9063b5a4ced27714daee3a281e68b26514dd18ec340'
print (web3.sha3(hexstr='0x789456'))

