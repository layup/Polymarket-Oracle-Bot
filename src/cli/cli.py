import asyncio
import os


import argparse
import logging
import sys

from dotenv import load_dotenv
from logger import logger

from py_clob_client.client import ClobClient
from py_clob_client.constants import POLYGON


private_key = os.getenv('PK')
host = "https://clob.polymarket.com"
chain_id = POLYGON

async def get_polymarket_markets():

    client = None
    try:
        client = ClobClient(host, key=private_key, chain_id=chain_id)
        print("Initialized Polymarket ClobClient.")

        sample = client.get_sampling_markets()
        #rint(sample)

    except Exception as e:
        print(f"An error occurred: {e}")



def main():

    parser = argparse.ArgumentParser(
        description="Control the Polymarket Oracle Bot via CLI",
        epilog="Use -h or --help for command-specific help.",
    )

    # Subparsers for different commands
    subparsers = parser.add_subparsers(title="Commands", dest="command")

    # 'start' command
    start_parser = subparsers.add_parser("start", help="Start the bot.")
    start_parser.add_argument(
        "-d", "--daemon", action="store_true", help="Run in daemon mode (background)."
    )

    stop_parser = subparsers.add_parser("stop", help="Stop the bot.")

    query_parser = subparsers.add_parser("query", help="Query market data.")
    query_parser.add_argument("market_id", type=str, help="Market ID to query.")

    status_parser = subparsers.add_parser("status", help="Get the bot's status.")

    # Global options (can be used with any command)
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output."
    )


    while True:
        try:
            command_line = input(">").split()  #
            logger.info(f'command_line: {command_line}')

            if not command_line:
                continue

            if command_line[0].lower() in ['exit', 'exit()']:
                print("Exiting CLI.")
                break

            args = parser.parse_args(command_line)  # Parse the command
            logger.info(f"CLI started with arguments: {args}")


            if args.command == "start":
                if args.daemon:
                    logger.info("Starting bot in daemon mode")
                    print('starting bot in the foreground')

                else:
                    logger.info("Starting bot in foreground")
                    print('starting bot in the foreground')

            elif args.command == "stop":
                logger.info("Stopping bot")
                print("Stopping bot")

            elif args.command == "query":
                logger.info(f"Querying market {args.market_id}")
                print(f"Querying market {args.market_id}")


            elif args.command == "status":
                logger.info("Getting bot status")
                print("Getting bot status")

            else:
                parser.print_help()  # Show help if no command is given

        except SystemExit:  # Catch the exception that print_help() raises
            pass

        except Exception as e:
            logger.error(f"Error: {e}", exc_info=True)
            break


def main_2():
    logger.info(f'running log test')

    parser = argparse.ArgumentParser(prog="pm-trade")
    parser.add_argument('-g', help='User supplied gas price (in gwei)', type=int)

    client = None




    while True:
        try:
            client = ClobClient(host, key=private_key, chain_id=chain_id)
            print("Initialized Polymarket ClobClient.")

            sample = client.get_sampling_markets()
            #print(sample[0])

        except Exception as e:
            print(f"An error occurred: {e}")


