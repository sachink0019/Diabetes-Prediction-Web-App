# base image
FROM python:3.11

# workdir
WORKDIR /2_app

#copy
COPY . /2_app

#requirements
RUN pip install --no-cache-dir -r requirements1.txt

#port
EXPOSE 8000

#command
CMD ["uvicorn", "2_app:app", "--host", "0.0.0.0", "--port", "8000"]
