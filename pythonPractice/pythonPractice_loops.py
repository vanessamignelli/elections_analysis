x = 0
while x <= 5:
    print(x)
    x = x + 1

#for loops
counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

#for loops and dictionaries
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

#get values in dictionary using a for loop
for county in counties_dict.values():
    print(county)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

#key-value pairs in a for loop
    for county, voters in counties_dict.items():
        print(county,voters)
    
    for county, voters in counties_dict.items():
        print(f"{county} county has, {voters:,} registered voters.")

# for loops and dictionary lists
voting_data = [{"county" : "Arapahoe", "registered_voters" : 422829},{"county" : "Denver", "registered_voters" : 463353}, {"county" : "Jefferson", "registered_voters" : 432438}]
print(voting_data)

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
    