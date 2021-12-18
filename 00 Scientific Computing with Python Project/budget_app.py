class Category:

    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, *description):
        record = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(record)
    
    def check_fund(self, amount):
        balance = 0
        for i in range(len(self.ledger)):
            balance = balance + self.ledger[i]["amount"]
        if amount <= balance:
            return True
        else:
            return False
    
    def withdraw(self, amount, *description):
        if self.check_fund(amount) == True:
            record = {
                "amount": int(amount)*-1,
                "description": description
            }
            self.ledger.append(record)
        else:
            return
    
    def get_balance(self):
        balance = 0
        for i in range(len(self.ledger)):
            balance = balance + self.ledger[i]["amount"]
        print(balance)

    def transfer(self, amount, another_budget):
        if self.check_fund(amount) == True:
            record = {
                "amount": int(amount)*-1,
                "description": f"Transfer to {another_budget.name}"
                }
            self.ledger.append(record)

            record_t = {
                "amount": amount,
                "description": f"Transfer from {self.name}"
                }
            another_budget.ledger.append(record_t)
            #setattr(another_budget, "ledger", record_t)
        else:
            return

    def show_tx(self):
        star_count = 30 - len(self.name)
        if star_count % 2 == 0:
            first_stars = "*" * int(star_count/2)
            last_stars = "*" * int(star_count/2)
        else:
            first_stars = "*" * int((star_count-1)/2)
            last_stars = "*" * int((star_count-1)/2)
        head_line = first_stars + self.name + last_stars
        print(head_line)

        for i in range(len(self.ledger)):
            dsc = self.ledger[i]["description"][0]
            amt = float("{:.2f}".format(self.ledger[i]["amount"]))
            print(f"{dsc:<23}{amt:>7}")

        total = 0
        for i in range(len(self.ledger)):
            total = total + int((self.ledger[i]["amount"]))
        total = float("{:.2f}".format(total))
        print(f"Total{total:>25}")

##################################################################################################
##################################################################################################

def create_spend_chart(categories: list):

    #calculation
    withdraws = list(range(len(categories)))
    for i in range(len(categories)):
        withdraws[i] = []
        for j in range(len(categories[i].ledger)):
            if categories[i].ledger[j]["amount"] < 0:
                withdraws[i].append(categories[i].ledger[j]["amount"])

    sum = 0
    for i in range(len(withdraws)):
        for j in range(len(withdraws[i])):
            sum = sum + withdraws[i][j]

    percent = list(range(len(withdraws)))
    for i in range(len(withdraws)):
        sum_each_category = 0
        for j in range(len(withdraws[i])):
            sum_each_category = sum_each_category + withdraws[i][j]
        percent[i] = (sum_each_category/sum)*100

    summary = []
    for i in range(len(categories)):
        wrap = [categories[i].name, int(percent[i])]
        summary.append(wrap)
    def find_number(number):
        return number[1]
    summary.sort(key=find_number, reverse=True)
    print(summary)

    #plotting chart
    point = list(range(11))
    point[0] = "100 | "
    for i in range(9):
        point[i+1] = " " + str(100-((i+1)*10)) + " | "
    point[10] = "  0 | "

    for i in range(len(summary)):
        for j in range(len(point)):
            scale = int(point[j].split()[0])
            if int(summary[i][1]) > scale:
                point[j] = point[j] + " o "
    
    print("Percentage spent by category")
    for i in range(len(point)):
        print(point[i])
    
    mark = "-" * (len(point[10])+2)
    print(mark)

    x_label = list(range(len(summary)))
    for i in range(len(summary)):
        x_label[i] = list(summary[i][0])

    x_label_sep = []
    for i in range(len(x_label)):
        for j in range(len(x_label[i])):
            try:
                x_label_sep.append(x_label[i][j] + x_label[i+1][j])
            except:
                list_len = max(len(k) for k in x_label)
                if  len(x_label_sep) < list_len:
                    x_label_sep.append(x_label[i][j] + " ")
                else:
                    continue

    for i in range(len(x_label_sep)):
        line = ""
        for j in range(len(x_label_sep[i])):
            line = line + "  " + x_label_sep[i][j]
        print("     " + line)
