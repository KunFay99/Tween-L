import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pkg install python")
    os.system("pkg install python2")
    os.system("pkg install python3")
    os.system("pkg install slowloris")
    

c = input(">>>: ")
if c == "1":
    os.system("pkg install python")
    os.system("pkg install python2")
    os.system("pkg install python3")
    os.system("pkg install slowloris")
    
print("Done.")
