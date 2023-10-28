import requests
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        bitcoin_rate = o["bpi"]["USD"]["rate_float"]
        result = n * bitcoin_rate
        print(f"${result:,.4f}")

if __name__ == "__main__":
    main()

