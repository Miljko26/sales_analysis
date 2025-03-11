# sales_data.py
sales_data = [230, 200, 310, 290, 400, 150, 180]
print(f"Sales data for the week: {sales_data}")

# sales_data.py
# Weekly sales data: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
sales_data = [230, 200, 310, 290, 400, 150, 180]


def total_sales(data):
    return sum(data)

def average_sales(data):
    if len(data) == 0:
        return 0 
    return sum(data) / len(data)

sales_data = [100, 200, 150, 300, 250, 400]

total = total_sales(sales_data)
average = average_sales(sales_data)

print(f"Ukupna vrednost svih prodaja: {total}")
print(f"Prosečna vrednost svih prodaja: {average}")