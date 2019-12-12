python3 <<EOF
import psutil as pu
import json
info = {}
info['cpu_count'] = pu.cpu_count()
info['cpu_percent'] = pu.cpu_percent(interval=1)
#info['cpu_percent'] = pu.cpu_percent(percpu=True, interval=1)
mem = pu.virtual_memory()
info['mem_total'] = mem.total
#info['mem_available'] = mem.available
info['mem_percent'] = mem.percent
#info['mem_used'] = mem.used
#info['mem_free'] = mem.free
disk = pu.disk_usage('/')
info['disk_total'] = disk.total
#info['disk_used'] = disk.used
#info['disk_free'] = disk.free
info['disk_percent'] = disk.percent
data = json.dumps(info)
print(data)
EOF