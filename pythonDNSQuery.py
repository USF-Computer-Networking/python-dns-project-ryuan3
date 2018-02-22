from argparse import ArgumentParser
import sys,socket  
#import dns.reversename
#import dns.resolver



def gethost(args):
    '''
        try to get hostname by ip but failed.
    '''
    try:
        #result = socket.gethostbyaddr(args.ipaddr)
        #result = dns.reversename.from_address(args.ipaddr)
        #result = dns.resolver.query(args.ipaddr, 'PTR')
        print "Result: hostname is " + result.to_text()
        write(result + " " + args.ipaddr)

    except Exception,e:
        print e
        #print "Cannot find the hostname."


def getip(args):
    try:
        result = socket.gethostbyname(args.hostname)
        print "Result: ip address is " + result
        write(args.hostname + " " + result)

    except Exception,e:
        print e        
        #print "Cannot find the ip address."

def write(record):
    file = open("dns_record.txt", 'w+')
    file.write(record)
    file.close()

def read():
    file = open("dns_record.txt", 'r+')
    for c in file:
        print(c)
    file.close()

def main():
    ap = ArgumentParser()
    #ap.add_argument('-ip', '--ipaddr', type = str, nargs = '?', help = "find hostname for an ip address") 
    ap.add_argument('-hn', '--hostname', type = str, nargs = '?', help = "find ip address for a hostname") 

    args = ap.parse_args()

    #if args.ipaddr:
    #    gethost(args)
    
    if args.hostname:
        getip(args)

if __name__ == "__main__":
    main()

