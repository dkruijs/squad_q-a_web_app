FROM python:3.7-slim-stretch

WORKDIR /app
# Copy and install source code and python packages:
COPY ./src /app
COPY requirements.txt /app
COPY setup.py /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "app.api"]
#ENTRYPOINT [ "flask" ]
#CMD ["run", "--host=0.0.0.0", "--port=5000"]
