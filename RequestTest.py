import requests

url = 'http://192.168.1.37:5000/testDetect'

data = {
    "requestId": "12345",
    "imageUrl":"https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593144.jpg",
    "returnUrl":"12345",
    "type":"12345"
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json = data, headers = headers, timeout = 50)

print(response.text)
