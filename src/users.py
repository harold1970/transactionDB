class Customer:
    def __init__(self, name, id, listOfTransactions, points, PPO, total):
        self.name = name
        self.id = id
        self.listOfTransactions = listOfTransactions
        self.PPO = PPO
        self.points = points
        self.total = total
    
class Transaction:
    def __init__(self, transactionId, date, time, customerId, itemsOrdered, total, tipP):
        self.transactionId = transactionId
        self.date = date
        self.time = time
        self.customerId = customerId
        self.itemsOrdered = itemsOrdered
        self.total = total
        self.tipP = tipP
