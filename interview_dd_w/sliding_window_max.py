# input_data = [(order_id, time)]
from datetime import timedelta


def sliding_w_max(orders, window):
    orders = sorted(orders, key=lambda x: x["timestamp"])
    w_minutes = timedelta(minutes=window)

    left = 0
    count = 0

    for right in range(len(orders)):
        while orders[right]["timestamp"] - orders[left]["timestamp"] > w_minutes:
            left += 1
        count = max(count, right - left + 1)
    return count


from datetime import datetime, timedelta

orders = [
    {"order_id": 1, "timestamp": datetime(2026, 1, 1, 10, 0)},
    {"order_id": 2, "timestamp": datetime(2026, 1, 1, 10, 2)},
    {"order_id": 3, "timestamp": datetime(2026, 1, 1, 10, 4)},
    {"order_id": 4, "timestamp": datetime(2026, 1, 1, 10, 15)},
    {"order_id": 5, "timestamp": datetime(2026, 1, 1, 10, 16)},
]

print(sliding_w_max(orders, 5))