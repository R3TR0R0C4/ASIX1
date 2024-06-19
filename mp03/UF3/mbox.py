"""
man_a = open('mbox-short.txt')
for linia in man_a:
    linia = linia.rstrip()
    if linia.startswith('From:'):
        print(linia)"""


"""man_a = open('mbox-short.txt')
for linia in man_a:
    linia = linia.rstrip()
    if linia.find('@uct.ac.za') == -1:continue
    print(linia)"""

man_a = open('mbox-short.txt')
for linia in man_a:
    linia = linia.rstrip()
    if linia.startswith('From:') and linia.find('@uct.ac.za') !=-1:
        #if linia.find('@uct.ac.za') == -1:continue
        print(linia)