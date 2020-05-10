from names import names
import random
import os



dirName= "files"
if not os.path.exists(dirName):
  os.mkdir(dirName)
  print("Directory", dirName,  "Created ")

friend = []
for x in range(100000):
  temp1 = random.choice(names)
  temp2 = random.choice(names)
  friend.append((temp1, temp2))
friend = set(friend)
friend = tuple(friend)

oldnum=-1
for index in range(len(friend)):
  newnum = index // 1000
  if oldnum != newnum:
    f = open(os.path.join(dirName, "file{}.txt".format(newnum)), "w")
    print("dir {} created.\n".format(newnum))
  else:
    f = open(os.path.join(dirName, "file{}.txt".format(newnum)), "a")
  oldnum=newnum
  f.write("{}, {}\n".format(friend[index][0], friend[index][1]))
  f.close()







