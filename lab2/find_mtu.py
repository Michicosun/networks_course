#!/usr/bin/env python3

import platform
import subprocess
import argparse
import time

SIZEOF_IP_HEADER = 20
SIZEOF_ICMP_HEADER = 8


def ping(host, packet_size):
    count_of_packets_key = '-c'
    size_of_packets_key = '-s'
    dont_fragment_combination = ['-M', 'do']

    if platform.system().lower() == 'windows':
        count_of_packets_key = '-n'
        size_of_packets_key = '-l'
        dont_fragment_combination = ['-f']

    command = [
        'ping',
        count_of_packets_key, '1',
        size_of_packets_key, str(packet_size),
        '-w', '1',
    ] + dont_fragment_combination + [host]

    return subprocess.call(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    ) == 0


def check_connect(host):
    return ping(host, 0)


def verbose_print(text, verbose_mode, end = '\n'):
    if verbose_mode:
        print(text, end = end, flush=True)


def find_mtu(host, verbose_mode = False):
    verbose_print("checking connectivity...", verbose_mode=verbose_mode, end = " ")

    if not check_connect(host):
        verbose_print("FAIL", verbose_mode=verbose_mode)
        return 0

    verbose_print("SUCCESS", verbose_mode=verbose_mode)

    l = 0
    r = 1501

    while r - l > 1:
        mid = (l + r) // 2

        verbose_print(f'sending ping with size {mid}...\t', verbose_mode = verbose_mode, end = " ")

        if ping(host, mid):
            l = mid
            verbose_print(f"OK, \tcurrent borders: [{l}, {r})", verbose_mode = verbose_mode)
            time.sleep(0.5)
        else:
            r = mid
            verbose_print(f"FAIL, \tcurrent borders: [{l}, {r})", verbose_mode = verbose_mode)

    return l + SIZEOF_IP_HEADER + SIZEOF_ICMP_HEADER


def main():
    parser = argparse.ArgumentParser(description='Find MTU on path to host.')

    parser.add_argument('host', help='hosts for which to determine the optimal MTU')
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()
    host = args.host
    verbose_mode = args.verbose

    mtu = find_mtu(host, verbose_mode)
    print(f"result MTU: {mtu}")



if __name__ == '__main__':
    main()

