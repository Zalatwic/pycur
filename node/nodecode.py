import time;


# our data will be stored in linked lists
# this code will create a structure for our data to live in
class Link(object):
    def __init__(self, data = None, nextLink = None):
        self.data = data
        self.next = nextLnk
    def getData(self):
        return self.data
    def getLink(self):
        return self.nextLink
    def setLink(self, newLink):
        self.nextLink = newLink

class Chain(object):
    def __init__(self, primary = None):
        self.primary = primary
    def insert(self, newPrimary):
        newPrimary = Link(data)
        newPrimary.setLink(self.primary)
        self.primary = newPrimary

class Transaction(object):
    def __init__(self, txData, toAdrs, fromAdrs, sig, reward, epoch = time.time(), xBroad = 0):
        self.txData = txData
        self.toAdrs = toAdrs
        self.fromAdrs = fromAdrs
        self.sig = sig
        self.reward = reward
        self.epoch = epoch
        self.xBroad = xBroad

# 
