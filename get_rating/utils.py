import requests


with open("docs/proxy.txt", "r", encoding="utf-8") as proxy_file:
    proxy_list = [proxy.strip() for proxy in proxy_file.readlines()]


def is_true_proxy(proxy):
    try:
        requests.get("https://strike.ru/",  proxies= {"https": "https://" + proxy}, timeout = 0.1)
    except:
        # print('--' + proxy + ' is dead: ' + proxy.__class__.__name__)
        return False
    return True

for proxy in proxy_list:
    if is_true_proxy(proxy):
        print(proxy)


