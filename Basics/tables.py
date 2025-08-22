
def generateTables(n):
    table = ""
    for i in range(1,11):
        table += (f"{n} × {i} = {n*i}\n")
    with open(f"Basics/tables/table_{n}.txt", "w")  as f:
        f.write(table)  

for i in range(2,41):
    generateTables(i)