#!/usr/bin/env python

def devices():
    routers = ["router1", "router2", "router3"]
    return routers


def security():
    credentials = {}

    for router in devices():
        credentials[router] = 'passw0rd1'

    return credentials


def combined():
    return devices(), security()


if __name__ == "__main__":
    print 'The routers are:\n{}'.format(devices())
    print 'The credentials are:\n{}'.format(security())
    print 'All data is:'
    for result in combined():
        print result