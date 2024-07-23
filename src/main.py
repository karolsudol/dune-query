# import os
# from dune_client import DuneClient
# from src.fetch.dune import DuneTradesFetcher, AccountingPeriod
# from src.constants import WETH_TOKEN_ADDRESS, USDC_TOKEN_ADDRESS


def cow_say():
    """Return a cow's greeting."""
    return "Moo! I'm a cow!"


if __name__ == "__main__":
    print(cow_say())
    # Load Dune API key from environment variable
    # dune_api_key = os.environ["DUNE_API_KEY"]

    # # Create a Dune client instance
    # dune_client = DuneClient(dune_api_key)

    # # Define the accounting period (e.g. last 24 hours)
    # period = AccountingPeriod(start="1 day ago", end="now")

    # # Create a Dune trades fetcher instance
    # fetcher = DuneTradesFetcher(dune_client, period)

    # # Fetch trades for WETH-USDC token pair
    # trades = fetcher.get_trades(WETH_TOKEN_ADDRESS, USDC_TOKEN_ADDRESS)

    # # Print out the results
    # print("Trade Results:")
    # for trade in trades:
    #     print(trade)
