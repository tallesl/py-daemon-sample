FROM python:3
COPY random-wiki.py random-wiki.py
ENV PYTHONUNBUFFERED=1
CMD [ "python", "./random-wiki.py" ]
