import argparse
import getpass
import cython


@cython.cfunc
def create_project(args) -> None:
    project_id = hash(args["project"])
    print(f"Creating project {project_id}")
    server_string = input("What is the project location in username@server:port format?\n> ")
    host = server_string.split("@")[1].split(":")[0]
    port = int(server_string.split("@")[1].split(":")[1])
    username = server_string.split("@")[0]
    print(f"Connecting to {host}:{port} as {username}")
    input("Your password will be required. Press enter to continue.")
    password = getpass.getpass()


@cython.cfunc
def download_project(args) -> None:
    print(f"Downloading project {args['project']}")
    print("Tip: Only use Download when you haven't made changes to the project yet.")
    input("Any changes made by collaborators will overwrite your changes. Press enter to continue.")
    print("Downloading files...")
    print("Decompressing files...")
    print("Applying changes...")


@cython.cfunc
def upload_project(args) -> None:
    print(f"Uploading project {args['project']}")
    print("Compressing files...")
    print("Uploading files...")
    print("Applying changes...")


@cython.cfunc
def delete_project(args) -> None:
    print(f"Deleting project {args['project']}")
    input("Any changes made by collaborators will be lost. Press enter to continue.")
    print("Deleting files...")
    print("Deleting project from database...")



commands = {
    "create": create_project,
    "download": download_project,
    "upload": upload_project,
    "delete": delete_project
}

parser = argparse.ArgumentParser(description="Communicate with a Foxtrot server")
parser.add_argument("command", help="The command to run")
parser.add_argument("project", help="The project to use")
args = parser.parse_args()

command = args["command"].lower()
if command not in commands:
    print(f"Unknown command {command}")
    exit(1)

commands[command](args)
