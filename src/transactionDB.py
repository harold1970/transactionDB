import users
import random
import time
import json
# broken, get someone to fix --finnh 9/12/24
import color
import hashlib
# first commit works

customers = {}
transactions = {}


with open("names.txt", "r") as f:
    file = f.read()
    names = file.split("\n")
with open("payment_options.txt", "r") as f:
    file = f.read()
    options = file.split("\n")
with open("menu.json", "r") as f:
    menu = json.load(f)
    print(menu)

def error(message):
    print(f"{color.bcolors.FAIL}{message}{color.bcolors.ENDC}")


for i in range(1000):
    customers[i] = users.Customer(random.choice(names), i, 0,0, random.choice(options),0)

# for i in range(1000):
#     print(customers[i].name, " | ", customers[i].id, " | ", customers[i].PPO )

for i in range(10000):                           #id                                 date                                                                                       time                                                                               
    transactions[i] = users.Transaction(f"T{i*1000000000}", f"{random.randint(0,99)}{random.randint(0,99)}/{random.randint(0,12)}/{random.randint(0,31)}", time.gmtime(), random.randint(0,999), [], 0, random.randint(10,25))
    for o in range(random.randint(1,10)):
        item = random.choice(list(menu.keys()))
        # choice of some random item
        transactions[i].itemsOrdered.append(item)
        transactions[i].total += menu[item]
        # add the tip
        transactions[i].total += (transactions[i].total * (transactions[i].tipP / 100))
        # give this to a random customer
        transactions[i].customerId = random.randint(0,999)
        # add the points
        customers[transactions[i].customerId].points += len(transactions[i].itemsOrdered)
        # add the transaction total to customer total
        customers[transactions[i].customerId].total += transactions[i].total
# for i in range(999):
#     print(transactions[i].transactionId," | ", transactions[i].customerId," | ", transactions[i].total)

found_users = {} 
commands = ["list", "search", "get", "exit", "help"]

# Get user input and encode it
password = input("please enter password>> ")
userinput = password.encode()

# Read the stored password hash from the file
with open("password.txt", "r") as f:
    stored_hash = f.read().strip()

# Hash the user input
hashed_input = hashlib.sha512(userinput).hexdigest()
if hashed_input != stored_hash:
    error("incorrect password.")
    exit()
else:
    print("login succsessful\n")
while True:
    command = input("please enter command, help > ")
    command = command.split(" ")
    if command[0] in commands:
        
        
        if command[0] == "help":
            if len(command) == 1:
                print("list (none) -> returns list of users writes to a file")
                print("search (name) -> search for users and returns the id")
                print("get (id) -> returns the transactions of that users")
                print("exit (none) -> exits")
        if command[0] == "exit":
            break
        if command[0] == "search":
            if len(command) == 2:
                name = command[1]
                for i in customers.keys():
                    if name == customers[i].name.lower():
                        found_users[transactions[i].customerId] = customers[i].id
                if bool(found_users):
                    for i in found_users.keys():
                        print(color.bcolors.OKGREEN + customers[found_users[i]].name, "id: ", customers[found_users[i]].id , color.bcolors.ENDC)
                    
                    found_users.clear()
                else:
                    error(f"no user with name '{name}'")
            else:
                error(f"you need one more arg <id> ")
        if command[0] == "list":
            for i in customers.keys():
                if i % 10 == 0:
                    if input(":") == "q":
                        break
                print(customers[i].name," | ", customers[i].id )
                time.sleep(0.0005)


        if command[0] == "get":
            if len(command) == 2:    
                customer = ""
                try:
                    customer = customers[int(command[1])].id
                except KeyError:
                    error("the id does not exist")
                except ValueError:
                    error("the id must only contain intagers")
                print("1. see transactions \n2. see points \n3. see total spent")
                option = input("please enter option > ")
                if option == '1':
                    for i in transactions.keys():
                        if transactions[i].customerId == customer:
                            print(transactions[i].transactionId)
                            for x in transactions[i].itemsOrdered:
                                print(x, "| ", "$"+str(menu[x]))
                            input()
                if option == '2':
                    print(customers[customer].points)
                if option == '3':
                    print(f"${customers[customer].points}")
            else:
                error(f"you need one more arg <id>")
    else:
        print(color.bcolors.FAIL+f"unkown command {command[0]}"+color.bcolors.ENDC)