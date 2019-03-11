from paramiko import client

class Ssh:
    client = None

    def __init__(self, host, port, username, password):
        print("Connecting to the host " + host + " with user: " + username + " and password: " + password + ".")
        # We are creating new SSH client
        self.client = client.SSHClient()
        # Following line is for make the connection possible to server that is not in the known_hosts yet
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        # Then we make a connection
        self.client.connect(host, port=port,username=username, password=password, look_for_keys=False)
        print("Connection is established!")

    def sendCommand(self, command):
        # Check if connection was made previously
        if (self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print stdout data when available
                if stdout.channel.recv_ready():
                    # Retrieve the first 1024 bytes
                    alldata = stdout.channel.recv(1024)
                    while stdout.channel.recv_ready():
                        # Retrieve the next 1024 bytes
                        alldata += stdout.channel.recv(1024)

                    # Print as string with utf8 encoding
                    print(str(alldata))
            print("Connection to the given host was closed.")

        else:
            print("Connection were not established.")

