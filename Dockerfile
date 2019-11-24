From python:3.8.0
LABEL maintainer="huiliuyi@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
