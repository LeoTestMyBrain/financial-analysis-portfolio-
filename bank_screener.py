import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. ดึงข้อมูล
banks = ["BBL.BK","KBANK.BK","SCB.BK","KTB.BK",
         "KKP.BK","TISCO.BK","TTB.BK","TCAP.BK"]

rows = []
for ticker in banks:
    info = yf.Ticker(ticker).info
    rows.append({
        "Ticker":   ticker.replace(".BK",""),
        "Price":    info.get("currentPrice"),
        "ROE":      round(info.get("returnOnEquity", 0) * 100, 2),
        "PBV":      round(info.get("priceToBook", 0), 2),
        "DivYield": info.get("dividendYield"),
    })

df = pd.DataFrame(rows)

# 2. คำนวณ
g, CoE = 0.03, 0.10
df["BV"]         = round(df["Price"] / df["PBV"], 2)
df["Just_PBV"]   = round((df["ROE"]/100 - g) / (CoE - g), 2)
df["Fair_Price"] = round(df["Just_PBV"] * df["BV"], 2)
df["Upside"]     = round(((df["Fair_Price"] - df["Price"]) / df["Price"]) * 100, 1)

# 3. Signal
def signal(u):
    if u > 15:  return "BUY"
    elif u > 0: return "HOLD"
    else:       return "AVOID"

df["Signal"] = df["Upside"].apply(signal)
df = df.sort_values("Upside", ascending=False)

# 4. Chart
colors = {"BUY":"#1D9E75", "HOLD":"#EF9F27", "AVOID":"#E24B4A"}
bar_colors = df["Signal"].map(colors)

plt.figure(figsize=(10, 5))
plt.bar(df["Ticker"], df["Upside"], color=bar_colors)
plt.axhline(y=0,  color="black", linewidth=0.8)
plt.axhline(y=15, color="#1D9E75", linestyle="--", label="BUY threshold")
plt.title("Justified Price Upside — SET50 Banks")
plt.xlabel("Ticker")
plt.ylabel("Upside %")
plt.legend()
plt.tight_layout()
plt.savefig("justified_price.png", dpi=150, bbox_inches="tight")
plt.show()
print("บันทึก justified_price.png แล้วค่ะ!")

# 5. สรุป
print("\n=== Stock Screener ===")
print(df[["Ticker","Price","Fair_Price","Upside","Signal","DivYield"]].to_string(index=False))
