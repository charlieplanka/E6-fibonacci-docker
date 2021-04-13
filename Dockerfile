FROM python:3.8
# ENV PORT 8081
ENV FLASK_DEBUG 1
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./app/app.py /app/app.py
ENTRYPOINT ["flask"]
CMD ["run"]