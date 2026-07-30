# Linux System Health Monitor

A Python-based Linux system monitoring application that checks CPU, Memory, and Disk usage. The application generates a health report, logs the output to a file, and can be automated using Cron or run inside Docker.

## Features

- Monitor CPU Usage
- Monitor Memory Usage
- Monitor Disk Usage
- Display Hostname and Operating System
- Generate Health Reports
- Save Reports to Log File
- Automatic Monitoring using Cron
- Docker Support

## Technologies Used

- Python 3
- Linux (Ubuntu WSL)
- psutil
- Docker
- Git
- GitHub

## Project Structure

```
linux-health-monitor/
├── health_monitor.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .dockerignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/rishtaa/linux-health-monitor.git
```

Move into the project directory:

```bash
cd linux-health-monitor
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python health_monitor.py
```

## Docker

Build the Docker image:

```bash
docker build -t linux-health-monitor .
```

Run the Docker container:

```bash
docker run --rm linux-health-monitor
```

## Cron Automation

Example Cron job to execute the script every minute:

```cron
* * * * * /home/rishtaa/linux-health-monitor/venv/bin/python /home/rishtaa/linux-health-monitor/health_monitor.py
```

## Sample Output

```
System Health Report
-----------------------------
Hostname: LAPTOP-KOTLD872
Operating System: Linux

CPU Usage: 0.0%

Memory Usage: 23.9%
Memory Used : 0.40 GB
Memory Total: 1.69 GB

Disk Usage: 0.2%
Disk Used: 1.91 GB
Disk Free: 953.73 GB
Disk Total: 1006.85 GB
-----------------------------
```

## Future Improvements

- Email alerts
- Network monitoring
- CPU temperature monitoring
- Web dashboard using Flask
- Kubernetes deployment
- GitHub Actions CI/CD

## Author

**Rishtaa Jaishree**
