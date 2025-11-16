from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    rating: float
    description: str
    url: str
    sentiment_score: float = 0.0
    spec_score: float = 0.0
    price_score: float = 0.0

@dataclass
class RankedProduct:
    name: str
    price: float
    rating: float
    description: str
    url: str
    score: float
    breakdown: dict = field(default_factory=dict)
