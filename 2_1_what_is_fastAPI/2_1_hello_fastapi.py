# Если fastapi не скачивается обычно, то скачать с зеркала
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ fastapi[all]
#pip install -i https://mirrors.aliyun.com/pypi/simple/ fastapi[all]
#Для Установки FastAPI лучше использовать команду pip install fastapi[all]
#Она установит все нужные пакеты сразу. В том числе и Unicorn.
import uvicorn
# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=80)