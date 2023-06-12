# py-file-io.py
# File io APIs:
#  open, close, read, write-> append
# open: -> allocate a buffer for file operations (buffers can be: stacks or Queues)
# close: -> free for dynamically allocated buffer
#  r --> read only, can not write
#  w --> write only, can not read
#  r+ --> read and when wrtie append
#  w+ --> can read, when write --> overwrite 

db = list()
file = open("ex.csv", "r")
lines = file.readlines()
file.close()
def FindName(db, name):
	for i,record in enumerate(db):  #  for -
		if name == record["name"]:
			return i
	return -1

for line in lines:
    # print(line.split(",")[0])
    lineSplit = line.split(",")
    nameCol = lineSplit[0].rstrip("\n") # rstrip -> right stripping of whitespace
    numbCol = lineSplit[1].rstrip("\n")
    # db.append([nameCol,numbCol])
    db.append({"name":nameCol, "number":numbCol})
print(db)
name_in = input("enter a name to change: ")
name_out = input("enter name replacement: ")
index = FindName(db, name_in)

if index >= 0:
    db[index]["name"] = name_out
    
    file = open("ex.csv", "w")
    for record in db:
        file.write(record["name"]+","+record["number"]+"\n")
    file.close()
print(db)