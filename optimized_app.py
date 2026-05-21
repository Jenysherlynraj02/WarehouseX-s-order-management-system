# WarehouseX Optimized Application Code

import time
from functools import lru_cache

# Simulated database
orders_db = {
    1001: {"customer": "Alice", "amount": 2500},
    1002: {"customer": "Bob", "amount": 3200},
    1003: {"customer": "Charlie", "amount": 1800},
    1004: {"customer": "David", "amount": 4100}
}

# Cache frequently accessed orders
@lru_cache(maxsize=100)
def fetch_order(order_id):
    print(f"Fetching Order {order_id} from database...")
    time.sleep(1)
    return orders_db.get(order_id)

# Process orders efficiently
def process_orders(order_ids):
    processed_orders = []

    for order_id in order_ids:
        order = fetch_order(order_id)

        if order:
            processed_orders.append({
                "Order ID": order_id,
                "Customer": order["customer"],
                "Amount": order["amount"]
            })

    return processed_orders

# Main Program
if __name__ == "__main__":
    order_list = [1001, 1002, 1003, 1001]

    results = process_orders(order_list)

    print("\nProcessed Orders:\n")

    for result in results:
        print(result)
