import logging
import getpass

import bart
import mylog

# create logger
logger = logging.getLogger("bart-parking")


def main():
    logger.info("Please input your username and password.")
    user = raw_input("Username:")
    password = getpass.getpass()
    logger.info("Done reading username and password")

    bart.get_permit(user, password)
    pass


if __name__ == "__main__":
    main()
