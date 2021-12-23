import subprocess
import os

cp = subprocess.run(["ls", "-l"]) # recommended
print(type(cp))

os.system("whoami")