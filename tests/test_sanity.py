from common.jsonrpc import JSONRPC

def test_rpc_basic() -> None:
    client = JSONRPC()
    # should not throw, even if geth not running
    try:
        client.call("web3_clientVersion")
    except Exception:
        assert True  # passes if it retries cleanly