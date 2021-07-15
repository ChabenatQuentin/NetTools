import concurrent.futures
import socket
import time


def tcp_con(host, port):
    res = None
    con_port_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con_port_test.settimeout(1)
    conn = con_port_test.connect_ex((host, port))
    if conn == 0:
        res = port
    con_port_test.close()
    return res


def found_ports(host):
    futures = []
    port_up = []
    start_time = time.process_time()
    print(f"Port scanning of host : {host}")
    print("_" * 80)
    with concurrent.futures.ThreadPoolExecutor(max_workers=75) as executor:
        for port in range(1, 65536):
            future = executor.submit(tcp_con, host, port)
            futures.append(future)
        executor.shutdown(wait=True)
        count = 0
        for fut in futures:
            count += 1
            res = fut.result()
            if res is not None:
                port_up.append(res)
            print(f"{100 * count / 65535:.2f}% done")
    print("_" * 80)
    for port in port_up:
        print(f"{port} OPEN")
    print("_" * 80)
    print(f"Process take : {time.process_time() - start_time:.2f}s")
    print(f"Total OPEN port found : {len(port_up)}")


found_ports("127.0.0.1")
