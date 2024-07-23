"""
Dune sql query types for cow_protocol_ethereum.trades
"""

from __future__ import annotations

from typing import Optional, Union
from datetime import datetime
from enum import Enum
from dataclasses import dataclass

from dune_client.types import Address


class TradeType(Enum):
    """Classification of Trade Types"""

    BUY = "buy"
    SELL = "sell"

    @classmethod
    def from_str(cls, type_str: str) -> TradeType:
        """Constructs Enum variant from string (case-insensitive)"""
        try:
            return cls[type_str.upper()]
        except KeyError as err:
            raise ValueError(f"No TradeType {type_str}!") from err

    def __str__(self) -> str:
        return str(self.value)


class Token:
    """
    Token class consists of token `address` and additional `decimals` value.
    The constructor exists in a way that we can either
    - provide the decimals (for unit testing) which avoids making web3 calls
    - fetch the token decimals with eth_call.
    """

    def __init__(self, address: Union[str, Address], decimals: Optional[int] = None):
        if isinstance(address, str):
            address = Address(address)
        self.address = address
        self.decimals = decimals

    def __repr__(self) -> str:
        return str(self.address)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Token):
            return self.address == other.address and self.decimals == other.decimals
        return False

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Token):
            return self.address < other.address
        return False

    def __hash__(self) -> int:
        return self.address.__hash__()


@dataclass
class TokenInfo:
    """Represents information about a token in a trade"""

    token: Token
    price: float
    value_usd: float


@dataclass
class VolumeInfo:
    """Represents volume information of a trade"""

    units_sold: float
    atoms_sold: int


@dataclass
class TradeInfo:
    """Represents details of a trade"""

    volume: VolumeInfo
    usd_value: float
    token_pair: str


@dataclass
class Trade:
    """
    Trade class represents a trade with grouped attributes.
    """

    block_time: datetime
    tx_hash: str
    sell_info: TokenInfo
    buy_info: TokenInfo
    trade_info: TradeInfo

    def __repr__(self) -> str:
        return (
            f"Trade(tx_hash={self.tx_hash}, sell_token={self.sell_info.token}, "
            f"buy_token={self.buy_info.token}, units_sold={self.trade_info.volume.units_sold})"
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Trade):
            return self.tx_hash == other.tx_hash
        return False

    def __hash__(self) -> int:
        return hash(self.tx_hash)


@dataclass
class TokenTradeInfo:
    """Represents token-specific trade information"""

    token: Token
    price: float
    value_usd: float


@dataclass
class TradeRequest:
    """Represents all necessary data to create a Trade instance"""

    block_time: datetime
    tx_hash: str
    sell_info: TokenTradeInfo
    buy_info: TokenTradeInfo
    volume: VolumeInfo
    usd_value: float
    token_pair: str


def create_trade(request: TradeRequest) -> Trade:
    """
    Factory method to create a Trade instance

    This method takes a TradeRequest object and creates a Trade instance
    by constructing the necessary TokenInfo and TradeInfo objects.
    """
    sell_info = TokenInfo(
        request.sell_info.token, request.sell_info.price, request.sell_info.value_usd
    )
    buy_info = TokenInfo(
        request.buy_info.token, request.buy_info.price, request.buy_info.value_usd
    )
    trade_info = TradeInfo(request.volume, request.usd_value, request.token_pair)
    return Trade(request.block_time, request.tx_hash, sell_info, buy_info, trade_info)
