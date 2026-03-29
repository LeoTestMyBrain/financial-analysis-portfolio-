# SET50 Constituent List (Jan–Jun 2026)

set50 = [
    "ADVANC", "AOT", "AWC", "BANPU", "BBL",
    "BDMS", "BEM", "BH", "BJC", "BTS",
    "CBG", "CCET", "CENTEL", "COM7", "CPALL",
    "CPF", "CPN", "CRC", "DELTA", "EGCO",
    "GPSC", "GULF", "HMPRO", "IVL", "KBANK",
    "KKP", "KTB", "KTC", "LH", "MINT",
    "MTC", "OR", "OSP", "PTT", "PTTEP",
    "PTTGC", "RATCH", "SAWAD", "SCB", "SCC",
    "SCGP", "TCAP", "TIDLOR", "TISCO", "TLI",
    "TOP", "TRUE", "TTB", "TU", "WHA",
]

# สำหรับใช้กับ yfinance
set50_yf = [t + ".BK" for t in set50]

# SET50 Bank list
set50_banks = [
    "BBL", "KBANK", "SCB", "KTB",
    "KKP", "TISCO", "TTB", "TCAP",
]
set50_banks_yf = [t + ".BK" for t in set50_banks]

if __name__ == "__main__":
    print(f"SET50: {len(set50)} หลักทรัพย์")
    print(f"Banks: {len(set50_banks)} หลักทรัพย์")
