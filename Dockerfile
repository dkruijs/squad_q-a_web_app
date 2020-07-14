FROM python:3.7-slim-stretch
WORKDIR /app

# Copy and install source code and python packages:
COPY ./src /app
COPY requirements.txt /app
COPY setup.py /app
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Start both the Flask API and the nginx web server:
# CMD ["python", "-m", "app.api"]
#CMD ["nginx", "-g", "daemon off;", "python", "-m", "app.api"]

#ENTRYPOINT ["/bin/bash"]
CMD ["./app/start_server.sh"]