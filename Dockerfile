FROM python:latest

ENV $WORKING_DIR /usr/app
COPY . $WORKING_DIR

RUN pip3 install -r requirements

WORKDIR $WORKING_DIR

CMD ["python", "manage.py"]
