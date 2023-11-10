# Programmer: Mmdrza.Com

# Import modules
from .utils import Convertor, Generator
from .hd import (
    Axe,
    Bitcoin,
    BitcoinGold,
    Dash,
    DigiByte,
    Dogecoin,
    Ethereum,
    Litecoin,
    Qtum,
    Ravencoin,
    Tron,
    Zcash
)

# Metadata
__version__ = "v3.9.6"
__license__ = "MIT"
__author__ = "Mohammadreza (MMDRZA)"
__email__ = "PyMmdrza@gmail.com"
__description__ = ("Generated and Converted Keys with any Type Foundation from "
                   "Private Key [WIF Hexed Mnemonic and Binary Bytes seed] in Python")

# Publicly exposed elements
__all__ = [
    # Metadata
    "__version__",
    "__license__",
    "__author__",
    "__email__",
    "__description__",

    # Core modules
    "Wallet",
    "assest",
    "bs58",
    "utils",
    "hd",
    "CLI",
    
    # Classes
    "Convertor",
    "Generator",

    # Blockchain-specific classes
    "Axe",
    "Bitcoin",
    "BitcoinGold",
    "Dash",
    "DigiByte",
    "Dogecoin",
    "Ethereum",
    "Litecoin",
    "Qtum",
    "Ravencoin",
    "Tron",
    "Zcash"
]
