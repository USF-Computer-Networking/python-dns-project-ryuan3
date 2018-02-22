# python-dns-project-ryuan3

a tool for getting ip address by hostname

## how to use
`./ -hn www.google.com`

## result
it will print a ip address for the hostname and record the mapping relationship in a file.

## implement
use ArgumentParser to get the args

use socket.gethostbyname() to query the ip

## next step
search result in the local record first
