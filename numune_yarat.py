from pathlib import Path

import pandas as pd

QOVLUQ = Path(__file__).parent / "fayllar"
QOVLUQ.mkdir(exist_ok=True)   # qovluq yoxdursa yaradir


baki = pd.DataFrame({
    "Tarix":  ["2026-08-01", "2026-08-01", "2026-08-02", "2026-08-02"],
    "Mehsul": ["Noutbuk", "Sican", "Klaviatura", "Noutbuk"],
    "Say":    [2, 5, 3, 1],
    "Mebleg": [2400, 75, 120, 1200],
})
baki.to_excel(QOVLUQ / "baki.xlsx", index=False)


gence = pd.DataFrame({
    " TARIX ": ["2026-08-01", "2026-08-02", "2026-08-02"],
    "Mehsul ": ["Monitor", "Noutbuk", "Monitor"],
    " Say":    [1, 1, 2],
    "MEBLEG":  [450, 1200, 900],
})
gence.to_excel(QOVLUQ / "gence.xlsx", index=False)


sumqayit = pd.DataFrame({
    "Tarix":  ["2026-08-01", "2026-08-01", None, "2026-08-03"],
    "Mehsul": ["Printer", "Printer", None, "Sican"],
    "Say":    [1, 1, None, 4],
    "Mebleg": [320, 320, None, 60],
})
sumqayit.to_excel(QOVLUQ / "sumqayit.xlsx", index=False)


print("3 numune fayl yaradildi:", QOVLUQ)
print("Indi ise sal: python birlesdir.py")