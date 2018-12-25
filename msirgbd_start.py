#!/usr/bin/env python3

import os
from msirgbd import main

if __name__ == "__main__":
    os.putenv("LOG_CFG", "logging.json")
    main()
