FROM locustio/locust:1.2.3

ADD locust-tasks /locust-tasks
ADD run.sh .

# Install the required dependencies via pip
RUN pip install -r /locust-tasks/requirements.txt

# Set script to be executable
User root
RUN chmod 755 run.sh
User locust

# Start Locust using LOCUS_OPTS environment variable
ENTRYPOINT ["bash", "./run.sh"]