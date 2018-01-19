import requests
def getHTMLText(url):
    try:
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        res.raise_for_status()
        return res.text
    except Exception as exc:
        print('There was a problem: %s' % (exc))


if __name__ == "__main__":
    url = "https://www.baidu.com/pythonss"
    print(getHTMLText(url))
