def total_sales(ticket_sales):
    total_value = 0
    for key, sale in ticket_sales.items():
        total_value += sale
    return total_value
# Test Cases
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))
