import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []


# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# put all elements of name_1 in a dict
names_1_dict = dict()
for name in names_1:
    names_1_dict[name] = name

# loop through names_2 and check if name exist in name_1_dict
for name_2 in names_2:
    try:
        # name exist so it is duplicate
         duplicates.append(names_1_dict[name_2])
    except KeyError:
        # print("no duplicate")
        pass

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

