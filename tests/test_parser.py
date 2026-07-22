from fingerprinting.banner_parser import BannerParser

parser = BannerParser()

samples = [

    "220 (vsFTPd 2.3.4)",

    "SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1",

    "220 metasploitable ESMTP Postfix (Ubuntu)",

    "Server: Apache/2.2.8 (Ubuntu) DAV/2",

    "X-Powered-By: PHP/5.2.4-2ubuntu5.10"

]

for banner in samples:

    print("=" * 60)

    print(banner)

    print(parser.parse(banner))
