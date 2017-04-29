FROM python:3.6.1

COPY ["requirements.txt", "/"]
RUN pip install -r /requirements.txt && rm /requirements.txt

WORKDIR /redissample
ENV PYTHONPATH=/redissample
CMD ["python", "test/test_app.py"]
