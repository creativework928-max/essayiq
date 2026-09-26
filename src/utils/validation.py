from src.config import settings
def validate_essay(text:str):
    if not isinstance(text,str) or not text.strip(): raise ValueError("Essay must contain text.")
    if len(text)<settings.min_essay_chars: raise ValueError(f"Essay must contain at least {settings.min_essay_chars} characters.")
    if len(text)>settings.max_essay_chars: raise ValueError(f"Essay exceeds the {settings.max_essay_chars} character limit.")
