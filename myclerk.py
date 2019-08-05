#Real life situation: Customers in line at a grocery store
#A customer appears every 3 minutes
#The average customer takes 4 minutes to get through the line
#What is the average wait time?

import random
from pythonds.basic import Queue

class Clerk:
    def __init__(self, ipm):
        self.itemrate = ipm
        self.currentCustomer = None
        self.timeRemaining = 0
    def tick(self):
        if self.currentCustomer != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentCustomer = None
    def busy(self):
        if self.currentCustomer != None:
            return True
        else:
            return False 
    def startNext(self, newCustomer):
        self.currentCustomer = newCustomer
        self.timeRemaining = newCustomer.getItems() * 60/self.itemrate

class Customer:
    def __init__(self, time):
        self.timestamp = time
        self.items = random.randrange(1,21)
    def getStamp(self):
        return self.timestamp
    def getItems(self):
        return self.items
    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def simulation(numSeconds, itemsPerMinute):
    ourClerk = Clerk(itemsPerMinute)
    clerkQueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if newCustomer():
            customer = Customer(currentSecond)
            clerkQueue.enqueue(customer)
        if (not ourClerk.busy()) and (not clerkQueue.isEmpty()):
            nextCustomer = clerkQueue.dequeue()
            waitingtimes.append(nextCustomer.waitTime(currentSecond))
            ourClerk.startNext(nextCustomer)

        ourClerk.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print('Average Wait %6.2f secs %3d tasks remaining.'%(averageWait, clerkQueue.size()))

def newCustomer():
    num = random.randrange(1,181)
    if num == 44:
        return True
    else:
        return False

