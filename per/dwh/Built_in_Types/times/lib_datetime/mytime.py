# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:DW 
# date:2019/3/12
from datetime import datetime

# ====================data=========================
a = datetime.now()

print(type(a))
print(a.isoformat("/", "hours"))
