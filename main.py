import sys
from modules.ntp.get_ntp import get_ntp_time

_str_1 = "Hello World!"
_settings = {
    'one': '1',
    'two': '2',
    'three':'3'
}

# MAIN #################################################################################################################
if __name__ == '__main__':
    try:

        print(f"{_str_1}\n") 
        for item in _str_1:
            print(item.capitalize())
        
        print()
        
        for key, val in _settings.items():
            print(f"{key}:{val}")

        print()
        if len(sys.argv) < 2:
            time = get_ntp_time()
        else:
            time = get_ntp_time(sys.argv[1])




    except Exception as e:
        print(f"Error: {e}.")