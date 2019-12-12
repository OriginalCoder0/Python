from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

#proxy = '127.0.0.1:80'
#proxy = '111.200.239.46:8080'
#proxy = '111.200.239.42:8080'
#proxy = '218.60.8.83:3129'
#proxy = '61.50.96.62:8080'
#proxy = '218.29.38.150:49737'
proxy = '221.1.200.242:38652'

proxy_handler = ProxyHandler({'http':'http://'+proxy, 'https':'https://'+proxy})

opener = build_opener(proxy_handler)
#opener = build_opener()

try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
