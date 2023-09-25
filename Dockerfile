FROM python:3.10
RUN mkdir /app
COPY . /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt -i https://pypi.douban.com/simple
WORKDIR /app
RUN chmod 777 /app/allure/bin/allure

CMD ["python", "main.py"]
