import os, sys

if os.geteuid() != 0:
    print("This program must be run as root. Aborting.")
    sys.exit(1)
