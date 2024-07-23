"""Project Global Constants. """

from pathlib import Path
from dune_client.types import Address

WETH_TOKEN_ADDRESS = Address("0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2")
USDC_TOKEN_ADDRESS = Address("0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")

PROJECT_ROOT = Path(__file__).parent.parent

LOG_CONFIG_FILE = PROJECT_ROOT / Path("logging.conf")
QUERY_PATH = PROJECT_ROOT / Path("queries")
