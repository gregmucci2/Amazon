import urllib3

# Simple hello world
http = urllib3.PoolManager()
response = http.request('GET', 'http://httpbin.org/hello')
print(response.data)