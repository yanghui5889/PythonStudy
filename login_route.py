import paramiko

def qytang_ssh(ip,username,password,port=22,cmd='show ip int bri'):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode()

if __name__ == '__main__':
    # print(qytang_ssh('192.168.79.254','root','nihao123!'))
    print(qytang_ssh('192.168.79.254','root','nihao123!',cmd='show ip int bri'))
