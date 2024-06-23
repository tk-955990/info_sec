import urllib.request

url = (
    "https://www.starbucks.co.jp/cafe/bananabrulee"
    "/images/feature/p1_on2.png"
)
imagefile = "banana.png"

urllib.request.urlretrieve(url, imagefile)

print("File saved!")
