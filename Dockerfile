FROM python

WORKDIR /newApp

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["py","manage.py","runserver","192.168.0.101:3000/"]