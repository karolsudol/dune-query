"""
Localized account of all Queries related to this project's main functionality
"""

from __future__ import annotations

from copy import copy
from dataclasses import dataclass
from typing import List

from dune_client.types import QueryParameter


class Query:
    """Placeholder for Dune Query class"""

    def __init__(self, query_id: int, name: str):
        self.query_id = query_id
        self.name = name
        self.params: List[QueryParameter] = []

    def set_params(self, params: List[QueryParameter]) -> None:
        """Set the parameters for the query."""
        self.params = params

    def get_query_info(self) -> str:
        """Get a string representation of the query information."""
        return f"Query(id={self.query_id}, name='{self.name}', params_count={len(self.params)})"


@dataclass
class QueryData:
    """Stores name and a version of the query for each query."""

    name: str
    query: Query

    def __init__(self, name: str, query_id: int, filepath: str) -> None:
        self.name = name
        self.filepath = filepath
        self.query = Query(query_id, name)

    def with_params(self, params: List[QueryParameter]) -> Query:
        """Copies the query, adds parameters, returning the copy."""
        query_copy = copy(self.query)
        query_copy.set_params(params)
        return query_copy


QUERIES = {
    "TRADES": QueryData(
        name="Trades for Token Pair",
        filepath="trades.sql",
        query_id=0,
    ),
}
