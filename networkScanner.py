import ping3

network_address = input("Enter Network Address : ")

for host in range(1,255):
    target_address = network_address + "." + str(host)
    response_time = ping3.ping(target_address)
    if response_time is not None:
        print(target_address)
