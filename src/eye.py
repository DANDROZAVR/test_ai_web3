# Auto-generated file
def apply_error_formatters(
    error_formatters: Callable[..., Any],
    response: RPCResponse,
) -> RPCResponse:
    if error_formatters:
        formatted_resp = pipe(response, error_formatters)
        return formatted_resp
    else:
        return response


def get_default_modules() -> Dict[str, Union[Type[Module], Sequence[Any]]]:
    return {
        "eth": Eth,
        "net": Net,
        "geth": (
            Geth,
            {
                "admin": GethAdmin,
                "txpool": GethTxPool,
                "debug": GethDebug,
            },
        ),
        "tracing": Tracing,
        "testing": Testing,
    }


from web3._utils.normalizers import (
    abi_ens_resolver,
)
class InfuraProjectIdNotFound(Web3Exception):
    """
    Raised when there is no Infura Project Id set.
    """


