FROM python
COPY . /app
WORKDIR /app
RUN apt-get -y install python-rpi.gpio
CMD ["python", "trafficLight.py"]