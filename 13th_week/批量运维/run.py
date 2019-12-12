python3 <<EOF
import psutil as pu
mem = pu.virtual_memory()
print(mem.percent)
EOF
