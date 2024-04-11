import asyncio
from main import bot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from keyboards import reply


async def parsing(chat_id, **kwargs):
    city = kwargs['city']
    type_ads = kwargs['type_ads']
    type_housing = kwargs['type_housing']
    price_from = kwargs['price_from']
    price_to = kwargs['price_to']

    try:
        chrome_options = Options()
        chrome_options.add_argument('/Users/mac/Desktop/orders/bot_parser/functions/chromedriver')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get(f'https://www.halooglasi.com/nekretnine/{type_ads}-{type_housing}/{city}?cena_d_from={price_from}&cena_d_to={price_to}&cena_d_unit=4')
            await asyncio.sleep(5)
        except Exception:
            await bot.send_message(chat_id, 'Ошибка запроса!')
            return

        error = driver.find_elements(By.CLASS_NAME, 'error-404')

        if error:
            await bot.send_message(chat_id, 'Введите данные правильно!')
            return 
        
        with open('count.txt', 'r') as open_file:
            file_count = open_file.read()
        
        coming_count = driver.find_element(By.CLASS_NAME, 'ad-faceting-result-count').text.strip().split(' ')[0]
        

        coming_number = int(coming_count)
        file_number = int(file_count)

        with open('count.txt', 'w') as close_file:
            close_file.write(str(coming_number))

        if file_number == 0:
            await bot.send_message(chat_id, 'Начало работы бота')
            return

        if coming_number <= file_number:
            await bot.send_message(chat_id, 'Пока нет новых объявлений')
            return 

        result_count = coming_number - file_number

        all_elements = driver.find_elements(By.CLASS_NAME, 'my-product-placeholder')

        if not all_elements:
            await bot.send_message(chat_id, 'Нечего не найдено!')
            return 

        for item in all_elements[:result_count]:
            name = item.find_element(By.CSS_SELECTOR, 'h3.product-title a').text.strip()
            location = item.find_elements(By.CSS_SELECTOR, '.subtitle-places li')[0].text.strip()
            type_hous = type_housing
            square_meter = item.find_element(By.CSS_SELECTOR, '.value-wrapper').text.strip()
            price = item.find_element(By.CSS_SELECTOR, '.central-feature-wrapper span').get_attribute('data-value')
            url = item.find_element(By.CSS_SELECTOR, 'h3.product-title').find_element(By.TAG_NAME, 'a').get_attribute('href')

            square_meter = square_meter.replace("Kvadratura", "").strip()
            message = f"*Название:* {name}\n"
            message += f"*Местоположение:* {location}\n"
            message += f"*Тип жилья:* {type_hous}\n"
            message += f"*Площадь:* {square_meter}\n"
            message += f"*Цена:* {price}€\n"
            message += f"*Ссылка на объявление:* {url}"

            await bot.send_message(chat_id, message, parse_mode="Markdown", reply_markup=reply.cancel_kb)

    except Exception as error:
        await bot.send_message(chat_id, f'{error}')
    finally:
            driver.quit()
            


def stop_parser():
    global is_parser_running
    is_parser_running = False
    

async def parser(chat_id, **kwargs):

    await parsing(chat_id=chat_id, **kwargs)
    is_parser_running = True
    while is_parser_running:
        await asyncio.sleep(3600)
        await parsing(chat_id=chat_id, **kwargs)

        
        


