import concurrent.futures
import ipaddress
import math
import subprocess
import platform
import time
from icmplib import ping

import errorHandling


def ping_ip(addr):
    host = ping(addr, count=1, timeout=2.5)
    if host.is_alive:
        return addr
    return None


def found_ip(net_cidr):
    ip_up = []
    futures = []
    nb_ip = math.pow(2, 32 - int(net_cidr.split("/")[1]))
    start_time = time.process_time()
    print(f"Ip scanning of {net_cidr} network")
    print("_" * 80)
    ip_done = 0
    try:
        net = ipaddress.ip_network(net_cidr)
        with concurrent.futures.ThreadPoolExecutor(max_workers=75) as executor:
            for addr in net:
                future = executor.submit(ping_ip, str(addr))
                futures.append(future)
                ip_done += 1
                print(f"{100 * ip_done / nb_ip:.2f}% done")
            not_done = ['not_nul']
            done = []
            while len(not_done) != 0:
                done, not_done = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)
                ip_done = len(done)
                print(f"{100 * ip_done / nb_ip:.2f}% done")
                time.sleep(2)
            for fut in done:
                res = fut.result()
                if res is not None:
                    ip_up.append(str(res))
        # for fut in concurrent.futures.as_completed(futures):
        #    res = fut.result()
        #    if res is not None:
        #        ip_up.append(str(res))
        #    ip_done += 1
        #    print(f"{100 * ip_done / nb_ip}% done")
        print("_" * 80)
        for ip in ip_up:
            print(f"{ip} UP")
        print("_" * 80)
        print(f"Process take : {time.process_time() - start_time:.2f}s")
        print(f"Total IP found : {len(ip_up)}")
    except ValueError as e:
        print(e)


found_ip("192.168.0.0/16")
