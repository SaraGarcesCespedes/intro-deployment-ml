from pydantic import BaseModel

class PredictionRequest(BaseModel):
    opening_gross: float
    screens: float
    production_budget: float
    title_year: float
    aspect_ratio: float
    duration: int
    budget: float
    cast_total_facebook_likes: float
    imdb_score: float


class PredictionResponse(BaseModel):
    worldwide_gross: float
