from fastapi import APIRouter, Request, Form
from config.db import conn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_note(request: Request):
    notes = conn.notes.notes.find({})
    notesList = []
    for note in notes:
        notesList.append({
            "title": note["title"],
            "desc": note["desc"]
        })
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "notes": notesList}
    )


@note.post("/")
async def add_note(request: Request):
    form = await request.form()
    form_dict = dict(form)
    form_dict["important"] = True if form_dict.get("important") == "on" else False
    conn.notes.notes.insert_one(form_dict)
    return {"msg": "Note added successfully", "success": True, "status": 200}
