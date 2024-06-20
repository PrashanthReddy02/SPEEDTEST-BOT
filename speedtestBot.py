import math
import speedtest

def bytes_to_mb(size_bytes):
    """Convert bytes to megabits per second."""
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} Mbps"

# Create a Speedtest object
wifi = speedtest.Speedtest()

# Get download speed
print("Getting download speed...")
download_speed = wifi.download()
print("Download:", bytes_to_mb(download_speed))

# Get upload speed
print("Getting upload speed...")
upload_speed = wifi.upload()
print("Upload:", bytes_to_mb(upload_speed))

# Get the closest server details
print("Getting server details:")
servers = wifi.get_servers()
wifi.get_best_server()
closest_server = wifi.results.server
print("Closest Server:", closest_server['sponsor'])

# Get ping
ping = wifi.results.ping
print("Ping:", ping, "ms")

# Get client information
print("Getting client information:")
client_info = wifi.results.client
print("IP:", client_info['ip'])
print("ISP:", client_info['isp'])

# Get server information
print("Getting server details:")
server_info = wifi.results.server
print("Server Name:", server_info['sponsor'])
print("Server Location:", server_info['name'])
print("Server Country:", server_info['country'])

# Get raw speed test results
print("Getting raw speed test results:")
speedtest_results = wifi.results.dict()
print(speedtest_results)
