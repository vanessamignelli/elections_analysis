counties = ["Arapahoe", "Denver", "Jefferson"]

if "El Paso" in counties:
    print("El Paso in list of counties")
else:
    print("El Paso not in list")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Both in list of counties")
else:
    print("Both not in list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("At least one in counties")
else:
    print("None in counties")