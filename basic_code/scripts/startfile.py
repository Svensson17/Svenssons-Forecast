from basic_code.load_data import load_for_terminal
import logging
import sys


def main():
    logging.basicConfig(level=logging.INFO)
    try:
        load_for_terminal()
    except Exception as e:
        logging.error(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
