"""
Beräknar skadestånd enligt svensk rättspraxis (SFB, NJA, m.m.)
"""

def calculate_damages(income_loss, months, sveda_vark=20000, ideell_skada=10000):
    total_loss = income_loss * months
    total = total_loss + sveda_vark + ideell_skada
    return {
        "inkomstbortfall": total_loss,
        "sveda_och_värk": sveda_vark,
        "ideell_skada": ideell_skada,
        "totalbelopp": total
    }
