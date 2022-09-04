import json

def load_candidates():
    """Загрузка файла жсон"""
    with open("candidates.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidates_all():
    """Получение всех кандидатов"""
    return load_candidates()


def get_candidates_by_pk(pk):
    """Получение кандидата по pk"""
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate
    return 'Not Found'


def get_candidates_by_skill(skill):
    """Получение кандидата по skill"""
    result = []
    candidates = load_candidates()
    for candidate in candidates:
        if skill in candidate['skills'].lower():
            result.append(candidate)
    return result


