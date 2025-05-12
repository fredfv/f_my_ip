#!/usr/bin/env python3
import argparse
import logging
import sys
from typing import Optional

import requests

try:
    import pyperclip
    PYPERCLIP_AVAILABLE = True
except ImportError:
    PYPERCLIP_AVAILABLE = False

DEFAULT_SERVICE_URL = 'https://api.ipify.org'


def get_external_ip(url: str = DEFAULT_SERVICE_URL, timeout: int = 5) -> Optional[str]:
    """
    Fetches the external IP address from the specified service URL.

    :param url: The endpoint to query for the external IP.
    :param timeout: Timeout for the HTTP request in seconds.
    :return: The external IP as a string, or None on failure.
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as err:
        logging.error(f"Failed to retrieve external IP from {url}: {err}")
        return None


def copy_to_clipboard(text: str) -> None:
    """
    Copies the given text to the system clipboard, if pyperclip is available.

    :param text: The text to copy.
    """
    if not PYPERCLIP_AVAILABLE:
        logging.warning("pyperclip is not installed; skipping clipboard copy.")
        return

    try:
        pyperclip.copy(text)
        logging.info("IP address copied to clipboard.")
    except pyperclip.PyperclipException as err:
        logging.error(f"Clipboard copy failed: {err}")


def parse_args() -> argparse.Namespace:
    """
    Parses command-line arguments.

    :return: An argparse Namespace containing URL and timeout.
    """
    parser = argparse.ArgumentParser(
        description='Fetch and copy the external IP address.'
    )
    parser.add_argument(
        '-u', '--url',
        default=DEFAULT_SERVICE_URL,
        help=f"Service URL for IP lookup (default: {DEFAULT_SERVICE_URL})"
    )
    parser.add_argument(
        '-t', '--timeout',
        type=int,
        default=5,
        help='Request timeout in seconds (default: 5)'
    )
    return parser.parse_args()


def main() -> None:
    """
    Main entry point: configures logging, retrieves the IP, and handles output.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s'
    )

    args = parse_args()
    ip = get_external_ip(args.url, args.timeout)

    if ip:
        logging.info(f"External IP: {ip}")
        copy_to_clipboard(ip)
        # Also print IP for piping or immediate visibility
        print(ip)
        sys.exit(0)
    else:
        logging.error("Could not determine external IP.")
        sys.exit(1)


if __name__ == '__main__':
    main()
