import subprocess
cmd = "dir"
result=subprocess.run(cmd,shell=True,capture_output=True,text=True)
print(result.stdout)