# Write a program that converts a given number of days 
#into years, weeks, and days
all_days = 43336
extra_months = all_days % 365
years = all_days // 365
days = extra_months % 30
months = extra_months // 30

print("years",years, " months", months, "days",days)
