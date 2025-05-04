"""
Analys av argumentation: styrka, logiska brister, invändningar
"""

def analyze_arguments(text):
    if "kommunicerades ej" in text:
        return "Formaliabrist enligt FL 25 § – partsinsyn har ej tillgodosetts."
    if "felaktig rättstillämpning" in text:
        return "Invändning mot rättsgrund – bör prövas mot HFD-praxis."
    return "Ej tillräckligt underlag för bedömning av argumentens styrka."
