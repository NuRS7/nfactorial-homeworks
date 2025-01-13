from fastapi import FastAPI, Request


app = FastAPI()

# 1. server-ping-pong
#
# Задание:
# Измените WSGI приложение так, чтобы на запрос GET /ping отвечал pong.
# На все остальные запросы отвечать Not Found
@app.get("/ping")
async def root():
    return {"message": "pong"}
#Можно реализовать через WSGI таким оброзом )) с conditional expression if else
@app.get("/pping")
async def root(environ, start_response):
    path = environ['PATH_INFO']
    if path == '/ping':
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b'pong']
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']

# 3. fastapi-hello
#
# Задание:
# Создать хендлер на GET /, который возвращает {"message": "Hello, nfactorial!"}
@app.get("/")
async def root():
    return {"message": "Hello nFactorial!"}

# 2. server-request-info
#
# Задание:
# Измените WSGI приложение так, чтобы на запрос GET /info возвращал информацию о запросе:
# HTTP-метод
# URL запроса
# Протокол запроса
@app.get("/info")
async def info(Request: Request):
    return {
        'method': Request.method,
        'url': Request.url,
        'protocol': Request.scope['http_version'],
    }

# 4. fastapi-meaning-life
#
# Задание:
# Создать хендлер на POST /meaning-of-life, который возвращает {"meaning": "42"}


@app.post("/meaning-of-life")
async def meaning_of_life():
    return {"meaning": "42"}

# 5. fastapi-nfactorial 💎
#
# Задание:
# Создать хендлер на GET /{num}, который возвращает факториал числа “num”.

def calculate_factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
@app.get("/{num}")
async def nfactorial(num: int):
    result = calculate_factorial(num)
    return {"num:": num, "factorial": result}


