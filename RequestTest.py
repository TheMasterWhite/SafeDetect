import requests, json




if __name__ == "__main__":
    url = 'http://192.168.1.37:8000/Detect'

    data = {
        "requestId": "10086",
        "imageUrl": "https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593144.jpg",
        "returnUrl": "12345",
        "type": "gasTank",
        "saveImage":True
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json = data, headers = headers, timeout = 50)

    print(response.text)