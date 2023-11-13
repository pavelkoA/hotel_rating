from fake_useragent import UserAgent


ua = UserAgent()
headers = {
    "User-Agent": ua.random
}


proxy1 = {
    'https': 'socks5://vAcqzZ:8ZeV5m@31.44.190.36:9421',
    'http': 'socks5://vAcqzZ:8ZeV5m@31.44.190.36:9421'
}
proxy2 = {
    'https': 'socks5://vAcqzZ:8ZeV5m@31.44.190.20:9746',
    'http': 'socks5://vAcqzZ:8ZeV5m@31.44.190.20:9746'
}
proxy3 = {
    'https': 'socks5://vAcqzZ:8ZeV5m@31.44.188.6:9981',
    'http': 'socks5://vAcqzZ:8ZeV5m@31.44.188.6:9981'
}


proxy_list = [proxy1, proxy2, proxy3]



# mob_proxy = {
#     'https': 'socks5://6424679-all-country-RS-state-8199669-city-792680-asn-2885:1b6q4k3y1x@89.39.106.148:13765',
#     'http': 'socks5://6424679-all-country-RS-state-8199669-city-792680-asn-2885:1b6q4k3y1x@89.39.106.148:13765'
# }

mob_proxy = {
    'https': 'socks5://a799b46c4d:475a6e9c6d@88.87.84.141:41413',
    'http': 'socks5://a799b46c4d:475a6e9c6d@88.87.84.141:41413'
}
