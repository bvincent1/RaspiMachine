import subprocess as sub
from sys import argv

def killProcess(pid, bang=False):
	if bang:
		sub.call(['kill','-9', pid])
	else:
		sub.call(['kill', pid])
			
def isRunning(name):
	processes = sub.check_output(['ps','ax']).decode('utf-8').split('\n')
	for proc in processes:
		if proc.count(name):
			return proc.split(' ')[1]
	return ''

if __name__ == "__main__":
	if len(argv) > 1:
		status = isRunning(argv[1])
		killProcess(status)
		status2 = isRunning(argv[1]):
		if status2 != '':
			killProcess(status2, bang=True)
