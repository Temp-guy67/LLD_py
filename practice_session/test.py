import time

# Usage
current_timestamp = time.time()
print(current_timestamp)

import datetime

# Usage
now = datetime.datetime.now()
time.sleep(10)
now2 = datetime.datetime.now()
x = now2-now

print(x.total_seconds())
