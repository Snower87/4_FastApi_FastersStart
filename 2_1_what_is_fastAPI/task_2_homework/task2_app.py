from fastapi import FastAPI
from fastapi.responses import FileResponse

task2_app = FastAPI()

# Вариант №1 - выдаем файл через объект FileResponse
# @task2_app.get("/")
# def read_root():
#     return FileResponse("public/task2.html")

# Вариант №2 - прописываем, что в ответе будет объект класса FileResponse
# и возвращаем путь к файлу
# в данном варианте url-запроса: "http://127.0.0.1:8000/file"
@task2_app.get("/file", response_class=FileResponse)
def root_html():
    return "public/task2.html"