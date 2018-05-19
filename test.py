import sys
import subprocess
import shlex

command_line = input()
args = shlex.split(command_line)
print(command_line, 'john')
#proc = subprocess.Popen('command', shell=False,stdout=PIPE, stdin=PIPE, stderr=STDOUT)
#proc.communicate(b'1')
