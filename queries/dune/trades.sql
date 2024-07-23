SELECT block_time, tx_hash, sell_token_address, sell_token,
       buy_token_address, buy_token, token_pair,
       units_sold, atoms_sold, usd_value,
       buy_price, buy_value_usd, sell_price, sell_value_usd
FROM cow_protocol_ethereum.trades
WHERE block_date BETWEEN DATE '{{StartDate}}' AND DATE '{{EndDate}}'
AND buy_token_address = '{{BuyTokenAddress}}'  -- WETH
AND sell_token_address = '{{SellTokenAddress}}';  -- USDC
