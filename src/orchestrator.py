import re
from src.weather_agent import get_weather_info
from src.places_agent import get_places_info


def extract_location_fallback(text: str) -> str | None:
    text_norm = text.replace("'", "'")
    text_clean = text_norm.strip()

    patterns = [
        r"\b(?:visit|go|travel|trip)\s+(?:some\s+)?(?:places\s+)?(?:in|at|to|near)\s+([A-Z][A-Za-z\s]+?)(?:[,.!?]|$)",
        r"\b(?:in|at|to|near)\s+([A-Z][A-Za-z\s]+?)(?:[,.!?]|$)",
        r"\b(?:visit|go|travel)\s+(?:to\s+)?([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)?)(?:[,.!?]|$)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text_clean, flags=re.IGNORECASE)
        if match:
            candidate = match.group(1).strip()
            
            filler_words = ["some", "places", "any", "the", "many", "few", "several"]
            words = candidate.split()
            words = [w for w in words if w.lower() not in filler_words]
            
            candidate = " ".join(words).strip()
            
            if candidate and len(candidate) > 2:
                return candidate.lower()

    capitals = re.findall(r"[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*", text_norm)
    NON_LOCATIONS = {"ok", "yes", "no", "hi", "hey", "hello", "thanks", "i"}
    
    for cap in reversed(capitals):
        if cap.lower() not in NON_LOCATIONS:
            return cap.lower()

    return None


def extract_location(text: str) -> str | None:
    return extract_location_fallback(text)


def detect_intent(query: str):
    q = query.lower()

    weather_keywords = [
        "weather", "temperature", "climate", "rain", "snow",
        "sunny", "forecast", "humidity", "wind"
    ]

    places_keywords = [
        "places", "attractions", "visit", "tourist", "things to do",
        "plan my trip", "plan my visit", "sightseeing", "travel guide",
        "where to go"
    ]

    wants_weather = any(k in q for k in weather_keywords)
    wants_places = any(k in q for k in places_keywords)

    if not (wants_weather or wants_places):
        wants_places = True

    return wants_weather, wants_places


def handle_user_query(query: str) -> str:
    location = extract_location(query)

    if not location:
        return "I'm not sure which location you are referring to. Please provide the city name."

    wants_weather, wants_places = detect_intent(query)

    responses = []

    if wants_weather:
        responses.append(get_weather_info(location))

    if wants_places:
        responses.append(get_places_info(location))

    if not responses:
        return "Please ask about the weather or places to visit for a specific location."

    return "\n\n".join(responses)
