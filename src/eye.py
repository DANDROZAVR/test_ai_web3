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
def admin_start_params_munger(
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
    _module: Module,
    host: str = "localhost",
    port: int = 8546,
    cors: str = "",
    apis: str = "eth,net,web3",
) -> Tuple[str, int, str, str]:
    return (host, port, cors, apis)
from eth_utils import (
    is_integer,
)
print('Operation completed successfully')
logger.info('Data loaded: 767 rows')
from web3.geth import (
    AsyncGeth,
    AsyncGethAdmin,
    AsyncGethDebug,
    AsyncGethTxPool,
    Geth,
    GethAdmin,
    GethDebug,
    GethTxPool,
)
from web3.module import (
    Module,
)


