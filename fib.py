#!/usr/bin/env python

#number of rabbit pairs after n months if we begin with 1 pair and every generation every pair produces k rabbit pairs
n = 32
k = 2
founding_pair = 1
months = n
litterpergen_pair = k
final_rabbits = 0

rabbits = [1, 1]  # Month 1 and Month 2 both start with 1 pair

# Step 2: Loop through months 3 to n
for month in range(3, n + 1):
    # New total = rabbits from last month + (rabbits from 2 months ago * k)
    new_rabbits = rabbits[-1] + (rabbits[-2] * k)
    rabbits.append(new_rabbits)  # Add the new month's total to the list

# Step 3: Print the final total
print(rabbits[-1])


