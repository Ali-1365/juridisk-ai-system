"""
Identifierar juridiska risker: preskription, partsbrister, kommunikationsfel
"""

def assess_risks(text):
    risks = []
    if "beslut utan kommunikation" in text:
        risks.append("Formaliafel: Brott mot FL 25 §")
    if "fel part" in text:
        risks.append("Processhinder: ogiltig partsställning")
    if "för sent inkommet" in text:
        risks.append("Tidsfrist: risk för avvisning enligt SFB 113 kap.")

    return risks
