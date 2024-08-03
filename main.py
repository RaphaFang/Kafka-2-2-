import asyncio
from postgre_pool import create_pool

from producer.p_ebay import start_ebay_producer
from producer.p_amazon import start_amazon_producer
from producer.p_momo import start_momo_producer

from consumer.c_ebay import start_ebay_consumer
from consumer.c_amazon import start_amazon_consumer
from consumer.c_momo import start_momo_consumer


startup_keyword_list = [ "手機", "筆記型電腦", "無線耳機", "藍牙喇叭", "智能手錶", "遊戲主機", "平板電腦", "4K電視", "攝影機", "咖啡機", "空氣淨化器", "冰箱", "洗衣機", "微波爐", "風扇", "吸塵器", "廚房家電", "健身器材", "單車", "室內裝飾", "服裝", "美妝產品", "保健食品" ]
startup_keyword_list = [ "Smartphones", "Laptops", "Wireless Earbuds", "Bluetooth Speakers", "Smartwatches", "Gaming Consoles", "Tablets", "4K TVs", "Cameras", "Coffee Machines", "Air Purifiers", "Refrigerators", "Washing Machines", "Microwave Ovens", "Electric Fans", "Vacuum Cleaners", "Kitchen Appliances", "Fitness Equipment", "Bicycles", "Home Decor", "Clothing", "Beauty Products", "Health Supplements" ]

async def main_loop(pool):
    for k in startup_keyword_list:
        await asyncio.gather(
            start_ebay_producer(k),
            start_amazon_producer(k),
            start_momo_producer(k),

            start_ebay_consumer(pool),
            start_amazon_consumer(pool),
            start_momo_consumer(pool),
        )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    pool = loop.run_until_complete(create_pool())
    try:
        loop.run_until_complete(main_loop(pool))
    finally:
        loop.run_until_complete(pool.close())