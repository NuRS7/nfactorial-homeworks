from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Хранение комментариев в памяти
comments = []

# Настройка шаблонов и статических файлов
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/templates"), name="static")


@app.get("/")
def read_comments(request: Request, page: int = 1, per_page: int = 5):
    # Параметры для пагинации
    start = (page - 1) * per_page
    end = start + per_page
    paginated_comments = comments[start:end]
    total_pages = (len(comments) + per_page - 1) // per_page

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "comments": paginated_comments,
            "page": page,
            "total_pages": total_pages,
        },
    )


@app.post("/add")
def add_comment(
    text: str = Form(...), category: str = Form(...)
):
    if category not in ["positive", "negative"]:
        category = "positive"  # Значение по умолчанию

    # Добавление нового комментария в память
    comments.insert(0, {"text": text, "category": category})

    # Перенаправление на главную страницу
    return RedirectResponse(url="/", status_code=303)
