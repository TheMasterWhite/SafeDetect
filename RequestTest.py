import requests, json

if __name__ == "__main__":
    url = 'http://222.240.1.44:38080/addInfer'

    data = {
        "imageData": ["2","3","4","5","6","7","8","9"]
    }
    data2 = {
        "oper":"Test",
        "imgId":"2",
        "safeType":"6",
        "indexUrl":"666 666 666 666"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json = data2, headers = headers)
    result = response.json()
    print(result)
