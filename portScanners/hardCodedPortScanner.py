from socket import *
def conScan(tgHost, tgPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgHost,tgPort))
        print('[+]%d/tcp open'% tgPort)
        connskt.close()
    except:
        print('[-]%d/tcp closed'% tgPort)

def portScan(tgHost, tgPorts):
    try:
        tgIP = gethostbyname(tgHost)
    except:
        print('[-]Cannot resolve %s'% tgHost)
        return

    try:
        tgName = gethostbyaddr(tgIP)
        print('[-]Scan result of %s'% tgName[0])
    except:
        print('[-]Scan result of %s'% tgIP)
    setdefaulttimeout(1)
    for tgPort in tgPorts:
        print('Scanning Port: %d'% tgPort)
        conScan(tgHost, int(tgPort))

if __name__ == '__main__':
    portScan('google.com', [80,22])