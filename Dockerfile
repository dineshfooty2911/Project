# Use the official Airflow image as the base image
FROM apache/airflow:2.5.1

# Switch to the airflow user to install additional packages
USER airflow

# Install the minio library
RUN pip install minio
