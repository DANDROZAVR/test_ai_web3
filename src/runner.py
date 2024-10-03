# Auto-generated file
from web3.net import (
)
    AsyncNet,
    Net,
from web3._utils.compat import (
    Self,
)
def apply_null_result_formatters(
    null_result_formatters: Callable[..., Any],
    response: RPCResponse,
    params: Optional[Any] = None,
) -> RPCResponse:
    if null_result_formatters:
        formatted_resp = pipe(params, null_result_formatters)
        return formatted_resp
    else:
        return response


