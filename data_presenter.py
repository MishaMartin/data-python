cupcake_file = open("CupcakeInvoices.csv")

# for line in cupcake_file:
#     print(line)

# for line in cupcake_file:
#     line_split = line.rstrip("\r\n").split(",")
#     print(line_split[2])

# for line in cupcake_file:
#     line_split = line.rstrip("\r\n").split(",")
#     quant = float(line_split[3])
#     price = float(line_split[4])
#     total = quant * price
#     print(total)
sum = 0

for line in cupcake_file:
    line_split = line.rstrip("\r\n").split(",")
    quant = float(line_split[3])
    price = float(line_split[4])
    total = quant * price
    total1 = round(total, 2)
    # print(total)
    sum += total1

print (sum)

#how to limit your float to a certain decimal point
# example = 76.3656985
# a_round = round(example, 2)
# print(a_round)

