FROM mysql
ADD ./db/products-sql-dump.sql /docker-entrypoint-initdb.d

# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# Run the web service
CMD ["python", "/app/src/app.py"]
