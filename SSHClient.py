#!/usr/bin/env python3


import paramiko
import cmd


class RunCommand(cmd.Cmd):
    """Simple shell to run a command on the host"""

    prompt = 'ssh>'

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.hosts = []
        self.connections = []

    def do_add_host(self, args):
        """add_host
        Add the host to the host list"""
        if args:
            self.hosts.append(args.split(','))
        else:
            print("Usage: host")

    def do_connection(self, args):
        """Connect to all hosts in the hosts list"""
        for host in self.hosts:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host[0],
                           username=host[1],
                           password=host[2])
            self.connections.append(client)

    def do_run(self, command):
        """run
        Execute this command on all hosts in the list"""
        if command:
            for host, conn in zip(self.hosts, self.connections):
                stdin, stdout, stderr = conn.exec_command(command)
                stdin.close()
                for line in stdout.read().splitlines():
                    print('hosts: %s %s' % (host[0], line))
        else:
             print("Usage: run")

    def do_close(self, args):
        for conn in self.connections:
            conn.close()


if __name__ == '__main__':
    RunCommand().cmdloop()
