HELP_KEYWORDS = [
    "עזרה",
    "תעזרו לי",
    "אני צריך אמבולנס",
    "נפלתי",
    "תקראו לאמבולנס",
    "help",
    "ambulance",
]


def detect_help_intent(text):
    text = text.lower()

    for kw in HELP_KEYWORDS:
        if kw in text:
            return 1.0

    return 0.0
