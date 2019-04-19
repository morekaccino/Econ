import os

clear = lambda: os.system('cls')
clear()

stream = open('7.txt', 'r')
stream.seek(0)
source = stream.read().split('\n')
stream.close()

filtered_source = ""
for i in source:
    if ("Parkin" in i and " Macroeconomics" in i and "Tenth Edition" in i) or (
            "Copyright" in i and "Pearson Education" in i and "©" in i):
        pass
    else:
        filtered_source += i + '\n'

# print(filtered_source)
final = []
filtered = filtered_source.split('\n')
temp_q = ""
temp_a = ""
for i in filtered:
    if temp_q != "":
        if ')' in i:
            stand = i.find(')')
            if i[:stand].isdigit():
                final.append(temp_q)
                temp_q = ""
    temp_q += i + '\n'

final2 = []
for i in final:
    elements = i.split('\n')
    ans = ""
    for j in elements:
        if "Answer:" in j:
            ans = j
            i = i.replace(str(j), "")
            final2.append([i, ans])
            continue

startnum = input()
if startnum.isdigit():
    startnum = int(startnum) - 1
else:
    startnum = 0

for question in range(startnum, final2.__len__()):
    print(final2[question][0])
    print(question + 1, 'from', final2.__len__(),"-",str(int(100*(question/final2.__len__())))+'%')
    input()
    print(final2[question][1])
    truth = input()
    if truth != "":
        with open('7-review.txt', 'a+') as f:
            f.write(str(final2[question][0]) +
                    "\n" +
                    str(final2[question][1]) +
                    "\n" +
                    "----------------------------------" +
                    "\n")

    clear()
