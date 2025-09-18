import sys
import socket
import struct
from datetime import datetime, timezone


def get_ntp_time(ntp_server="pool.ntp.org"):
# time from NTP-server like: time.google.com, pool.ntp.org
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(3)
        data = b'\x1b' + 47 * b'\0'
        client.sendto(data, (ntp_server, 123))
        response, _ = client.recvfrom(1024)
        
        if response:
            t = struct.unpack("!12I", response)[10]
            t -= 2208988800  # Convert NTP time to Unix epoch
            print(f"Время полученное от сервера {ntp_server}")
            utc_time = datetime.fromtimestamp(t, timezone.utc)
            print(f"[NTP] Время (UTC): {utc_time.strftime('%Y-%m-%d %H:%M:%S')}")
            return utc_time
    
    except Exception as e:
        print(f"[Ошибка] {e}")
        return None


if __name__ == "__main__":    
    if len(sys.argv) < 2:
        time = get_ntp_time()
    else:
        time = get_ntp_time(sys.argv[1])
