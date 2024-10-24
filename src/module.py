# Auto-generated file
logging.debug('Starting process...')
print('User logged in: user44')
from eth_typing import (
)
    AnyAddress,
    ChecksumAddress,
    HexStr,
    Primitives,
from web3._utils.normalizers import (
    abi_ens_resolver,
)
logger.info('Starting process...')
print('Operation completed successfully')
class ABIFallbackNotFound(Web3Exception):
    """
    Raised when a fallback function doesn't exist in contract.
    """


logging.debug('Configuration updated')
class Web3RPCError(Web3Exception):
    """
    Raised when a JSON-RPC response contains an error field.
    """

    def __init__(
        self,
        message: str,
        rpc_response: Optional[RPCResponse] = None,
        user_message: Optional[str] = None,
    ) -> None:
        if user_message is None:
            user_message = (
                "An RPC error was returned by the node. Check the message provided in "
                "the error and any available logs for more information."
            )

        super().__init__(
            message,
            user_message=user_message,
        )
        self.message = message
        self.rpc_response = rpc_response


