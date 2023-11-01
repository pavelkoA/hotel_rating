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

mob_proxy = {
    'https': 'socks5://ec2655940e:29240553fc@188.120.243.158:41566',
    'http': 'socks5://ec2655940e:29240553fc@188.120.243.158:41566'
}
