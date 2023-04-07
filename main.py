import asyncio
from datetime import datetime

from dotenv import dotenv_values
import tweepy

LYRICS = [
    "I hear the drums echoing tonight",
    "But she hears only whispers of some quiet  conversation",
    "She's coming in, 12:30 flight",
    "The moonlit wings reflect the stars that guide me towards salvation",
    "I stopped an old man along the way",
    "Hoping to find some long forgotten words or ancient melodies",
    "He turned to me as if to say, \"Hurry boy, it's waiting there for you\"",
    "It's gonna take a lot to take me away from you",
    "There's nothing that a hundred men or more could ever do",
    "I bless the rains down in Africa",
    "Gonna take some time to do the things we never had",
    "The wild dogs cry out in the night",
    "As they grow restless, longing for some solitary company",
    "I know that I must do what's right",
    "As sure as Kilimanjaro rises like Olympus above the Serengeti",
    "I seek to cure what's deep inside",
    "Frightened of this thing that I've become",
    "It's gonna take a lot to drag me away from you",
    "There's nothing that a hundred men or more could ever do",
    "I bless the rains down in Africa",
    "Gonna take some time to do the things we never had",
    "[instrumental break]",
    "Hurry boy, she's waiting there for you",
    "It's gonna take a lot to drag me away from you",
    "There's nothing that a hundred men or more could ever do",
    "I bless the rains down in Africa",
    "Gonna take some time to do the things we never had"
]

async def main():
    # read .env into dict
    env = dotenv_values()
    client = tweepy.Client(
        consumer_key=env["CONSUMER_KEY"],
        consumer_secret=env["CONSUMER_SECRET"],
        access_token=env["ACCESS_TOKEN"],
        access_token_secret=env["ACCESS_SECRET"],
    )

    # print user info
    me = client.get_me()
    print(f'Assuming the identity of @{me.data.username} ({me.data.id})')

    line = 0
    # the main loop
    while True:
        print(f'Posting line #{line}: {LYRICS[line]}')
        client.create_tweet(text=LYRICS[line])
        line = (line+1) % len(LYRICS)
        print(f'Delaying for an hour... (started at {datetime.now().strftime("%I:%M:%S%p")})')
        await asyncio.sleep(3600)


if __name__ == '__main__':
    asyncio.run(main())