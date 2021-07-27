# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
# Create a list called names
names = ["Maria", "Rohan", "Valentina"]

# create a list called insurance_costs
insurance_costs = [4150.0, 5320.0, 35210.0]

# Pair names with insurance_costs and assign it to insurance_data 
insurance_data = list(zip(names, insurance_costs))

# Display insurance_data
print("\n" + str(insurance_data))

# Create an empty list called estimated_insurance_data
estimated_insurance_data = []

# Add Maria's estimated insurance data to estimated_insurance_data
estimated_insurance_data.append(("Maria", maria_insurance_cost))

# Add Rohan's estimated insurance data to estimated_insurance_data
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))

# Add Velentina's estimated insurance data to estimated_insurance_data
estimated_insurance_data.append(("Velentina", valentina_insurance_cost))

# Display estimated_insurance_data
print("\n" + str(estimated_insurance_data))

# Display the actual insurance cost data (insurance_data)
print("\nHere is the actual insurance cost data: " + str(list(insurance_data)))

# Display estimated_insurance_data
print("\nHere is the estimated insurance cost data: " + str(estimated_insurance_data))

# Display a message
print("\nComparing the actual insurance cost data with the estimated insurance data, by inspection the estimated insurance cost data turns to be overestimated.")

# A list of estimated_insurance_data - insurance_data
insurance_cost_difference = [4222.0-4150.0, 5442.0-5320.0, 36368.0-35210.0]

# Display insurance_cost_difference
print("\nThe difference between the actual insurance cost data and the estimated insurance cost data for each individual is " + str(insurance_cost_difference))

# Estimate Akira's insurance cost
print("\n")
akira_insurance_cost = estimate_insurance_cost("Akira", 19, 1, 27.1, 0, 0)

# Add Akira's name to names
names.append("Akira")

# Add Akira's actual insurance data to insurance_costs
insurance_costs.append(2930.0)

# Pair names with insurance_costs and assign it to insurance_data including Akira's own
insurance_data = list(zip(names, insurance_costs))

# Add Akira's estimated insurance data to estimated_insurance_data
estimated_insurance_data.append(("Akira", akira_insurance_cost))

# Display the actual insurance cost data (insurance_data) including Akira's own
print("\nHere is the actual insurance cost data: " + str(list(insurance_data)))

# Display estimated_insurance_data including Akira's own
print("\nHere is the estimated insurance cost data: " + str(estimated_insurance_data))