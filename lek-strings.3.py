print("Välkommen till mitt program där du kan addera")

operator = input("Välj räknesätt(+, -, *, /): ")
try:
    
    num1 = int(input("Skriva in ett heltal: "))
    
except:
    print("Du måste skriva ett tal")
    
    num1 = 0
    

try:
     num2 = int(input("skriv ett annorlunda heltal: "))

except:
    print("Du måste skriva ett tal: ")
    num2 = 0

if operator == "+":
    total = num1 + num2

elif operator == "-":
    total = num1-num2

elif operator == "*":
    total = num1 * num2

elif operator == "/":
    total = num1/num2

   



print("Summan är:", total)