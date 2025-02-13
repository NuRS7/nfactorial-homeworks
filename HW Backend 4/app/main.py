from fastapi import FastAPI, Form, Request, Query
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from .repository import BooksRepository
app = FastAPI()
import os
repository = BooksRepository()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
templates = Jinja2Templates(directory="templates")

ITEMS_PER_PAGE = 10

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/books")
def get_books(request: Request, page: int = Query(1, alias="page", ge=1)):
    try:
        page = int(page)
        if page < 1:
            return {"error": "Invalid page number"}
    except ValueError:
        return {"error": "Invalid page number"}

    books = repository.get_all()
    total_books = len(books)
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    books_on_page = books[start:end]
    has_next = end < total_books
    has_prev = start > 0
    return {"books": books_on_page, "has_next": has_next, "has_prev": has_prev}

@app.get("/books/new")
def new_book_form(request: Request):
    return templates.TemplateResponse("books/new.html", {"request": request})

@app.post("/books")
def create_book(
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
    total_pages: int = Form(...),
    genre: str = Form(...),
):
    try:
        repository.create({
            "title": title,
            "author": author,
            "year": year,
            "total_pages": total_pages,
            "genre": genre,
        })
        return RedirectResponse(url="/books", status_code=303)
    except Exception as e:
        return {"error": str(e)}
    #