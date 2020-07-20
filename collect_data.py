import oi_mark_funding as exchange_data
import pause
from datetime import datetime
import time



ura = datetime(2020,7,10,17,45,0)    
pause.until(ura)

i = 0
week_15min_int = 7 * 24 * 4
min15 = 60 * 15



while i < week_15min_int:

    start_time = time.time()   # timestap

    i = i + 1
    print(f"getting data #{i}")

    exchange_data.get_and_store_btc_data()
    exchange_data.get_and_store_eth_data()

    exe_time = time.time() - start_time             # calculates script execution time
    print(f"script execution time was: {exe_time}s")
    time.sleep(min15 - exe_time)                    # subtracts script execution time from time interval so we don't get data request delays

print("----------------------------1 WEEK OF BTC OI/FUNDING/MARK_PRICE DATA IS COLLECTED-------------------------------")