from fake_useragent import UserAgent


ua = UserAgent()
headers = {
    "User-Agent": ua.random
}


proxy = {
        'https': 'socks5://q6G8yQ:xs33tk@146.19.234.45:8000',
        'http': 'socks5://q6G8yQ:xs33tk@146.19.234.45:8000'
    }


proxy1 = {
    'https': 'socks5://vAcqzZ:8ZeV5m@31.44.190.36:9421',
    'http': 'socks5://vAcqzZ:8ZeV5m@31.44.190.36:9421'
}

proxy2 = {
    'https': 'https://vAcqzZ:8ZeV5m@31.44.190.20:9746',
    'http': 'http://vAcqzZ:8ZeV5m@31.44.190.20:9746'
}
proxy3 = {
    'https': 'https://vAcqzZ:8ZeV5m@31.44.188.6:9981',
    'http': 'http://vAcqzZ:8ZeV5m@31.44.188.6:9981'
}


proxy_list = [proxy1, proxy2, proxy3]



mob_proxy = {
    'https': 'socks5://d647c11572:0715cbad61@92.255.251.69:41578',
    'http': 'socks5://d647c11572:0715cbad61@92.255.251.69:41578'
}