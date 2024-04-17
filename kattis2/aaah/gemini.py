jon_aah = input()
doc_aah = input()
if jon_aah[-1] == 'h' and doc_aah[-1] == 'h':
    print("go")
elif jon_aah[:-1] == doc_aah[:-1]:
    print("go")
else:
    print("no")