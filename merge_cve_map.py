
out = open("cve_exploitdb_dict.py", "w")

s = "__cve_map = {\n"

i = 0
while True:
    file = open("files_" + str(i) + ".list.dict")
    lines = file.readlines()
    for l in lines:
        s += "\t" + l + ",\n"
    file.close()

s = s[:-3]
s += "\n}\n\ndef get_cve_map():\n\treturn __cve_map\n"

out.write(s)
out.close()
