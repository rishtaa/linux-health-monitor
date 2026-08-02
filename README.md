# Linux Health Monitor

![Python CI/CD](https://github.com/rishtaa/linux-health-monitor/actions/workflows/python.yml/badge.svg)

## Features

- Monitor CPU Usage
- Monitor Memory Usage
- Monitor Disk Usage
- Display Hostname and Operating System Information
- Generate System Health Reports
- Save Reports to a Log File
- Automated Monitoring using Cron Jobs
- Dockerized Application
- Automated Code Quality Checks using flake8
- Unit Testing using pytest
- CI/CD Pipeline with GitHub Actions
- Automatic Docker Image Publishing to Docker Hub

## Technologies Used

- Python
- Linux (WSL)
- Docker
- Git
- GitHub
- GitHub Actions
- pytest
- flake8
- Docker Hub

## Project Structure

```
linux-health-monitor/
│
├── .github/
│   └── workflows/
│       └── python.yml
│
├── images/
│
├── tests/
│   └── test_health_monitor.py
│
├── health_monitor.py
├── requirements.txt
├── Dockerfile
├── README.md
└── LICENSE
```

## CI/CD Workflow

Every push to the `main` branch automatically triggers GitHub Actions.

Pipeline:

```
Push Code
      │
      v
Checkout Repository
      │
      v
Install Dependencies
      │
      v
Run flake8
      │
      v
Run pytest
      │
      v
Build Docker Image
      │
      v
Push Docker Image to Docker Hub
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

## Future Enhancements

- Email alerts for high resource usage
- Slack notifications
- Grafana dashboard integration
- Prometheus metrics
- Kubernetes deployment

## Author

**Rishtaa Jaishree**
