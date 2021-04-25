line_counter = 0
data_header = []
customer_list = []
employee = []
customer_usa_only_list = []

with open("C:\\Users\\user\\atom-workspace\\customers.csv") as c:

    while 1:
        data = c.readline()
        if not data:
            break

        if line_counter == 0:
            data_header = data.split(",")

        else:
            customer = data.split(",")

            if (customer[3].upper() == "USA\n"):
                customer_usa_only_list.append(customer)
            else:
                customer_list.append(data.split(","))

        line_counter += 1


print("header : ", data_header)
for i in range(len(customer_list)):
    print("data ", i, " : ", customer_list[i])
print(len(customer_list))

with open("customer_usa_only.csv", "w") as customer_usa_only_csv:
    for customer in customer_usa_only_list:
        customer_usa_only_csv.write(",".join(customer).strip('\n') + "\n")

for i in range(len(customer_usa_only_list)):
    print("data ", i, " : ", customer_usa_only_list[i])
