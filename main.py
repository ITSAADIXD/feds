import os
import pytz
import time
import datetime
import asyncio
from pyrogram import filters, Client, idle
from pyrogram.errors import FloodWait as gey
from pyrogram.types.messages_and_media.message import Message
from pyrogram.types import ChatPrivileges

API_ID = os.environ.get("APIID", "1749732")
API_HASH = os.environ.get("APIH", "16ebcc625d37787bbb872a33a6ac1ea3")
SESSION = os.environ.get("SESSION", "BQCikHDzgjVlKK09xs-OoOoCE4aPNxBfnFy_b0PtjbRsVBdz3p9eonjPXLlS_QU03pK3htMbxyRpDRQgPeforfGhWos_sD5hXBjtSatq5LrBQ6RccbULOgZ2X3GNME4woP1MZcO7ki2PTcK4yTfQMHr4DGkxJJumsaK9dg9yKfj5-LnrsuDnAF31xq25bt-rvGAKXQSW2HSmnfEFfDaD6HMUBRijoHU5QrCj27Mn_t3Iix23mdWeqbsnVBCZHo2zwJxLU9DBhOthI971xxBFrpWLBKVuK8fRKqtgjwvhHIF96xv05XQ0LByyhbj4raRAjwbYjLTVIbOIw1a-3ELEO-PzScIIMgA")
CHANNELID = os.environ.get("CHANNELID", "-1001462326719")
MESSAGEID = os.environ.get("MESSAGEID", "14")
GRPNAME = os.environ.get("GROUPNAME", "StarPanel.top")
BOTUNAME = os.environ.get("BOTUNAME", "@missrose_bot")
OWNERID = os.environ.get("OID", "")

"""
API_ID2 = os.environ.get("APIID", "1749732")
API_HASH2 = os.environ.get("APIH", "16ebcc625d37787bbb872a33a6ac1ea3")
SESSION2 = os.environ.get("SESSION", "BQCikHDzgjVlKK09xs-OoOoCE4aPNxBfnFy_b0PtjbRsVBdz3p9eonjPXLlS_QU03pK3htMbxyRpDRQgPeforfGhWos_sD5hXBjtSatq5LrBQ6RccbULOgZ2X3GNME4woP1MZcO7ki2PTcK4yTfQMHr4DGkxJJumsaK9dg9yKfj5-LnrsuDnAF31xq25bt-rvGAKXQSW2HSmnfEFfDaD6HMUBRijoHU5QrCj27Mn_t3Iix23mdWeqbsnVBCZHo2zwJxLU9DBhOthI971xxBFrpWLBKVuK8fRKqtgjwvhHIF96xv05XQ0LByyhbj4raRAjwbYjLTVIbOIw1a-3ELEO-PzScIIMgA")
app2 = Client(name="omk", session_string=SESSION, api_id=API_ID, api_hash=API_HASH)
def main():
    with app:
        while True:
           print("Starting adding chats.... /")
           k = app.send_message(int(f"{CHANNELID}"), "starting...")
           try:
               ok = app.create_supergroup(GRPNAME, "Create by aju")
               ok = app2.create_supergroup(GRPNAME, "Create by aju")
               
               okii2 = app.get_messages(int(f"{CHANNELID}"), int(f"{MESSAGEID}"))
               FID = okii2.text
               app.add_chat_members(ok.id, f"{BOTUNAME}")
               app.promote_chat_member(
                   chat_id=ok.id,
                   user_id=f"{BOTUNAME}",
                   privileges=ChatPrivileges(can_restrict_members=True),
               )
               app2.add_chat_members(ok.id, f"{BOTUNAME}")
               app2.promote_chat_member(
                   chat_id=ok.id,
                   user_id=f"{BOTUNAME}",
                   privileges=ChatPrivileges(can_restrict_members=True),
               )
               app2.send_message(ok.id, f"/joinfed {FID}") 
           
               app.send_message(ok.id, f"/joinfed {FID}") 
           except gey as e:
               asyncio.sleep(e.x)
           except:
               app.send_message(int(f"{OWNERID}"), f"Error")
               app.leave_chat(int(f"{CHANNELID}"))
               app2.send_message(int(f"{OWNERID}"), f"Error")
               app2.leave_chat(int(f"{CHANNELID}"))
           time.sleep(20)
            
if __name__ == "__main__":
   main()

"""
app = Client(name="omk", session_string=SESSION, api_id=API_ID, api_hash=API_HASH)

def main():
    with app:
        while True:
           print("Starting adding chats.... /")
           k = app.send_message(int(f"{CHANNELID}"), "starting...")
           try:
               ok = app.create_supergroup(GRPNAME, "Create by aju")
               okii2 = app.get_messages(int(f"{CHANNELID}"), int(f"{MESSAGEID}"))
               FID = okii2.text
               app.add_chat_members(ok.id, f"{BOTUNAME}")
               app.promote_chat_member(
                   chat_id=ok.id,
                   user_id=f"{BOTUNAME}",
                   privileges=ChatPrivileges(can_restrict_members=True),
               )
               app.send_message(ok.id, f"/joinfed {FID}") 
           except gey as e:
               asyncio.sleep(e.x)
           except:
               app.send_message(int(f"{OWNERID}"), f"Error")
               app.leave_chat(int(f"{CHANNELID}"))
           time.sleep(20)
            
if __name__ == "__main__":
   main()
