
def lend_money(debts, person, amount):
    if (not person in debts):
        list_new = []
        list_new.append(amount)

        debts[person] = list_new
    else:
        debts[person].append(amount)    
    print(debts)
    return None

def amount_owed_by(debts, person):
    dividafinal = 0

    if (not person in debts):
        return dividafinal 
    else:
       for i in debts[person]:
           dividafinal = dividafinal + i
       return dividafinal

def total_amount_owed(debts):
    total = 0
    for i in debts.keys():
        total += sum(debts[i]) 
    return total