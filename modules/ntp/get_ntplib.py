import ntplib
from datetime import datetime, timezone

def get_ntp_time(ntp_server="pool.ntp.org"):
    try:
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request(ntp_server, version=3)
        
        # Время в формате Unix timestamp (UTC)
        ntp_time = response.tx_time
        
        # Преобразование в читаемый формат
        utc_time = datetime.fromtimestamp(ntp_time, timezone.utc)
        local_time = datetime.fromtimestamp(ntp_time)
        
        print(f"[NTP] Сервер: {ntp_server}")
        print(f"[NTP] Точное время (UTC): {utc_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"[NTP] Локальное время: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        return utc_time
    
    except Exception as e:
        print(f"[Ошибка] Не удалось получить время: {e}")
        return None

if __name__ == "__main__":
    get_ntp_time()