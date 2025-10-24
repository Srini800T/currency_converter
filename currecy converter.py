print(" Currency Converter")
print("1.Dollar to Ruppees")
print("2.Rupees to Dollar")

choice = int(input("Enter your choice (1 to 2): "))

if choice == 1:
    Dollar = float(input("Enter Dollar in to Rupees:"))
    Rupees = (Dollar * 88.72)
    print("Dollar in Rupees:",Rupees)
elif choice == 2:
    Rupees = float(input("Enter Rupees in to Dollar:"))
    Dollar = (Rupees / 88.72)
    print("Rupees in Dollar:",Dollar)
else:
    print("Invalid choice! Please enter 1 0r 2.")