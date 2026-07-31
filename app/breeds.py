"""Indian cattle and buffalo breed reference data."""

from __future__ import annotations


BREEDS = {
    "Gir": {
        "type": "Cattle",
        "region": "Gujarat",
        "milk_yield": "1,200–1,800 L / lactation",
        "lifespan": "12–15 years",
        "usage": "Dairy, drought resistance",
        "description": "Distinctive curved horns and a prominent forehead. One of India's finest dairy breeds, well adapted to tropical climates.",
        "color_hints": ["red", "brown", "white_patches"],
        "visual": "Indian Gir cow, reddish-brown coat with white patches, prominent convex forehead, long curved lyre-shaped horns",
    },
    "Sahiwal": {
        "type": "Cattle",
        "region": "Punjab, Haryana, Rajasthan",
        "milk_yield": "1,500–2,500 L / lactation",
        "lifespan": "12–18 years",
        "usage": "High milk yield dairy",
        "description": "Reddish-brown dual-purpose breed known for heat tolerance and high butterfat milk.",
        "color_hints": ["red", "brown"],
        "visual": "Indian Sahiwal cow, solid reddish-brown or dun coat, loose skin, short horns, dairy zebu cattle",
    },
    "Red Sindhi": {
        "type": "Cattle",
        "region": "Sindh origin; kept across India",
        "milk_yield": "1,200–2,000 L / lactation",
        "lifespan": "12–15 years",
        "usage": "Dairy",
        "description": "Deep red coat, compact body. Excellent milk producer suited to hot, humid regions.",
        "color_hints": ["red", "deep_red"],
        "visual": "Indian Red Sindhi cow, deep red or dark red solid coat, compact body, small horns",
    },
    "Tharparkar": {
        "type": "Cattle",
        "region": "Rajasthan, Gujarat",
        "milk_yield": "1,800–2,600 L / lactation",
        "lifespan": "12–16 years",
        "usage": "Dairy and drought work",
        "description": "White to light grey desert breed, hardy and productive even in arid zones.",
        "color_hints": ["white", "light_grey"],
        "visual": "Indian Tharparkar cow, white or light grey desert cattle, medium horns, arid Rajasthan breed",
    },
    "Hariana": {
        "type": "Cattle",
        "region": "Haryana, Western UP, Rajasthan",
        "milk_yield": "1,000–1,500 L / lactation",
        "lifespan": "12–15 years",
        "usage": "Dual-purpose (milk & draught)",
        "description": "White or light grey cattle traditionally used for both milk and farm work.",
        "color_hints": ["white", "light_grey"],
        "visual": "Indian Hariana cow, white or light grey coat, long face, draught zebu cattle from Haryana",
    },
    "Kankrej": {
        "type": "Cattle",
        "region": "Gujarat, Rajasthan",
        "milk_yield": "1,000–1,800 L / lactation",
        "lifespan": "12–16 years",
        "usage": "Dual-purpose, strong draught",
        "description": "Silver-grey to iron-grey breed with lyre-shaped horns; powerful draught animals.",
        "color_hints": ["grey", "silver"],
        "visual": "Indian Kankrej cow, silver-grey or iron-grey coat, large lyre-shaped horns, strong draught cattle",
    },
    "Ongole": {
        "type": "Cattle",
        "region": "Andhra Pradesh",
        "milk_yield": "800–1,200 L / lactation",
        "lifespan": "14–18 years",
        "usage": "Draught, beef export lineage",
        "description": "Large white cattle with muscular build; historically prized for strength.",
        "color_hints": ["white"],
        "visual": "Indian Ongole cow, large white muscular zebu, short horns, heavy body from Andhra Pradesh",
    },
    "Hallikar": {
        "type": "Cattle",
        "region": "Karnataka",
        "milk_yield": "500–800 L / lactation",
        "lifespan": "15–20 years",
        "usage": "Draught / farm work",
        "description": "Grey draught breed famous for stamina and long, pointed horns.",
        "color_hints": ["grey"],
        "visual": "Indian Hallikar cow, grey draught cattle from Karnataka, long pointed horns, lean athletic body",
    },
    "Rathi": {
        "type": "Cattle",
        "region": "Rajasthan",
        "milk_yield": "1,500–2,000 L / lactation",
        "lifespan": "12–15 years",
        "usage": "Dairy",
        "description": "Brown with white patches; good milkers adapted to desert conditions.",
        "color_hints": ["brown", "white_patches"],
        "visual": "Indian Rathi cow, brown coat with white patches, desert dairy cattle from Rajasthan",
    },
    "Deoni": {
        "type": "Cattle",
        "region": "Maharashtra, Karnataka",
        "milk_yield": "800–1,200 L / lactation",
        "lifespan": "12–16 years",
        "usage": "Dual-purpose",
        "description": "Spotted black-and-white or grey cattle of the Deccan plateau.",
        "color_hints": ["black", "white_patches", "grey"],
        "visual": "rare Indian Deoni cattle breed with clear black-and-white piebald spots like a patched dual-colour coat, Maharashtra Deccan zebu, not a solid-coloured cow",
    },
    "Murrah": {
        "type": "Buffalo",
        "region": "Haryana, Punjab, Delhi NCR",
        "milk_yield": "1,800–3,000 L / lactation",
        "lifespan": "15–20 years",
        "usage": "Premier dairy buffalo",
        "description": "Jet-black coat, tightly curled horns. India's most famous dairy buffalo breed.",
        "color_hints": ["black"],
        "visual": "Indian Murrah buffalo, jet black water buffalo, tightly curled horns, dairy buffalo",
    },
    "Jaffarabadi": {
        "type": "Buffalo",
        "region": "Gujarat (Saurashtra)",
        "milk_yield": "1,800–2,500 L / lactation",
        "lifespan": "15–18 years",
        "usage": "Dairy, high fat milk",
        "description": "Largest Indian buffalo; black with heavy drooping horns.",
        "color_hints": ["black"],
        "visual": "Indian Jaffarabadi buffalo, very large black buffalo, heavy drooping horns covering the face",
    },
    "Mehsana": {
        "type": "Buffalo",
        "region": "Gujarat (Mehsana)",
        "milk_yield": "1,800–2,700 L / lactation",
        "lifespan": "15–18 years",
        "usage": "Dairy",
        "description": "Black or brownish-black; mix of Murrah and Surti traits, strong milkers.",
        "color_hints": ["black", "dark_brown"],
        "visual": "Indian Mehsana buffalo, black or brownish-black dairy buffalo from Gujarat, sickle shaped horns",
    },
    "Surti": {
        "type": "Buffalo",
        "region": "Gujarat (Kaira, Baroda)",
        "milk_yield": "1,500–2,000 L / lactation",
        "lifespan": "14–18 years",
        "usage": "Dairy, high butterfat",
        "description": "Medium-sized, black or brown with sickle-shaped horns; rich milk.",
        "color_hints": ["black", "brown"],
        "visual": "Indian Surti buffalo, medium sized black or brown buffalo, sickle-shaped horns, Gujarat dairy buffalo",
    },
    "Nili-Ravi": {
        "type": "Buffalo",
        "region": "Punjab",
        "milk_yield": "1,800–2,500 L / lactation",
        "lifespan": "15–20 years",
        "usage": "Dairy",
        "description": "Black buffalo often with white markings on face/legs; excellent milk breed.",
        "color_hints": ["black", "white_patches"],
        "visual": "Indian Nili-Ravi buffalo, black buffalo with white markings on face forehead and legs, wall eyes",
    },
    "Bhadawari": {
        "type": "Buffalo",
        "region": "Uttar Pradesh, Madhya Pradesh",
        "milk_yield": "800–1,200 L / lactation",
        "lifespan": "14–18 years",
        "usage": "Dairy (very high fat %)",
        "description": "Copper-coloured coat; milk has exceptionally high fat content.",
        "color_hints": ["copper", "brown"],
        "visual": "Indian Bhadawari buffalo, copper coloured or light brown buffalo coat, not jet black, UP Madhya Pradesh",
    },
}


# Model label → display name
_LABEL_ALIASES = {
    "Red_Sindhi": "Red Sindhi",
    "Nili_Ravi": "Nili-Ravi",
    "Jaffrabadi": "Jaffarabadi",
    "Brown_Swiss": "Brown Swiss",
    "Holstein_Friesian": "Holstein Friesian",
    "Malnad_gidda": "Malnad Gidda",
    "Krishna_Valley": "Krishna Valley",
    "Red_Dane": "Red Dane",
}

_BUFFALO_LABELS = {
    "Banni",
    "Bhadawari",
    "Jaffrabadi",
    "Jaffarabadi",
    "Mehsana",
    "Murrah",
    "Nagpuri",
    "Nili_Ravi",
    "Nili-Ravi",
    "Surti",
    "Toda",
}


def normalize_breed_name(label: str) -> str:
    label = label.strip()
    if label in _LABEL_ALIASES:
        return _LABEL_ALIASES[label]
    if label in BREEDS:
        return label
    return label.replace("_", " ")


def get_breed_info(name: str) -> dict:
    key = normalize_breed_name(name)
    if key in BREEDS:
        info = BREEDS[key].copy()
        info.pop("color_hints", None)
        info.pop("visual", None)
        info["name"] = key
        return info

    animal_type = "Buffalo" if key in _BUFFALO_LABELS or name in _BUFFALO_LABELS else "Cattle"
    return {
        "name": key,
        "type": animal_type,
        "region": "India",
        "milk_yield": "Varies by animal",
        "lifespan": "12–18 years",
        "usage": "Dairy / draught",
        "description": f"{key} is a recognised bovine breed identified by the AI model.",
    }


def list_breeds() -> list:
    return [
        {
            "name": name,
            "type": data["type"],
            "region": data["region"],
            "milk_yield": data["milk_yield"],
            "description": data["description"],
        }
        for name, data in BREEDS.items()
    ]
