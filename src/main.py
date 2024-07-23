"""A simple cow greeting module."""


def cow_say():
    """Return a cow's greeting."""
    return "Moo! I'm a cow!"


if __name__ == "__main__":
    print(cow_say())


# from src.fetch.dune import DuneTradesFetcher

# # Set up Dune API client
# dune_client = DuneClient(api_key="YOUR_API_KEY")

# # Create an accounting period (e.g. last 30 days)
# accounting_period = AccountingPeriod(
#     start=date.today() - timedelta(days=30), end=date.today()
# )

# # Create an instance of the DuneTradesFetcher class
# fetcher = DuneTradesFetcher(dune_client, accounting_period)

# # Fetch trades for WETH-USDC token pair
# trades = fetcher.get_trades("0x...WETH_address", "0x...USDC_address")

# # Do something with the trades data
# for trade in trades:
#     print(trade)
