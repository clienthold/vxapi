# 💽 VXAPI

[![PyPI version](https://img.shields.io/pypi/v/vxapi.svg)](https://pypi.org/project/vxapi/)
[![Downloads](https://img.shields.io/pypi/dm/vxapi.svg)](https://pypi.org/project/vxapi/)

**Python wrapper for the [Virus.Exchange](https://virus.exchange/) API** to fetch malware sample metadata and download malicious files for analysis.

## 📋 Table of Contents

* [🔍 Features](#-features)
* [💾 Installation](#-installation)
* [🚀 Quick Start](#-quick-start)
* [🛠️ Usage](#️-usage)

## 🔍 Features

* Retrieve sample metadata (MD5, SHA256, SHA512, type, size, first seen)
* Generate direct download links for malware samples
* Lightweight and easy-to-use Python interface
* Built-in error handling and status checks

## 💾 Installation

Install from PyPI:

```bash
pip install vxapi
```

Obtain your API key on the [Virus.Exchange settings page](https://virus.exchange/users/settings).

## 🚀 Quick Start

```python
from vxapi import VXAPI

# Initialize client
client = VXAPI('YOUR_API_KEY')

# Fetch a sample by SHA256
sample = client.get_sample('9f7b4bd7f9b3dff55e97516a19905cc6af88bae1817f1ad6e5e3e2ca7737f3dc')

print(f"MD5:           {sample.md5}")
print(f"SHA256:        {sample.sha256}")
print(f"SHA512:        {sample.sha512}")
print(f"Type:          {sample.type or 'Unknown'}")
print(f"Size:          {sample.size} bytes")
print(f"First seen:    {sample.first_seen}")
print(f"Download link: {sample.download_link}")
```

## 🛠️ Usage

### Initialization

```python
from vxapi import VXAPI
client = VXAPI('<YOUR_API_KEY>')
```

### Methods

* `get_sample(identifier: str) -> Sample`

  * **identifier**: SHA256, SHA1, or MD5 hash of the sample.
  * **returns**: a `Sample` object with properties:

    * `md5`, `sha1`, `sha256`, `sha512`
    * `type`: file type if detected
    * `size`: file size in bytes
    * `first_seen`: timestamp of first sighting
    * `download_link`: URL to download the sample

### Example

```python
# Query a list of hashes
hashes = ['abc123...', 'def456...']
for h in hashes:
    try:
        s = client.get_sample(h)
        print(f"{h}: {s.size} bytes, seen {s.first_seen}")
    except Exception as e:
        print(f"Error fetching {h}: {e}")
```
