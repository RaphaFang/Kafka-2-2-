import asyncio
from producer.p_ebay import start_ebay_producer
from consumer.c_ebay import start_ebay_consumer

from producer.p_amazon import start_amazon_producer
from consumer.c_amazon import start_amazon_consumer



async def main_loop():
    await asyncio.gather(
        start_ebay_producer(),
        start_amazon_producer(),

        start_ebay_consumer(),
        start_amazon_consumer(),
    )

if __name__ == "__main__":
    asyncio.run(main_loop())