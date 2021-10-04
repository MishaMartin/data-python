cupcake_file = open("CupcakeInvoices.csv")

# for line in cupcake_file:
#     print(line)

for line in cupcake_file:
    line_split = line.rstrip("\r\n").split(",")
    print(line_split[2])

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
cupcake_file.close()

#this is a text for matplotlib. Please use python3 or pip3 if you need to access that. 
#python3 {name of file} in the terminal will make sure that it is going to show a graph with the formula below.
# import matplotlib.pyplot as plt

# plt.bar([1,2,3],[4,5,6])
# plt.show()
