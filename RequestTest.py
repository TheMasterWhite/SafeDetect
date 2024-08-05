import requests, json


if __name__ == "__main__":
    url = 'http://192.168.2.36:8888/Detect'
    imageurl = ["https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593135.jpg",
           "https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593144.jpg"]

    data = {
        "requestId": "10086",
        "imageUrl": imageurl,
        "type": "gasTank",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json = data, headers = headers, timeout = 50)

    print(response)