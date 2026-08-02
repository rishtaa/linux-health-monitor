import datetime
import platform

import psutil


def generate_report():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    memory_percent = memory.percent
    memory_used = round(memory.used / (1024**3), 2)
    memory_total = round(memory.total / (1024**3), 2)

    disk_percent = disk.percent
    disk_used = round(disk.used / (1024**3), 2)
    disk_total = round(disk.total / (1024**3), 2)
    disk_free = round(disk.free / (1024**3), 2)

    hostname = platform.node()
    os_name = platform.system()
    os_version = platform.release()

    if cpu > 80:
        print("Warning: High CPU Usage!")
    if memory_percent > 80:
        print("Warning: High Memory Usage!")
    if disk_percent > 80:
        print("Warning: High Disk Usage!")

    time = datetime.datetime.now()

    report = f"""
System Health Report
-----------------------------
Hostname: {hostname}
Operating System: {os_name}
OS Version: {os_version}

Time: {time}
CPU Usage: {cpu}%

Memory Usage: {memory_percent}%
Memory Used : {memory_used} GB
Memory Total: {memory_total} GB

Disk Usage: {disk_percent}%
Disk Used: {disk_used} GB
Disk Free: {disk_free} GB
Disk Total: {disk_total} GB
-----------------------------
"""

    print(report)

    with open("health.log", "a") as file:
        file.write(report)


if __name__ == "__main__":
    generate_report()
