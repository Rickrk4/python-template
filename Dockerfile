FROM python
COPY . /usr/bin/app
WORKDIR /usr/bin/app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]