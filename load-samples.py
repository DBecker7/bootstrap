
handle = open("testfile.txt", "r")
sample2 = handle.readlines()
for item in sample2[0].split(" "):
    print(float(item))

handle.close()

sample3 = [float(item) for item in sample2[0].split(" ")[:-1]]
plt.hist(sample3, bins = 40)
plt.show()
