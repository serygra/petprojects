import sendemailscript
import requests
import json
import time

item_watchlist = [
{
    "price_ceiling": "221.00",
    "def_index": "5032", # hand wraps
    "paint_index": "10053" # cobalt skulls
},
{
    "price_ceiling": "380.00",
    "def_index": "523", # talon knife
    "paint_index": "42" # blue steel
} # to add more items add another dictionary here if desired
]

def main():
    for item in item_watchlist:
        price_ceiling = item["price_ceiling"]
        price_ceiling = price_ceiling.replace(".","")
        def_index = item["def_index"]
        paint_index = item["paint_index"]

        headers = {
            # api found in csfloat profile settings
            "Authorization": "add your api key here" # modification required
        }

        response = requests.get(f"https://csfloat.com/api/v1/listings?type=buy_now&max_price={price_ceiling}&def_index={def_index}&paint_index={paint_index}", headers=headers)

        obj = response.json()
        for result in obj.get("data", []):
            if len(result) > 0:
                subject_info = f"""
    {result['item']['item_name']} - MATCH FOUND!!
    """
                body_info = f"""
A new matching item was found on CSFloat!

Price Ceiling Parameter: {int(price_ceiling) / 100:.2f} USD

Name: {result['item']['item_name']}
Price: {int(result['price']) / 100:.2f} USD
Float: {result['item']['float_value']}
Avg Trade Time: {int(result['seller']['statistics']['median_trade_time']) / 60:.2f} Minutes
Successful Transactions: {int(result['seller']['statistics']['total_verified_trades'])}
Failed Transactions: {int(result['seller']['statistics']['total_avoided_trades']) + int(result['seller']['statistics']['total_failed_trades'])}
URL: https://csfloat.com/search?type=buy_now&max_price={price_ceiling}&def_index={def_index}&paint_index={paint_index}
"""
                sendemailscript.send_email(
                    subject=subject_info,
                    body=body_info,
                    to_email="your email here" # modification required
                )
                time.sleep(10)

if __name__ == "__main__":
    main()
