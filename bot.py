import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = 37266230
API_HASH = "c9f95b37dd021863d56426d500cc7227"
SESSION_STRING = "1BJWap1sBu6DjMs-MVEirTsNthEMuvujO55lm46aAuM62svvQa7S1xLZhLdftcsLGwy0dhFDt87WxUTxsTpJVy2jUuK0jmipuV9Q5nB5Fxw7Zl3alBsh8REzuMKs_dNfI7qAifLKnFi2p6FRfDE4pcms9nyjlBei5-zLxPDT7rM8h-h6pz1FqZ39ZgiusblCpdVPJ7zWfH9cgrprR3-aN8Ee2r1MnVa_UvXeOUzvbj4txhe8NWWXCA9b0Sb67tuEXSfLiYZfr3JGO4bK6tWbLWgWSPCWYHoSrV1Q8cqPkWKjzcgRBuUwQqLb0w6V88CCt7PtX1Ocpra3LLrG1IUMOhYdNNsQOG8c="

CHAT_IDS = [
    "@ChezMendoza",
    "@avietalpacino_pub",
    "@quadblade",
    "@chezkanoe",
    "@chezyatsu",
    "@chezalpha",
    "@chezz9",
    "@chezphineasesimsfr",
    "@chezdsavv",
    "@chezrass",
    "@chezdh",
    "@ChezObsidianV2",
    "@chezqui",
    "@creditviro261",
    "@pedrofabiente",
    "@chezZurgkennedy",
    "@plans_sous92",
    "@Chez_DuckLand",
    "@ChezHouse",
    "@chezlasolucee",
    "@onpaiepaslatva",
    "@chezlenfoiree",
    "@in_heisenberg_house",
    "@CvbienspasserUHQ",
    "@paradisduscam",
    "@blackwolfgroupe",
    "@chezmyflunch",
    "@vagabod",
    "@commecheztoi",
    "@LaLoiDuTalion",
    "@chezlocalbusnessChat",
    "@Aidefinaciere",
    "@CHEZSMAKA",
    "@aidefinancieres",
    "@chezdalton",
    "@chezbenzema",
    "@cheznyzoo",
    "@chezmekoi",
    "@ChezYtem",
    "@xbetcoupon90",
    "@groupeinfopositive",
    "@argentgratuitparrainage",
    "@prronooos",
    "@LACRIZ_OMIC",
    "@chezelea",
    "@chezelproffesor75",
    "@chezkaisencard"
]

SOURCE_CHANNEL = -1004297379788

async def main():
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        messages = await client.get_messages(SOURCE_CHANNEL, limit=1)
        last_message = messages[0]
        for chat_id in CHAT_IDS:
            try:
                await client.forward_messages(chat_id, last_message)
                print(f"Message transfere a {chat_id}")
            except Exception as e:
                print(f"Erreur pour {chat_id}: {e}")

asyncio.run(main())
