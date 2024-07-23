"""Dune related query fetching for trades is defined here in the DuneTradesFetcher class"""

from typing import Optional

# from datetime import date

from dune_client.client import DuneClient
from dune_client.query import Query
from dune_client.types import QueryParameter, DuneRecord

from src.logger import set_log
from src.models.accounting_period import AccountingPeriod
from src.models.trades import Trade, TradeRequest, TokenTradeInfo, VolumeInfo, Token
from src.queries import QUERIES, QueryData

log = set_log(__name__)


class DuneTradesFetcher:
    """
    Class Contains DuneAPI Instance and Accounting Period along with methods
    for fetching trade data from Dune.
    """

    dune: DuneClient
    period: AccountingPeriod

    def __init__(
        self,
        dune: DuneClient,
        period: AccountingPeriod,
    ):
        self.dune = dune
        self.period = period

    def _period_params(self) -> list[QueryParameter]:
        """Generate query parameters for the accounting period."""
        return [
            QueryParameter.date_type("StartDate", self.period.start),
            QueryParameter.date_type("EndDate", self.period.end),
        ]

    @staticmethod
    def _parameterized_query(
        query_data: QueryData, params: list[QueryParameter]
    ) -> Query:
        return query_data.with_params(params)

    def _get_query_results(
        self, query: Query, job_id: Optional[str] = None
    ) -> list[DuneRecord]:
        """Execute Dune query and return results."""
        log.info(f"Fetching {query.name} from query: {query}")
        if not job_id:
            exec_result = self.dune.refresh(query, ping_frequency=15)
        else:
            exec_result = self.dune.get_result(job_id)

        log.info(f"Fetch completed for execution {exec_result.execution_id}")

        if exec_result.result is not None:
            log.debug(f"Execution result metadata {exec_result.result.metadata}")
        else:
            log.warning(f"No execution results found for {exec_result.execution_id}")
        return exec_result.get_rows()

    def get_trades(
        self, buy_token_address: str, sell_token_address: str
    ) -> list[Trade]:
        """
        Fetches trade data for the specified token pair and accounting period.
        """
        params = self._period_params() + [
            QueryParameter.text_type("BuyTokenAddress", buy_token_address),
            QueryParameter.text_type("SellTokenAddress", sell_token_address),
        ]

        results = self._get_query_results(
            self._parameterized_query(QUERIES["TRADES"], params)
        )

        return [self._create_trade(record) for record in results]

    @staticmethod
    def _create_trade(record: DuneRecord) -> Trade:
        """Create a Trade object from a Dune query result record."""
        trade_request = TradeRequest(
            block_time=record["block_time"],
            tx_hash=record["tx_hash"],
            sell_info=TokenTradeInfo(
                token=Token(record["sell_token_address"]),
                price=float(record["sell_price"]),
                value_usd=float(record["sell_value_usd"]),
            ),
            buy_info=TokenTradeInfo(
                token=Token(record["buy_token_address"]),
                price=float(record["buy_price"]),
                value_usd=float(record["buy_value_usd"]),
            ),
            volume=VolumeInfo(
                units_sold=float(record["units_sold"]),
                atoms_sold=int(record["atoms_sold"]),
            ),
            usd_value=float(record["usd_value"]),
            token_pair=record["token_pair"],
        )
        return Trade(
            block_time=trade_request.block_time,
            tx_hash=trade_request.tx_hash,
            sell_info=trade_request.sell_info,
            buy_info=trade_request.buy_info,
            trade_info=trade_request.volume,
            usd_value=trade_request.usd_value,
            token_pair=trade_request.token_pair,
        )
