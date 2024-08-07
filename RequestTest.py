import requests, json

if __name__ == "__main__":
    url = 'http://222.240.1.44:48888/Detect'

    data = {
        "imageData": ["0"]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json = data, headers = headers)
    result = response.json()
    print(result)
