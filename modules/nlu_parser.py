"""
Natural Language Understanding för juridiska dokument
Identifierar parter, rättsområden, beslutstyp, myndigheter och rättsgrunder
"""

def parse_document(text):
    parsed = {
        "parter": [],
        "myndighet": "",
        "ärendetyp": "",
        "rättsområde": "",
        "identifierade_begrepp": []
    }

    if "Försäkringskassan" in text:
        parsed["myndighet"] = "Försäkringskassan"
        parsed["rättsområde"] = "Socialförsäkringsrätt"
    if "avslag" in text.lower() or "överklagande" in text.lower():
        parsed["ärendetyp"] = "Överklagande"

    for begrepp in ["SGI", "sjukpenning", "inkomstbortfall", "FL 25 §", "SFB 27 kap."]:
        if begrepp in text:
            parsed["identifierade_begrepp"].append(begrepp)

    return parsed
