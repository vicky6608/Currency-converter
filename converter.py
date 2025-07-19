x = float(input("Please enter amount in USD "))
y = input("Enter the output currency - CAD,EUR,INR").strip().upper()

if y == "CAD":
    z = x * 1.37
elif y == "EUR":
    z = x * 0.86
elif y == "INR":
    z = x * 86.19
else :
    print("Invalid currency. Please enter CAD, EUR or INR.")

print(f"\n You entered: ${x} USD")
print(f"Converted to {y}: {round(z,2)} {y} \n")