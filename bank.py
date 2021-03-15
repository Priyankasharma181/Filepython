banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
file=open("bank.txt","w")
for i in banks_list:
    file.write(i)
    file.write("\n")
