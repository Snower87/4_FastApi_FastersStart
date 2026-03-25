import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Авторелоад222 действительно работает"}

# 1. Надо поменять директорию запуска приложения:
# cd C:\pythonAQA\cources\4_FastApi_FastersStart\2_1_what_is_fastAPI
# 2. При запуска надо не main:app писать, а app:app:
# не забываем при запуске uvicorn app:app --reload менять переменную приложения (название), а то будете долго думать что не так ))

"""
if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=80)
"""