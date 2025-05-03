FROM python:3.10

WORKDIR /app
COPY . /app

COPY requirements.txt .
RUN python -m venv env && env/Scripts/pip.exe install -r requirements.txt

# RUN python -m venv /app/venv && /app/venv/bin/pip install -r requirements.txt

# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "src.app:create_app()"]