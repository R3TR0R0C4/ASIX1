import subprocess

"""testPing=subprocess.run(["ping 192.168.0.250 -c 2"], shell=True, capture_output=True, text=True)
print("-----ping1:-----")
print(testPing.stdout)
print(testPing.returncode)
print("-----ping1:-----")"""
testPing2=subprocess.run(["ping 1.1.1.1 -c 2"], shell=True, capture_output=True, text=True)
print("-----ping2:-----")
print(testPing2.stdout)
print(testPing2.returncode)
print("-----ping2:-----")



if testPing2.returncode == "2":
    print("Codi 2")