import os
print("All Environment variables", os.environ)
print("Details of only PATH variable ", os.environ['PATH'])
print("Current working directory", os.getcwd())
print("Change of directory")
#os.chdir("home/krish/")
print("os.gtcwd()")
print("Group ID connected with present process",os.getgid())
print("UserID connected with present process", os.getuid())
print("List of group IDS",os.getgroups())
print("Get present process ID",os.getpid())
print("Get present process ID",os.getppid())
print("Execution of system call ps",os.system("ps"))
print("Execution of system call ls -l ",os.system("ls -l"))
