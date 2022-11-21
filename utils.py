import json

CANDIDATES_JSON = "candidates.json"


def load_candidates():
    """
    Загружает из json файла список со всеми кандидатами
    """
    with open(CANDIDATES_JSON, "r") as json_file:
        candidates = json.load(json_file)
        return candidates


def get_all():
    """
    Возвращает всех кандидатов из списка
    """
    return load_candidates()


def get_by_pk(pk):
    """
    Возвращает одного кандидата по номеру в виде словаря
    """
    candidates = load_candidates()
    for item in candidates:
        if item.get("pk") == pk:
            return item


def get_by_skill(skill_name):
    """
    Возвращает всех кандидатов, имеющих нужный навык в виде списка словаря
    """
    candidates = load_candidates()
    candidates_with_skills = []
    for item in candidates:
        if skill_name.lower() in item.get("skills").lower():
            candidates_with_skills.append(item)
    return candidates_with_skills


def view_candidate(candidate):
    """
    Собирает из словаря с данными кандидатами строку для отображения со всеми нужными переносами
    """
    text = ""
    text += candidate.get("name")
    text += " -\n"
    text += candidate.get("position")
    text += "\n"
    text += candidate.get("skills")
    text += "\n\n"
    return text
