from datetime import time

# Market timings
MARKET_OPEN = time(9, 15)
MARKET_CLOSE = time(15, 30)

# DIDRS configuration
EXPIRY_SCAN_START = time(14, 0)

# Strike Selection
DEFAULT_LEVELS = 2        # 23500 CE when spot is 24081

# Discount
DEFAULT_DISCOUNT_THRESHOLD = 5.0