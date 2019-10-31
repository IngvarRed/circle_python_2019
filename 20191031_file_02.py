file_read = open("info.lala", "r")

data = file_read.read()
file_read.close()

for n, line in enumerate(data.split("\n")):
    # print(n+1, ":", len(line), ":" line)
    print(f"{n+1:}:{len(line):02}: "+line)