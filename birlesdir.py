from pathlib import Path
import pandas as pd

QOVLUQ = Path(__file__).parent / "fayllar"
NETICE = Path(__file__).parent / "birlesmis.xlsx"


hamisi = []

for fayl in sorted(QOVLUQ.glob("*.xlsx")):
    # Excel acilanda "~$ad.xlsx" kimi kolge fayl yaradir, onu atlayiriq
    if fayl.name.startswith("~$"):
        continue

    df = pd.read_excel(fayl)
    df.columns = df.columns.str.strip().str.lower()
    df = df.dropna(how="all")   #any

    # hansi fayldan geldiyi bilinsin
    df["menbe_fayl"] = fayl.stem

    hamisi.append(df)
    print("  oxundu:", fayl.name, "-", len(df), "setir")


if not hamisi:
    print("Qovluqda Excel fayli tapilmadi.")
    raise SystemExit


# ---- 2) Hamisini alt-alta yapisdir ----
cedvel = pd.concat(hamisi, ignore_index=True)
xam_say = len(cedvel)


# ---- 3) Temizle ----
# menbe_fayl sutunu istisna edilir, yoxsa ferqli fayllardaki
# eyni setirler tekrar sayilmaz
sutunlar = [s for s in cedvel.columns if s != "menbe_fayl"]
cedvel = cedvel.drop_duplicates(subset=sutunlar)

# tarix sutununu real tarix tipine cevir
# errors="coerce" - cevrile bilmeyeni xeta vermeden bos (NaT) edir
cedvel["tarix"] = pd.to_datetime(cedvel["tarix"], errors="coerce")


# ---- 4) Yaz ----
cedvel.to_excel(NETICE, index=False)

print()
print(len(hamisi), "fayl birlesdi")
print(xam_say, "xam setir ->", len(cedvel), "temiz setir")
print("Atilan:", xam_say - len(cedvel), "setir")
print("Netice:", NETICE.name)