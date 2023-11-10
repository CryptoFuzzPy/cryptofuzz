

![](https://raw.githubusercontent.com/CryptoFuzzPy/.github/main/profile/media/Cryptofuzz_Header.png)


# CryptoFuzz



## Installing & Quick Use

### Windows

On Windows, you can install CryptoFuzz using the following pip command:

```bash
pip install cryptofuzz
```

### Linux & Mac

On Linux and macOS, you should use pip3 for installation:

```bash
pip3 install cryptofuzz
```

### Git

To use the latest version from the source, you can clone the CryptoFuzz repository:

1. Clone the repository:

```bash
git clone https://github.com/Pymmdrza/cryptofuzz
```

2. Navigate to the cloned directory:

```bash
cd cryptofuzz
```

3. Install the package:

### Windows

You can either run the `install.bat` or `install` command:

```bash
./install.bat
# or
./install
```

### Linux & Mac

On Linux and Mac, you can use the following commands to install:

```bash
bash install.sh
# or simply:
./install.sh
```

**Note:** If you face any permission issues on Linux, make the script executable using:

```bash
sudo chmod +x install.sh
```
---
### CLI

generated and converted private key (hex) , bytes (seed), wif compressed and uncompressed and mnemonic , Root Key (xprv) , XPUB, Decimal (Number) , Public Key and Binary To Compressed and Uncompressed Bitcoin Address :

- Generated Option : `--generate` and `-g`
- Total Generated and convereted Key Option: `--total`, `-t` (integer/number type)
- Saved all Details and full information to `JSON file (OutputFile.json)` option `--save` and `-s`
this example just generated `1000` key without save details
```shell
# windows
cryptofuzz --generate --total 1000
# linux & mac
cryptofuzz --generate --total 1000
```
example Generated `1000` Key and saved to `OutputFile.json`:
```shell
# windows
cryptofuzz -g -t 1000 -s
# linux & mac
cryptofuzz --generate --total 1000 --save
# or can use : -g -t 1000 -s
```
**Run this command anywhere in your system (in any Path folder) Saved `OutputFile.json`**


create with CryptoFuzz, you can see from the `example` section with the following `cryptofuzz-example` command in your terminal:


#### Generated example Private Key From CLI `cryptofuzz-example` :


all option command for windows `cryptofuzz-example OPTION` and Linux or Mac `cryptofuzz-example OPTION` :

- Generated `private key` (hex) & Converted : `cryptofuzz-example privatekey`
- Generated `bytes` & Converted : `cryptofuzz-example bytes`
- Generated `mnemonic` & Converted : `cryptofuzz-example mnemonic`
- Generated `wif` & Converted : `cryptofuzz-example wif`
- Generated `binary` & Converted : `cryptofuzz-example binary`
- Generated Root Key (`xprv`) & Converted : `cryptofuzz-example xprv`
- Generated `decimal` & Converted : `cryptofuzz-example decimal`

Generated and Converted Private Key (HEX) To another cryptocurrency:
- Generated Private Key (Hex) and Converted To Ethereum Address [Example command]:
```shell
# windows
cryptofuzz-example ethereum
# linux and macOs:
cryptofuzz-example ethereum
```
- Generated Private Key (Hex) and Converted To bitcoin Address [Example command]:
```shell
# windows
cryptofuzz-example bitcoin
# linux and macOs:
cryptofuzz-example bitcoin
```
- Generated Private Key (Hex) and Converted To dash Address [Example command]:
```shell
# windows
cryptofuzz-example dash
# linux and macOs:
cryptofuzz-example dash
```
- Generated Private Key (Hex) and Converted To dogecoin Address [Example command]:
```shell
# windows
cryptofuzz-example dogecoin
# linux and macOs:
cryptofuzz-example dogecoin
```
- Generated Private Key (Hex) and Converted To digibyte Address [Example command]:
```shell
# windows
cryptofuzz-example digibyte
# linux and macOs:
cryptofuzz-example digibyte
```
- Generated Private Key (Hex) and Converted To Bitcoin Gold Address [Example command]:
```shell
# windows
cryptofuzz-example bitcoingold
# linux and macOs:
cryptofuzz-example bitcoingold
```
- Generated Private Key (Hex) and Converted To qtum Address [Example command]:
```shell
# windows
cryptofuzz-example qtum
# linux and macOs:
cryptofuzz-example qtum
```
- Generated Private Key (Hex) and Converted To zcash Address [Example command]:
```shell
# windows
cryptofuzz-example zcash
# linux and macOs:
cryptofuzz-example zcash
```
- Generated Private Key (Hex) and Converted To Ravencoin Address [Example command]:
```shell
# windows
cryptofuzz-example rvn
# linux and macOs:
cryptofuzz-example rvn
```
- Generated Private Key (Hex) and Converted To Litecoin Address [Example command]:
```shell
# windows
cryptofuzz-example litecoin
# linux and macOs:
cryptofuzz-example litecoin
```

---

### Private Key

generated random private key without repeat :

```python
from cryptofuzz import getPrivateKey

Privatekey = getPrivateKey()
```
---
### Mnemonic
Generated random mnemonic with standard size :
```python
from cryptofuzz import getMnemonic
# default size 12 . can use [12, 18, 24]
mnemonicString = getMnemonic(size=12)
```
----
### Bytes (seed)

Generated Random Bytes Without Repeat :

```python
from cryptofuzz import getBytes
byte = getBytes()
```
---
### Binary
Generate Random Binary Without repeat `0/1`:

```python
from cryptofuzz import getBin

binary_string = getBin(256)
```
---
### Private Key To Bytes
```python
from cryptofuzz import PrivateKey_To_Bytes

privatekey = getPrivateKey()
# Convert Private Key HEX To Bytes SEED
byte = PrivateKey_To_Bytes(privatekey)

```
---
### Private Key To Wif

generated private key (hex) and convert to wif compressed and uncompressed.
```python
from cryptofuzz import getPrivateKey, PrivateKey_To_Wif

privatekey = getPrivateKey()
# Convert Private key Hex To Wif
#  compressed
wif_compress = PrivateKey_To_Wif(privatekey, compress=True)
# wif Uncompressed
wif_uncompress = PrivateKey_To_Wif(privatekey, compress=False)
```
---
### Private Key To Mnemonic

```python
from cryptofuzz import getPrivateKey, PrivateKey_To_Mnemonic

privatekey = getPrivateKey()
# convert private key [hex] To mnemonic
mnemonic_string = PrivateKey_To_Mnemonics(privatekey)
# for size mnemonic can use [12, 18, 24]
```
---
### Private Key To Binary

```python
from cryptofuzz import getPrivateKey, PrivateKey_To_Binary

privatekey = getPrivateKey()

# convert hex to bin
binary_string = PrivateKey_To_Binary(privatekey)
```
---
### Private Key To Decimal (int)
```python
from cryptofuzz import getPrivateKey, PrivateKey_To_Decimal

privatekey = getPrivateKey()
# convert private key hex to number (dec)
dec = PrivateKey_To_Decimal(privatekey)
```
---
### Private Key To Address

convert private key `Hex` to Compress and Uncompress Address
```python
from cryptofuzz import getPrivateKey, PrivateKey_To_Wif

privatekey = getPrivateKey()
# convert private key to compress address
compress_Address = PrivateKey_To_Address(privatekey, compress=True)
# convert to uncompress address
uncompress_Address = PrivateKey_To_Address(privatekey, compress=False)
```
---
### Private Key To Public Key

generated private key and convert to public key compress and uncompress:

```python
from cryptofuzz import getPrivateKey, PrivateKey_To_PublicKey

privatekey = getPrivateKey()
# convert to public key uncompress
public_uncompress = PrivateKey_To_PublicKey(privatekey)
# convert private key hex to public key compress
public_compress = PrivateKey_To_PublicKey(privatekey, compress=True)
```
---
### Bytes To Private Key
```python
from cryptofuzz import getBytes, Bytes_To_PrivateKey

byte = getBytes()
# convert bytes to hex (private key)
privatekey = Bytes_To_PrivateKey(byte)
```
### Bytes To mnemonic 
convert bytes to mnemonic with default `size=12`

can use standard sizr: `12, 18, 24`

```python
from cryptofuzz import getBytes, Bytes_To_Mnemonic

byte = getBytes()
# Convert bytes to mnemonic with default size 12
mnemonic_words = Bytes_To_Mnemonic(byte)
```
---
### Bytes To Wif
convert bytes To wif Compress and uncompress:
```python
from cryptofuzz import getBytes, Bytes_To_Wif

byte = getBytes()
# compress wif
wif_compress = Bytes_To_Wif(byte, compress=True)
#uncompress Wif
wif_uncompress = Bytes_To_Wif(byte, compress=False)
```
---
### Bytes To Public Key

convert bytes to public key compress and uncompress
```python
from cryptofuzz import getBytes, Bytes_To_PublicKey

byte = getBytes()
# compress Publickey
Pub_compress = Bytes_To_PublicKey(byte, compress=True)
#uncompress Wif
Pub_uncompress = Bytes_To_PublicKey(byte, compress=False)
```
---
### Bytes to Dec (number)

convert bytes to decimal number

```python
from cryptofuzz import getBytes, Bytes_To_Decimal

byte = getBytes()
#convert to integer 
dec = Bytes_To_Decimal(byte)
```
---
### Wif To Public Key
convert wif to public key compress and uncompress
```python
from cryptofuzz import Wif_To_PublicKey

wif = "WIF_STRING_HERE"
pub_compress = Wif_To_PublicKey(wif, compress=True)
pub_uncompress = Wif_To_PublicKey(wif, compress=False)
```
---
### Wif To Mnemonic 
convert Wif To Mnemonic With Default `size=12`
```python
from cryptofuzz import Wif_To_Mnemonic

wif = "WIF_STRING_HERE"
mnemonic_string = Wif_To_Mnemonic(wif)
```
### Wif To Private Key:
convert wif to private key (hex)
```python
from cryptofuzz import Convertor

convertor = Convertor()
wif_string = "WIF_KEY_COMPRESS_OR_UNCOMPRESS"
privatekey = convertor.wif_to_hex(wif_string)
```

### Wif To XPRV
convert wif key to xprv (root key):
```python
from cryptofuzz import Convertor

convertor = Convertor()
wif_string = "WIF_KEY_COMPRESS_OR_UNCOMPRESS"
# root key (xprv)
xprv = convertor.wif_to_xprv(wif_string)
```

### Wif To Decimal (integer/number)
convert wif key to decimal number :
```python
from cryptofuzz import Convertor

convertor = Convertor()
wif_string = "WIF_KEY_COMPRESS_OR_UNCOMPRESS"
# dec
dec = convertor.wif_to_int(wif_string)
```

### Wif To XPUB

convert wif key to xpub (root public key):

```python
from cryptofuzz import Convertor

convertor = Convertor()
wif_string = "WIF_KEY_COMPRESS_OR_UNCOMPRESS"
#xpublic key
xpub = convertor.wif_to_xpub(wif_string)
```

### Wif To Address

convert wif key to compressed and uncompressed address

```python
from cryptofuzz import Convertor

convertor = Convertor()
wif_string = "WIF_KEY_COMPRESS_OR_UNCOMPRESS"
# compress
compress_address = convertor.wif_to_addr(wif_string, True)
# uncompress
uncompress_address = convertor.wif_to_addr(wif_string, False)
```

### Wif To Mnemonic

convert wif key to mnemonic 

```python
from cryptofuzz import Convertor

convertor = Convertor()
wif_string = "WIF_KEY_COMPRESS_OR_UNCOMPRESS"
# mnemonic 
mnemonic_str = convertor.wif_to_mne(wif_string)
```

---
### Passphrase To Compress And Uncompress Address
```python
from cryptofuzz.Wallet import *

passphrase = "Mmdrza.com"
compress_address = Passphrase_To_Address(passphrase, True)
uncompress_address = Passphrase_To_Address(passphrase, False)

```
### Generated XPRV and XPUB :

```python
from cryptofuzz.Wallet import *

seed = getBytes()

xprv = Bytes_To_XPRV(seed)

xpub = Bytes_To_XPUB(seed)

```

More example follow : [Example](https://github.com/Pymmdrza/cryptoFuzz/tree/main/Example)

---

### contact


Programmer & Owner : Mr. [PyMmdrza](https://github.com/Pymmdrza)



Email : PyMmdrza@Gmail.Com

Github: [cryptofuzz/cryptofuzz](https://github.com/Pymmdrza/cryptoFuzz)

Document: [cryptofuzz](https://pymmdrza.github.io/cryptoFuzz)

---
### Donate:

Bitcoin (BTC): `1MMDRZA12xdBLD1P5AfEfvEMErp588vmF9`

Ethereum & USDT (ERC20): `0x348e3C3b17784AafD7dB67d011b85F838F16E2D1`

USDT & TRON (TRC20): `TR4mA5quGVHGYS186HKDuArbD8SVssiZVx`

Litecoin (LTC): `ltc1qtgvxc6na9pxvznu05yys3j5rq9ej6kahe2j50v`
