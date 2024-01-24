import logging
import requests
from os import getenv
from dotenv import load_dotenv
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.markdown import hbold

load_dotenv()

TOKEN = getenv("TOKEN")
API = getenv("API")

user_router = Router()

def get_token_price(token_id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=usd'
    headers = {'Authorization': f'Bearer {API}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()

        if 'error' in data:
            logging.error(f'Error from CoinGecko API: {data["error"]}')
            return None

        price = data[token_id]['usd']
        return price

    except requests.RequestException as e:
        logging.error(f'Request to CoinGecko API failed: {e}')
        return None

    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        return None

@user_router.message(Command('start'))
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(f'Hello, {hbold(msg.from_user.first_name)}! I am the {hbold('Crypto_currencies bot')}. Use {hbold('/btc /eth /bnb /cgpt /sfund')} commands to get the current token price.')

@user_router.message(Command('btc'))
async def get_btc(message: types.Message) -> None:
    price = get_token_price('bitcoin')
    if price is not None:
        await message.answer(f'Bitcoin price: {price} USD')
    else:
        await message.answer('Failed to get Bitcoin price')

@user_router.message(Command('eth'))
async def get_eth(message: types.Message) -> None:
    price = get_token_price('ethereum')
    if price is not None:
        await message.answer(f'Ethereum price: {price} USD')
    else:
        await message.answer('Failed to get Ethereum price')

@user_router.message(Command('bnb'))
async def get_bnb(message: types.Message) -> None:
    price = get_token_price('binancecoin')
    if price is not None:
        await message.answer(f'BNB price: {price} USD')
    else:
        await message.answer('Failed to get Binance Coin (BNB) price')

@user_router.message(Command('cgpt'))
async def get_cgpt(message: types.Message) -> None:
    price = get_token_price('chaingpt')
    if price is not None:
        await message.answer(f'ChainGPT price: {price} USD')
    else:
        await message.answer('Failed to get ChainGPT price')

@user_router.message(Command('sfund'))
async def get_sfund(message: types.Message) -> None:
    price = get_token_price('seedify-fund')
    if price is not None:
        await message.answer(f'Seedify Fund price: {price} USD')
    else:
        await message.answer('Failed to get Seedify Fund price')

