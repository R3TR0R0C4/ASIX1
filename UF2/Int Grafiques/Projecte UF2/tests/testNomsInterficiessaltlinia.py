import subprocess

velocitat=subprocess.run([f"ethtool enp2s0 | grep Speed: |awk"" 'FNR==1{print$2}'"], shell=True, capture_output=True, text=True)

linkSpeed = velocitat.stdout #Guardem link speed
print(velocitat)
linkSpeed=linkSpeed.replace("\n", "")
print(linkSpeed)
