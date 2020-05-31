import logging
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os
import subprocess


def CreateFile(name):
    try:
        if name != "" and name is not None:
            os.system("touch " + str(name))
            return "Created " + str(name)
        else:
            return "can't create a file with empty name"
    except Exception as e:
        return "can't create " + str(name) + " file" + e.__cause__


def CreateDir(name):
    try:
        if name != "" and name is not None:
            os.system("mkdir " + str(name))
            return "Created " + str(name)
        else:
            return "can't create a dir with empty name"
    except Exception as e:
        return "can't create " + str(name) + " \n" + e.__cause__


def RenameFile(old_name, new_name):
    try:
        if new_name != "" and new_name is not None and old_name != "" and old_name is not None:
            os.system("mv " + old_name + " " + new_name)
            return "Now " + str(old_name) + " is " + str(new_name)
        else:
            return "empty option, check"
    except Exception as e:
        return "oops :( " + e.__cause__


def RemoveFile(name):
    try:
        if name != "" and name is not None:
            os.system("rm " + str(name))
            return "Removed " + str(name)
        else:
            return "error, empty name"
    except Exception as e:
        return "can't remove " + str(name) + " file" + e.__cause__


def RemoveFile(name):
    try:
        if name != "" and name is not None:
            os.system("rm " + str(name))
            return "Removed " + str(name)
        else:
            return "error, empty name"
    except Exception as e:
        return "can't remove " + str(name) + " file" + e.__cause__


def RemoveDir(name):
    try:
        if name != "" and name is not None:
            os.system("rmdir " + str(name))
            return "Removed " + str(name)
        else:
            return "error, empty name"
    except Exception as e:
        return "can't remove " + str(name) + " \n" + e.__cause__


def ListDir():
    try:

        return os.listdir()
    except Exception as e:
        return "oops :( " + " \n" + e.__cause__


def ReadFile(name, mode):
    try:
        return open(name, mode)
    except Exception as e:
        return e.__cause__


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('localhost', 5432),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    server.register_function(CreateFile, 'create')
    server.register_function(CreateDir, 'mkdir')
    server.register_function(RenameFile, 'rename')
    server.register_function(RemoveDir, 'rmdir')
    server.register_function(RemoveFile, 'rm')
    server.register_function(ListDir, 'ls')
    server.register_function(ReadFile, 'file')

    # Run the server's main loop
    server.serve_forever()
