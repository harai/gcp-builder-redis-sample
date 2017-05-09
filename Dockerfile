FROM redissample_redissample_test:latest

COPY ["build/redis_sample-0.0.0-py3-none-any.whl", "/"]
RUN pip install -I /redis_sample-0.0.0-py3-none-any.whl && rm /redis_sample-0.0.0-py3-none-any.whl

ENV FLASK_APP=redissample.app

CMD ["flask", "run", "-h", "0.0.0.0"]
