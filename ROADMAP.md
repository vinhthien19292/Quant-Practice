# Quant-Practice: Unlearn & Re-learn Roadmap

**Anchor problem**: *"Which is the most predictable range of a stock price in a specific period?"*

Every chapter must pass through 4 layers before it's considered done:
1. **Định nghĩa hình thức** — viết bằng ký hiệu toán, không phải chữ
2. **Chứng minh / dẫn xuất** — tự viết ra giấy, không copy
3. **Code from zero** — implement bằng numpy trước, rồi mới compare với thư viện chuẩn
4. **Ứng dụng vào 1 case Vietnam market** — VN30, cổ phiếu HOSE/HNX, warrant, futures

Không đủ 4 layer = chưa xong chapter đó. Không skip.

---

## 12-week arc

| Week | Chapter | WQU reference | Textbook backup | Deliverable |
|---|---|---|---|---|
| 1 | Returns & phân phối empirical | 610 M1 (Basic Stats) | Fat Tails (Taleb), Harvard Stats Cheat Sheet | Notebook: VN30 return distribution, normality test |
| 2 | Moments, skew, kurtosis, tail risk | 610 M1 + Fat Tails | — | Notebook: so sánh VN30 vs SPY tail behavior |
| 3 | Random walk → Brownian motion | 622 M1 (Brownian & Martingales) | Wiersema Ch 1-3 | Notebook: simulate Brownian paths |
| 4 | GBM, Ito's lemma | 622 M2 (Ito Process) | Wiersema Ch 4-5 | Notebook: GBM cho VN30, 95% CI range |
| 5 | Historical vol, EWMA | 610 M4 (Volatility Modeling) | — | Notebook: rolling vol VN30, compare methods |
| 6 | GARCH(1,1), realized vol | 610 M4 | — | Notebook: GARCH fit + forecast VN30 |
| 7 | Binomial tree → Black-Scholes | 620 M5 (Binomial) + 622 M5 (BS) | Wiersema Ch 6-7 | Notebook: BS price + convergence từ binomial |
| 8 | Greeks, implied vol | 622 M5 + 630 M2 (MC option pricing) + Dynamic Hedging (Taleb) | — | Notebook: Greeks cho VN warrant thực |
| 9 | Range estimators (Parkinson, GK) | 610 M4 + paper reading | — | Notebook: 5 vol estimators VN30 comparison |
| 10 | Vol cones, regime switching | 630 M5 (Local Vol) + 650 (ML clustering) | — | Notebook: regime detection VN30 HMM |
| 11 | VN30 futures, cost of carry, basis | 560 M6 (Futures/Options) | — | Notebook: basis trade backtest |
| 12 | Covered warrant, delta hedge, T+0 impact | 560 M7 (Market Making) + Capstone Options Track | — | Notebook: warrant pricing + hedge P&L |

---

## Weekly cadence

- **Mon-Tue** (3h): Đọc chapter PDF, viết proof ra giấy
- **Wed-Thu** (3h): Code notebook from zero, không copy
- **Fri** (2h): Áp dụng vào data VN, kiểm chứng
- **Sat** (2h): Review notebook cũ, làm Anki active recall
- **Sun**: Off hoặc catch-up

Total: 10h/tuần.

---

## Progress tracking

- [ ] Ch 01 — Returns & phân phối
- [ ] Ch 02 — Moments & tails
- [ ] Ch 03 — Brownian motion
- [ ] Ch 04 — GBM & Ito
- [ ] Ch 05 — Historical vol & EWMA
- [ ] Ch 06 — GARCH
- [ ] Ch 07 — Binomial & Black-Scholes
- [ ] Ch 08 — Greeks & implied vol
- [ ] Ch 09 — Range estimators
- [ ] Ch 10 — Vol cones & regime
- [ ] Ch 11 — VN30 futures
- [ ] Ch 12 — Covered warrant & options

Sau 12 tuần: có backtest thực trên VN market cho ít nhất 1 chiến lược derivatives.

---

## Folder structure

```
Quant-Practice/
├── PDF/                   Chapter HTML files (mở bằng browser, offline OK, tương tác)
├── Notebooks/             Jupyter notebooks (chạy trên laptop)
├── Data/                  VN30, warrants, futures data + checklist
├── Anki/                  Spaced repetition decks
├── Chapters-src/          Reserved (nếu sau này chuyển sang MkDocs)
└── ROADMAP.md             file này
```

**Format chương**: single HTML file per chapter, self-contained. Mở bằng browser bất kỳ (Chrome/Edge/Firefox trên laptop, Chrome/Samsung Internet trên Tab S). Tương tác được (slider, chart cập nhật live, quiz). Cần internet lần đầu để load Tailwind + Chart.js CDN — sau đó browser cache, offline OK.

**Style**: bình dân học vụ (MIT OCW). Không assume prerequisites về calculus/algebra/prob — giới thiệu just-in-time khi cần.

Path convention trong mọi notebook:
```python
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # đổi tên folder cha vô tư
DATA = PROJECT_ROOT / "Data"
```

---

## WQU source folder (reference, đừng chỉnh sửa)

`D:\OneDrive\1. Quant\World Quant - Master of Financial Engineering\`
