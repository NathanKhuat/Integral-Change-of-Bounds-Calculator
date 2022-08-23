# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /ChangeOfBoundsCalculator/requirements.txt

# switch working directory
WORKDIR /ChangeOfBoundsCalculator

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /ChangeOfBoundsCalculator
ENV FLASK_APP=app.py
# configure the container to run in an executed manner
CMD ["python", "./app.py"]