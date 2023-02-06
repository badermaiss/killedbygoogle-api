FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache -r requirements.txt

COPY ./api.py /code/app/api.py

CMD ["python", "app/api.py", "--host", "0.0.0.0"]