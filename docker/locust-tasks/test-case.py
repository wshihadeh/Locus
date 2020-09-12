
from locust import HttpLocust, TaskSet, task, between
import random
import string

class WebsiteTasks(TaskSet):
    @task
    def index(self):
        self.client.get("/")
    @task
    def update(self):
        self.client.get("/guestbook.php?cmd=set&key=messages&value=,JohnDietish,")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)
