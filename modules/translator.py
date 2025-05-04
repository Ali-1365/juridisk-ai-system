"""
Enkel manuell översättare mellan svenska och persiska för juridiska etiketter.
"""

def translate_sv_to_fa(label):
    dictionary = {
        "Dokumentanalys (NLU)": "تحلیل سند (پردازش زبان طبیعی)",
        "Argumentationsanalys": "تحلیل استدلال",
        "Riskbedömning": "ارزیابی ریسک",
        "Prejudikatmatchning": "مطابقت با رویه قضایی",
        "Strategiförslag": "پیشنهاد راهبردی",
        "Skadeståndsberäkning": "محاسبه خسارت",
        "Inkomstbortfall per månad": "کاهش درآمد ماهانه",
        "Antal månader": "تعداد ماه‌ها",
        "Sveda och värk": "درد و رنج",
        "Ideell skada": "آسیب معنوی",
        "Resultat": "نتیجه"
    }
    return dictionary.get(label, label)
