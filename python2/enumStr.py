from enum import Enum
class VIP(Enum):
    YELLO=1
    YELLO_ALE=1
    RED=2
    BLANK=3
for i in VIP:
    print(i)
for item in VIP.__members__:
    print(item)    
for v in VIP.__members__.items():
    print(v)        