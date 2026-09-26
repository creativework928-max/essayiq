from __future__ import annotations
import re
def word_count(text): return len(re.findall(r"\b[\w'’-]+\b",text))
def sentence_count(text): return len([x for x in re.split(r"(?<=[.!?])\s+",text.strip()) if x.strip()])
def paragraph_count(text): return len([x for x in re.split(r"\n\s*\n",text) if x.strip()])
