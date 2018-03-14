#rom urllib2 import Request, urlopen
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}
request = 'http://api.infura.io/v1/jsonrpc/ropsten/methods'
headers=headers

a = requests.get(request,headers)


response_body = a.text
print (response_body)

