# Data cần chuẩn bị cho 12-week roadmap

Fetch dần, không cần lấy hết cùng lúc. Mỗi chapter chỉ cần 1-2 file.

## Chapter 1-2 (Returns & phân phối) — CẦN NGAY

**File**: `vn30_daily.csv`
- Cột: `date, close`
- Khoảng thời gian: **2015-01-01 → hôm nay** (~10 năm, ~2500 dòng)
- Nguồn khả dĩ: vietstock, fireant, cafef, TradingView export, hoặc `pip install vnstock` rồi:
  ```python
  from vnstock import Vnstock
  stock = Vnstock().stock(symbol='VN30', source='VCI')
  df = stock.quote.history(start='2015-01-01', end='2025-07-21', interval='1D')
  df[['time','close']].to_csv('vn30_daily.csv', index=False)
  ```

**File**: `vnm_daily.csv`, `hpg_daily.csv`, `fpt_daily.csv` — 3 cổ phiếu đại diện 3 sector
- Cùng format, cùng thời gian

## Chapter 3-4 (Brownian, GBM) — dùng lại data trên
Không cần thêm.

## Chapter 5-6 (Vol, GARCH, realized vol) — CẦN INTRADAY
**File**: `vn30_intraday_5min.csv`
- Cột: `datetime, open, high, low, close, volume`
- Khoảng thời gian: **6 tháng gần nhất** là đủ
- Nguồn: TradingView export, hoặc broker API (SSI, VNDIRECT có API)

## Chapter 7-8 (Black-Scholes, Greeks) — CẦN OPTION/WARRANT
**File**: `warrant_list.csv` — danh sách covered warrant đang niêm yết
- Cột: `symbol, underlying, strike, expiry, conversion_ratio, issuer`
- Nguồn: HOSE website, hoặc broker

**File**: `warrant_prices_daily.csv` — giá đóng cửa của 5-10 warrant chọn lọc
- Cùng cấu trúc daily
- Khoảng thời gian: từ khi phát hành → giờ

## Chapter 9-10 (Range estimators, regime) — dùng lại data trên
Cần OHLC, không chỉ close. Nên chapter 1 fetch luôn OHLC cho tiện:
- Cập nhật `vn30_daily.csv` thành `date, open, high, low, close, volume`

## Chapter 11-12 (Futures, warrant hedge, T+0) — CẦN FUTURES
**File**: `vn30f1m_daily.csv` — VN30 futures near month
- Cột: `date, open, high, low, close, volume, open_interest`
- Khoảng thời gian: 2018 → giờ (từ khi VN30 futures ra mắt)

## Ghi chú
- CSV, UTF-8, header row.
- Ngày định dạng `YYYY-MM-DD` để tránh confusion Mỹ/châu Âu.
- Đặt tất cả file trong folder này (`Quant-Practice/Data/`).
- Notebook mỗi chapter sẽ đọc theo tên file trên — không cần đổi code.
