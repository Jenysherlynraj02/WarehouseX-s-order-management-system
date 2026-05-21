# WarehouseX Debugged Application Code

def calculate_total(order_amount, tax_rate):
    try:
        # Null validation
        if order_amount is None or tax_rate is None:
            raise ValueError("Inputs cannot be None")

        # Datatype validation
        if not isinstance(order_amount, (int, float)):
            raise TypeError("Order amount must be numeric")

        if not isinstance(tax_rate, (int, float)):
            raise TypeError("Tax rate must be numeric")

        # Total calculation
        total = order_amount + (order_amount * tax_rate)

        return round(total, 2)

    except ValueError as ve:
        return f"Value Error: {ve}"

    except TypeError as te:
        return f"Type Error: {te}"

    except Exception as e:
        return f"Unexpected Error: {e}"

# Testing
print(calculate_total(2000, 0.18))
print(calculate_total(None, 0.18))
print(calculate_total("2000", 0.18))
