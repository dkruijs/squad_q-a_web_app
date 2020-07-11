FROM python:3.7-slim-stretch
RUN apt-get update && apt-get install nginx -y

WORKDIR /app

# Overwrite nginx config file
COPY ./src/app/website/nginx.conf /etc/nginx/nginx.conf

# Copy and install source code and python packages
COPY ./src /app
COPY requirements.txt /app
COPY setup.py /app
#RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080, 80 and 90
EXPOSE 8080 80

CMD ["python", "./app/api.py"]
CMD ["nginx", "-g", "daemon off;"]


#ENTRYPOINT ["/bin/bash"]
#CMD ["./app/start_server.sh &"]