# TW Futures and Options Tick Data Crawler
### Usage:

```!
$ ./run.sh
```
自動儲存前30個交易日之期貨及選擇權tick資料至 fut / 及 opt/

---

```!
$ ./register_cron.sh
```
將 run.sh 註冊進 crontab 使其每天 8:00 及 18:00 會進行檢測是否有遺漏的資料，若有，會透過爬蟲將其補上

### Example:
<details>
<summary> example after executing </summary>

```!
.
├── crawler.py
├── fut
│   ├── Fut_2025_06_05.zip
│   ├── Fut_2025_06_06.zip
│   ├── Fut_2025_06_09.zip
│   ├── Fut_2025_06_10.zip
│   ├── Fut_2025_06_11.zip
│   ├── Fut_2025_06_12.zip
│   ├── Fut_2025_06_13.zip
│   ├── Fut_2025_06_16.zip
│   ├── Fut_2025_06_17.zip
│   ├── Fut_2025_06_18.zip
│   ├── Fut_2025_06_19.zip
│   ├── Fut_2025_06_20.zip
│   ├── Fut_2025_06_23.zip
│   ├── Fut_2025_06_24.zip
│   ├── Fut_2025_06_25.zip
│   ├── Fut_2025_06_26.zip
│   ├── Fut_2025_06_27.zip
│   ├── Fut_2025_06_30.zip
│   ├── Fut_2025_07_01.zip
│   ├── Fut_2025_07_02.zip
│   ├── Fut_2025_07_03.zip
│   ├── Fut_2025_07_04.zip
│   ├── Fut_2025_07_07.zip
│   ├── Fut_2025_07_08.zip
│   ├── Fut_2025_07_09.zip
│   ├── Fut_2025_07_10.zip
│   ├── Fut_2025_07_11.zip
│   ├── Fut_2025_07_14.zip
│   ├── Fut_2025_07_15.zip
│   └── Fut_2025_07_16.zip
├── opt
│   ├── Opt_2025_06_05.zip
│   ├── Opt_2025_06_06.zip
│   ├── Opt_2025_06_09.zip
│   ├── Opt_2025_06_10.zip
│   ├── Opt_2025_06_11.zip
│   ├── Opt_2025_06_12.zip
│   ├── Opt_2025_06_13.zip
│   ├── Opt_2025_06_16.zip
│   ├── Opt_2025_06_17.zip
│   ├── Opt_2025_06_18.zip
│   ├── Opt_2025_06_19.zip
│   ├── Opt_2025_06_20.zip
│   ├── Opt_2025_06_23.zip
│   ├── Opt_2025_06_24.zip
│   ├── Opt_2025_06_25.zip
│   ├── Opt_2025_06_26.zip
│   ├── Opt_2025_06_27.zip
│   ├── Opt_2025_06_30.zip
│   ├── Opt_2025_07_01.zip
│   ├── Opt_2025_07_02.zip
│   ├── Opt_2025_07_03.zip
│   ├── Opt_2025_07_04.zip
│   ├── Opt_2025_07_07.zip
│   ├── Opt_2025_07_08.zip
│   ├── Opt_2025_07_09.zip
│   ├── Opt_2025_07_10.zip
│   ├── Opt_2025_07_11.zip
│   ├── Opt_2025_07_14.zip
│   ├── Opt_2025_07_15.zip
│   └── Opt_2025_07_16.zip
├── README.md
├── register_cron.sh
├── requirements.txt
└── run.sh
```
</detail>