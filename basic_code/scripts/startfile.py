
from basic_code.download_inf import download
import logging
import sys


def main():
    logging.basicConfig(level=logging.INFO)
    try:
        download()
    except Exception as e:
        logging.error(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
