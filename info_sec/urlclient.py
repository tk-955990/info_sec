import urllib.request

response = urllib.request.urlopen('http://192.168.0.6/blog/wp-admin')

data = response.read()

print(data)
