import requests
import logging

logging.basicConfig(
    filename="fetched.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def fetch(url):
    response = requests.get(url)    # fetch("https://api.publicapis.org/entries")
    if response.status_code == 200:
        data = response.json()
        logging.info(f"Api call {url} successful")
        return data["count"]
    return "wrong url"

def multiply(a: int, b: int) -> int:
    """multiply 2 nos.
    Args:
        a (int): num1
        b (int): num2
    Returns:
        int: returns an int that is multipied.
    """
    return a * b

# TODO: Add your code here..
