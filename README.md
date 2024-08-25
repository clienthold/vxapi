# 💽 VXAPI

**[virus.exchange](https://virus.exchange/)** wrapper for python

# Installation

```
pip install vxapi
```

> [!NOTE]
> Get your API key **[here](https://virus.exchange/users/settings)**

# Usage

```
import vxapi

vx = vxapi.vxapi("ENTER YOUR API KEY")
sample = vx.get_sample("9f7b4bd7f9b3dff55e97516a19905cc6af88bae1817f1ad6e5e3e2ca7737f3dc")

print(sample.md5)
> ffdceadfc3973b02f15c0106122c7490
print(sample.sha256)
> 9f7b4bd7f9b3dff55e97516a19905cc6af88bae1817f1ad6e5e3e2ca7737f3dc
print(sample.sha512)
> a33fce3dcb3eb95a638b290757b3a613ca6a125ea324512de40658c62f7a0611775d5d802a6c4d45850c9a25974c2d5f279fd2f6b4ed75d11dc74e8c6f77111a
print(sample.type)
> None
print(sample.size)
> 131072
print(sample.first_seen)
> 2024-03-25 07:20:13+00:00
print(sample.download_link)
> https://s3[.]us-east-1[.]wasabisys[.]com/vxugmwdb/ ...