# Place for imports
import os
import time
from pypresence import Presence
from time import time

# Step to set RPC 
def step1():

    RPC = Presence(client_id)
    RPC.connect()
    
    if big_image == "nothing" or big_image == "":
        try:
            RPC.update(state=big_text, details=small_text, start=time())
        except:
            RPC.disconnect
            print("Something wrong happened!")
            os.system("pause")
    else:
        try:
            RPC.update(state=second_text, details=first_text, large_image=big_image, small_image=mini_image, start=time())
        except:
            RPC.disconnect
            print("Something wrong happened!")
            os.system("pause")

# Start script
print("=====================================")
print("Discord Rich Presence setter by @wink05 (at github)")
print("=====================================")
print("First we need your Discord APP ID.")
print("If you don't have one you can just make app at:")
print(" https://discord.com/developers/applications ")
print("=====================================")
client_id = input("Paste your APP ID here: ")
print("Great!")
print("=====================================")
first_text = input("Now type what you want in first text: ")
print("Great!")
second_text = input("Now type what you want in second text: ")
print("Great!")
print("=====================================")
big_image = input("Now type big image name: (if you dont have/want to use it write 'nothing', if you dont use big image, small image will be not available.) ")
if big_image == "nothing" or big_image == "":
    print("Image option are now disabled.")
else:
    mini_image = (input("Now type small image name: "))
print("Now we're done! Going to setting...")
print("====================================")
print("Warning! You have to keep this script open until you want to RPC status be visible.")

while True:
    step1()

