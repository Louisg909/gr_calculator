from colorama import Fore, Style, init
def debug(display_text):
    init()
    print(f"{Fore.RED}{Style.BRIGHT}Debugging: {Style.RESET_ALL}{display_text}")

def debug_function(func):
    def wrapper(*args, **kwargs):
        print(f"{Fore.RED}{Style.BRIGHT}Debuging function: {Style.RESET_ALL}{func.__name__}")
        result = func(*args, **kwargs)
        print(f"{Fore.RED}{Style.BRIGHT}\t{func.__name__} returned: {Style.RESET_ALL}{result}")
        return result
    return wrapper
