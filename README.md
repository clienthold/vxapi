# vxapi

[virus.exchange](https://virus.exchange/) wrapper for python

# Usage

```
import vxapi

vx = vxapi.vxapi("ENTER YOUR API KEY")
sample = vx.get_sample("9f7b4bd7f9b3dff55e97516a19905cc6af88bae1817f1ad6e5e3e2ca7737f3dc")

print(sample.size)
> 131072
print(sample.first_seen)
> 2024-03-25 07:20:13+00:00
print(sample.download_link)
> https://s3[.]us-east-1[.]wasabisys[.]com/vxugmwdb/ ...
