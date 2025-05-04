"""
Jämför ärendets innehåll med kända prejudikat
"""

def match_precedent(keywords):
    matches = []
    if "HFD 2021 ref. 63" in keywords or "felaktig rättshandlingskonversion" in keywords:
        matches.append("HFD 2021 ref. 63 – Otillåten rättshandlingskonversion")
    if "SGI" in keywords:
        matches.append("HFD 2018 ref. 51 – SGI-nivå vid aktivitetsersättning")

    return matches
