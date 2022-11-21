"""
Слишком кринжово получилось...
Простите...
"""
from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def view_all():
    """
    Выводит пользователю всех кандидатов
    """
    candidates = get_all()
    text = ""
    for item in candidates:
        text += view_candidate(item)
    return f"<pre>\n{text}\n</pre>"


@app.route("/candidates/<int:pk>")
def view_by_pk(pk):
    """
    Выводит одного кандидата по порядковому номеру с аватаркой
    """
    candidate = get_by_pk(pk)
    text = view_candidate(candidate)
    img = candidate.get("picture")
    return f"<img src={img}>\n\n<pre>{text}</pre>"


@app.route("/skills/<skill>")
def view_by_skill(skill):
    """
    Выводит список кандидатов с нужным навыком
    """
    candidates = get_by_skill(skill)
    text = ""
    for item in candidates:
        text += view_candidate(item)
    return f"<pre>\n{text}\n</pre>"


if __name__ == "__main__":
    app.run()
