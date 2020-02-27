import csv

region_units={}
region_revenue={}
region=[]

current_region=""
current_units=0
current_revenue=0

f = open("region_input.csv", 'rt')
reader =csv.reader(f)

# this is the header, we disregard it
my_header=next(reader)
print(my_header)

# read the input file
for row in reader:
    print(row)

    # get the current row value
    current_region =row[0]
    current_units=int(row[1])
    current_revenue=int(row[2])

    if not current_region in region_units:
        region_units[current_region] = current_units

    else:
        region_units[current_region] \
            += current_units

print(region_units)

regions=list(region_units.keys())

print(regions)

print("all the regions found are:", end="")
for r in regions:
    print(r,end=",")
print()

print("Totals per region")
for r in regions:
    print(r)
    print("total units for region:"+str(region_units[r]))
print()