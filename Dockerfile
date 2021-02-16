FROM  python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /library
COPY requirements.txt ./
RUN pip install -r requirements.txt