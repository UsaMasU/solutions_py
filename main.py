
_str_1 = "Hello World!"

# MAIN #################################################################################################################
if __name__ == '__main__':
    try:

        print(_str_1)
        
        for item in _str_1:
            print(item.capitalize())

    except Exception as e:
        print(f"Error: {e}.")