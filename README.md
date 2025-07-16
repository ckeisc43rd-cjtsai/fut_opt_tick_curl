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