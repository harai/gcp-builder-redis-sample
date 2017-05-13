FROM python:3.6.1

COPY ["requirements.txt", "build/redis_sample-0.0.0-py3-none-any.whl", "/"]

# RUN pip install -r /requirements.txt && rm /requirements.txt
# RUN pip install -I /redis_sample-0.0.0-py3-none-any.whl && rm /redis_sample-0.0.0-py3-none-any.whl
RUN pip install -r /requirements.txt
RUN pip install -I /redis_sample-0.0.0-py3-none-any.whl

ENV PYTHONPATH=/redissample
ENV FLASK_APP=redissample.app

WORKDIR /redissample

CMD ["flask", "run", "-h", "0.0.0.0"]
