import getpass
import paramiko
import time


ssh_command = ("show version | i 'Operating System'")

def banner():
    print (60 * "#")
    print ("")
    print (20 * " " + "SSH LOGIN SCRIPT")
    print ("")
    print ("")
    print (10 * " " + "This script will do the following command ")
    print ("")
    print (10 * " " + ssh_command)
    print ("")
    print (60 * "#")
    print ("")
    print ("")

def host_check_quest():
    host_check_menu = True
    while host_check_menu not in ("yes", "no"):
        print("Would you like to see the hostlist *RECOMMENDED* ")
        answer = input("yes/no: ")
        if answer == "yes":
            print (60 * "#")
            with open("hosts.txt") as file:
                for item in file:
                    print(str(item.strip()))
            print (60 * "#")

            print("Would you like to continue with this script?  ")
            after_check_answer = input("yes/no: ")
            if after_check_answer == "yes":
                print (60 * "#")
                print(20 * " " + "starting script")
                time.sleep(1)
                break
            elif after_check_answer == "no":
                print (20 * " " +"exiting script")
                time.sleep(1)
                exit()
            break
        elif answer ==  "no":
            print (60 * "#")
            print (20 * " " + "starting script")
            time.sleep(1)
            break
        else: 
        	print("Please enter yes or no.\n ")




def ssh_trying():
    
    global ssh_command

    print("")
    print("Please enter your username and password")
    print("")
    username = input("Enter a username ")
    password = getpass.getpass()
    print("")

    with open("hosts.txt") as file:
        for item in file:
            try:
                print ("### connecting to " + str(item.strip()) + " ###")
                server = str(item.strip())
                ssh = paramiko.SSHClient()
                ssh.load_system_host_keys()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(server, username=username, password=password, timeout=4)
                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(ssh_command)
                output = ssh_stdout.readlines()
                ssh.close
                print ("Output of " + str(item.strip()) + " " + str(output))

            except paramiko.AuthenticationException:
                print (str(item.strip()) + " [-] Authentication failed! ...")
            except paramiko.SSHException:
                print (str(item.strip()) + " [-] SSH Exception! ..." )
            time.sleep(4)
            except Exception as e:
                print (e)
    
banner()
host_check_quest()
ssh_trying()
