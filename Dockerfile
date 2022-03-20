FROM m.docker-registry.ir/python
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python3","main.py"]

