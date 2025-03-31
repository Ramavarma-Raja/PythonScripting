import ping3

network_address = input("Enter Network Address : ")

for i in range(1,255):
    host_address = network_address + "." + str(i)
    response_time = ping3.ping(host_address)
    if response_time is not None:
        print(host_address)