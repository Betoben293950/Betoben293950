#!/usr/bin/python
'''
brut3k1t - main application that calls upon dependencies and 
    other libraries / modules
'''

from src.brut3k1t import *


def main():
    os.system("rm -rf tmp/") # delete tmp if created from previous usage
    
    parser = argparse.ArgumentParser(description='Bruteforce framework written in Python')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--service', dest='service', help="Provide a service being attacked. Several protocols and services are supported")
    required.add_argument('-u', '--username', dest='username', help='Provide a valid username for service/protocol being executed')
    required.add_argument('-w', '--wordlist', dest='password', help='Provide a wordlist or directory to a wordlist')
    parser.add_argument('-a', '--address', dest='address', help='Provide host address for specified service. Required for certain protocols')
    parser.add_argument('-p', '--port', type=int, dest='port', help='Provide port for host address for specified service. If not specified, will be automatically set')
    parser.add_argument('-d', '--delay', type=int, dest='delay', help='Provide the number of seconds the program delays as each password is tried')
    #parser.add_argument('--proxy', dest='proxy', help="Providing a proxy for anonymization and avoiding time-outs")

    args = parser.parse_args()
    
    man_options = ['username', 'password']
    for m in man_options:
        if not args.__dict__[m]:
            print R + "[!] You have to specify a username AND a wordlist! [!]" + W
            exit(1)
    
    service = args.service
    username = args.username
    wordlist = args.password
    address = args.address
    port = args.port
    delay = args.delay
        
    print choice(headers)
    print (G + "[*] Username: %s " % username) + W
    sleep(0.5)
    print (G + "[*] Wordlist: %s " % wordlist) + W
    sleep(0.5)
    
    if os.path.exists(wordlist) == False:
        print R + "[!] Wordlist not found! [!]" + W
        exit(1)
        
    print (C + "[*] Service: %s "  % service) + W
    
    if service is None:
        print R + "[!] No service provided! [!]" + W
        exit(1)
    '''    
    if proxy is not None:
        print (C + "[*] Proxy file: %s " % proxy) + W
        print O + "Checking if proxies are active...\n" + W
        proxyServer(proxy)'''
        
    if delay is None:
        print O + "[?] Delay not set! Default to 1 [?]" + W
        delay = 1
        
    sleep(0.5)
    
    protocols = ["ssh", "ftp", "smtp", "telnet"]
    web = ["instagram", "twitter", "facebook"]
    
    if service in protocols:
        p = ProtocolBruteforce(service, address, username, wordlist, port, delay)
        p.execute()
    elif service in web:
        if address or port:
            print R + "[!] NOTE: You don't need to provide an address OR port [!]" + W
            exit(1)
        w = WebBruteforce(service, username, wordlist, delay)
        w.execute()
    elif service == 'xmpp':
        xmppBruteforce(address, port, username, wordlist, delay)
    elif service == 'test':
        b = Bruteforce(service=None, username=None, wordlist=None, address=None, port=None, delay=1)
    else:
        print R + "[!] No such service found! [!]" + W


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print R + "\n[!] Keyboard Interrupt detected! Killing program... [!]" + W
        exit(1)
