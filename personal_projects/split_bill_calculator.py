# Split Bill Calculator -> a calculator that splits the total bill inclusive of tax.

# User input of nett bill.
bill = float(input("How much is the bill?: "))
print(f"The nett bill is: ${bill}")

#User input of the tax charged. 
gst_input = input("Sprinkle in that GST (%): ")
gst = float(gst_input.replace('%', '').strip())
print(f"GST entered: {gst}%")

# Display the total bill with tax included.
gst_total = bill * (gst / 100) 
total_bill = gst_total + bill
print(f"The total bill inclusive of GST is: ${total_bill:.2f}")

# User input of the total number of diners
people = int(input("How many people are splitting the bill?: "))

# Display the split amount shared by each diner.
split = total_bill / people 
print(f"Each person has to pay: ${split:.2f}")