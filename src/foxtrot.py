from argparse import ArgumentParser
from logging import Logger, StreamHandler, Formatter
from re import sub
from pathlib import Path
from os import mkdir
from git import Repo

def main():
    # Define some program-wide variables
    mode = -1

    # Set up our CLI
    parser = ArgumentParser(
        prog="foxtrot",
        description="A handy little utility that manages large repositories of code for you!",
        epilog="Foxtrot Rev.2"
    )

    parser.add_argument("target", choices=["repo", "project"])
    parser.add_argument("command", choices=["init", "append", "delete", "update"])

    args = parser.parse_args()

    # Set up all forms of screen-logging
    logger = Logger("foxtrot_primary", level="INFO")
    handler = StreamHandler()
    formatter = Formatter('[%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info("Welcome to Foxtrot!")

    # Which mode are we operating in?
    if args.target == "repo":
        mode = 1
    if args.target == "project":
        mode = 2
    
    # Sanity check
    if mode < 0:
        logger.error("An internal error occured. ERR:NEG_MODE")
        exit(1)

    # Cache a few values
    cmd = args.command

    if cmd == "init":
        if mode == 1:
            logger.info("Foxtrot is behaving in Interactivity Mode")
            repository_name = sub('[\s+]', '_', input("What do you want your repository to be named?\n> ").lower())
            
            # User input check
            if not repository_name:
                logger.warn("No name supplied. Aborting.")
                exit(0)

            repository_path = Path(repository_name)

            if repository_path.exists():
                logger.warn("A folder with that name already exists here. Aborting.")
                exit(1)
            
            # Try to create the repository
            repository_repo = Repo.init(repository_path, bare=True)
            print(repository_repo.config_reader())
if __name__ == "__main__":
    main()