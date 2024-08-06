import requests, json


if __name__ == "__main__":
    url = 'http://222.240.1.44:38080/findImgsPage'
    imageurl = ["https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593135.jpg",
           "https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593144.jpg"]

    data = {
        "imgId" : "555",
        "page":1,
        "pageSize":1

    }
    headers = {'Content-Type': 'application/json'}
    data2 = {}
    response = requests.get(url, json = data2, headers = headers, timeout = 50)

    print(json.dumps(response.json(), indent = 4))