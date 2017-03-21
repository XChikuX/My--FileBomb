import os
file = open("file_bomb.py","r")
i = 0
extension = "py"
while os.path.exists("file_bomb" + "_" + str(i) + "." +extension):
    i+=1
f2 = open ("file_bomb"+ "_" + str(i) + "." +extension,"w+")
j = 0
for line in file:
    j+=1
    if(j==2):
        f2.write("file = open(\"file_bomb"+ "_" + str(i) + "." +extension+"\",\"r\")\n")
    else:
        f2.write(line)
f2.close()
file.close()