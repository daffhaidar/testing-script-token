import csv
import random

# Total supply and distribution
total_supply = 10_000_000_000
your_coins = int(total_supply * 0.1)  # 10% for yourself
airdrop_coins = total_supply - your_coins  # 90% for airdrop

# Generate random distribution for 100 addresses
num_addresses = 100
addresses = ["0x" + ''.join(random.choices("abcdef1234567890", k=40)) for _ in range(num_addresses)]

# Generate random allocations that sum up to airdrop_coins
allocations = [random.randint(1, airdrop_coins // num_addresses) for _ in range(num_addresses - 1)]
allocations.append(airdrop_coins - sum(allocations))  # Ensure total equals 9B

# Combine addresses and allocations
data = [{"Address": addr, "Quantity": qty} for addr, qty in zip(addresses, allocations)]

# Write to CSV
with open("airdrop_addresses.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Address", "Quantity"])
    writer.writeheader()
    writer.writerows(data)

print(f"File airdrop_addresses.csv berhasil dibuat. Total koin yang di-airdrop: {sum(allocations):,}.")
