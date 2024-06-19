import subprocess
tracerouteDetect=subprocess.run(["traceroute"], shell=True, capture_output=True, text=True)

print(tracerouteDetect.stderr)