#!/usr/bin/env python

import sys

from collections import Counter
from itertools import izip

print ''.join(Counter(item).most_common()[-1][0]
              for item in izip(*[line.strip() for line in sys.stdin])
              )
