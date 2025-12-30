
# 🚀 Binance Futures Trading Bot (Testnet)

A **lightweight, command-line based trading bot** built using **Python** and **Binance Futures Testnet API**.
This project demonstrates real-world trading automation, order execution, and clean CLI interaction.

---

## 📌 Features

✅ Market Orders
✅ Limit Orders
✅ Stop-Limit Orders
✅ Interactive CLI Interface
✅ Binance Futures Testnet Support
✅ Logging & Error Handling
✅ Clean, Modular Codebase

---

## 🧠 Technologies Used

* **Python 3**
* **Binance Official Python SDK**
* **Git & GitHub**
* **CLI-based UI**
* **REST API**

---

## 📂 Project Structure

```
binance/
│
├── bot.py               # Main trading bot logic
├── config.py            # API credentials
├── logger.py            # Logging setup
├── README.md            # Documentation
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Gourav232003/BINANCE_BOT.git
cd BINANCE_BOT
```

---

### 2️⃣ Install Dependencies

```bash
pip install python-binance
```

---

### 3️⃣ Configure API Keys

Edit `config.py`:

```python
API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_SECRET"
BASE_URL = "https://testnet.binancefuture.com"
```

⚠️ **Never expose your real API keys publicly**

---

## ▶️ How to Run

```bash
python bot.py
```

You’ll see:

```
================================
   BINANCE FUTURES TRADING BOT
================================
1. Market Order
2. Limit Order
3. Stop-Limit Order
0. Exit
```

---

## 📊 Order Types Supported

### 🔹 Market Order

Executes immediately at current market price.

### 🔹 Limit Order

Executes only at the specified price.

### 🔹 Stop-Limit Order

Triggers a limit order once the stop price is hit.

---

## 🧪 Example Usage

```
Select option: 1
Symbol: BTCUSDT
Side: BUY
Quantity: 0.001
```

Output:

```
[✓] Market Order Executed
Order ID: 342892374
```

---

## 📝 Logging

All API activity and errors are logged automatically in:

```
trade.log
```

This helps in debugging and auditing trades.

---

## 🔒 Safety Notes

* Uses **Binance Testnet only**
* No real funds involved
* API keys should be kept secret
* Do NOT push `.env` or keys to GitHub

---

## 🚀 Future Enhancements

* ✅ Grid Trading Strategy
* ✅ TWAP Execution
* 🔄 Live Price Streaming (WebSocket)
* 📈 PnL & Position Tracking
* 🌐 Web Dashboard (Flask)

---

## 👨‍💻 Author

**Gourav**
Aspiring Backend & Trading Systems Developer

GitHub: [https://github.com/Gourav232003](https://github.com/Gourav232003)

---

## ⭐ Star this repo if you find it useful!

Happy Trading 🚀
