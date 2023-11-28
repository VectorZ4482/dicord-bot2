import discord
from discord.ext import commands
import config

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">>", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready, go gaya ha ready.")
    await bot.tree.sync()



@bot.tree.command(description="Display All Available Payment methods")
async def paymentmethods(interaction: discord.Interaction):
    embed = discord.Embed(title="VIVA STORE PAYMENT METHODS", color=discord.Color.red())
    embed.add_field(name="LOCAL PAYMENTS", value="\nEasypaisa: **/easypaisa**\nJazzcash: **/jazzcash**\nSadayapy: **/sadapay**\nNayapay: **/nayapay\n\n**", inline=False)
    embed.add_field(name="\nCRYPTO PAYMENTS\n", value="BTC: **/btc**\nLTC: **/ltc**\n\n", inline=False)
    embed.add_field(name="CARD PAYMENTS", value="*Card Payment Also Available On Demand*\n*Contact <@1035613602423504966> For Card Payments*", inline=False   )
    await interaction.response.send_message(embed=embed)


@bot.tree.command(description="Display Easypaisa Number")
async def easypaisa(interaction: discord.Interaction):
    embed = discord.Embed(title="EASYPAISA\n", description="**Number: 03112874063**\n\n**Name: Shah Mohiuddin**", color=discord.Color.red())
    embed.set_image(url="https://media.discordapp.net/attachments/1088075924114776096/1109137064919826562/f4ccc860-a6d8-4ab3-8bad-6da5f8258b1c.png?width=392&height=675")
    embed.set_footer(text="Send Screenshot Of\nTransaction Receipt After\nSending Money", icon_url="https://cdn.discordapp.com/attachments/1088075924114776096/1109138374666752120/Afx97t2J531HAAAAAElFTkSuQmCC.png")

    await interaction.response.send_message(embed=embed)

@bot.tree.command(description="Display Jazzcash Number")
async def jazzcash(interaction: discord.Interaction):
      embed = discord.Embed(title="JAZZCASH\n", description="**Number: 03002378592**\n\n**Name: FARASAT ALI**", color=discord.Color.red())
      embed.set_image(url="https://cdn.discordapp.com/attachments/1088075924114776096/1109140404449849406/fb9b703b-b5cc-4591-84d9-51f4dc8b5368.png")
      embed.set_footer(text="Send Screenshot Of Transaction Receipt After\nSending Money", icon_url="https://cdn.discordapp.com/attachments/1088075924114776096/1109139570144067584/1200px-Jazz_logo.png")

      await interaction.response.send_message(embed=embed)


@bot.tree.command(description="Display Sadapay Number")
async def sadapay(interaction: discord.Interaction):
    embed = discord.Embed(title="SADAPAY\n", description="**Number: 03112874063**\n\n**IBAN: PK38SADA0000003112874063**\n\n**Name: Shah Mohiuddin**", color=discord.Color.red())
    await interaction.response.send_message(embed=embed)


@bot.tree.command(description="Display Nayapay Number")
async def nayapay(interaction: discord.Interaction):
    embed = discord.Embed(title="NAYAPAY\n", description="**Number: 03112874063**\n\n**IBAN: PK74NAYA1234503112874063**\n\n**Name: Shah Mohiuddin**", color=discord.Color.red())
    await interaction.response.send_message(embed=embed)



@bot.tree.command(description="Display Lite Coin Wallet Address")
async def ltc(interaction: discord.Interaction):
    embed = discord.Embed(title="LTC\n", description="**Address:\nLVx9qvdjReo5sUeca51n7i7gaRDts3v8wx**", color=discord.Color.red())
    embed.set_image(url="https://cdn.discordapp.com/attachments/1088075924114776096/1109202865001598996/16baf2bd-a8db-45db-acb2-00a46ad5d7ff.png")
    embed.set_footer(text="Send Screenshot Of Transaction Receipt After\nSending Money", icon_url="https://cdn.discordapp.com/attachments/1088075924114776096/1109203052222746826/2048px-LTC-400.png")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(description="Display Bitcoin Wallet Address")
async def btc(interaction: discord.Interaction):
    embed = discord.Embed(title="BTC\n", description="**Address:\n12AJrB6gC798d31P5DezngKPNn9WPRYp5F**", color=discord.Color.red())
    embed.set_image(url="https://cdn.discordapp.com/attachments/1088075924114776096/1109291777913008208/731c63d3-1040-4f4c-a8df-abca4c4cd7c9.png")
    embed.set_footer(text="Send Screenshot Of Transaction Receipt After\nSending Money", icon_url="https://cdn.discordapp.com/attachments/1088075924114776096/1109291545393373245/png-transparent-bitcoin-cryptocurrency-virtual-currency-decal-blockchain-info-bitcoin-text-trademark-logo.png")
    await interaction.response.send_message(embed=embed)



@bot.tree.command(description="Display TOS")
async def tos(interaction: discord.Interaction):
    embed = discord.Embed(title="VIVA STORE :  Terms & Service", description="\n\n**BY PLACING AN ORDER YOU WILL AUTOMATICALLY\nACCEPT THE TERMS & SERVICES**\n\n-Payment must be made before receiving the order\n\n-Refund will NOT be possible if the supplier will scam me\n\n-Refund will NOT be possible if you wish to cancel your order\n\n-Pre orders are NON-refundable\n\n-Spam = ignore / ban / no refund\n\n-You have to send feedback after receiving the order\n\n-No rep after delivery = no warranty\n\n-Accuse of scam = no refund\n\n-Negative feedback without proof = ban", color=discord.Color.red() )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1088075924114776096/1109297747766562867/Capture.PNG")
    embed.set_footer(text="In Order To Purchase Something, These Terms  Of\nService Must Be Accepted.", icon_url="https://cdn.discordapp.com/attachments/1088075924114776096/1109297696596054156/Capture-removebg-preview_1.png")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(description="Display Netflix Disclaimer")
async def netflix(interaction: discord.Interaction):
    embed = discord.Embed(title="NETFLIX DISCLIAMER", description="When you change your screen name, we lose track of it in our database and can sell it to others because we have no record of it.", color=discord.Color.red() )
    await interaction.response.send_message(embed=embed)


@bot.tree.command(description="Display Discord Nitro Disclaimer")
async def gay(interaction: discord.Interaction):
    embed = discord.Embed(title="DISCORD NITRO", description="You Must Provide An Additional Google Account For Discord Nitro Via Login. If You Do Not Offer An Additional Google Account, Your Purchase Will Not Be Returned.", color=discord.Color.red())
    await interaction.response.send_message(embed=embed)


@bot.tree.command(description="Display Discord Nitro Disclaimer")
async def dc(interaction: discord.Interaction):
    embed = discord.Embed(title="DISCORD NITRO", description="You Must Provide An Additional Google Account For Discord Nitro Via Login. If You Do Not Offer An Additional Google Account, Your Purchase Will Not Be Returned.", color=discord.Color.red() )
    await interaction.response.send_message(embed=embed)



@bot.tree.command()
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, amount:int):
    await interaction.channel.purge(limit=amount)
    await interaction.response.send_message(f"**Successfully Deleted {amount} Messages.**", ephemeral=True)


@clear.error
async def on_error(interation:discord.Interaction, error:commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        await interation.response.send_message("You Don't Have Permissons To Use This Command", ephemeral=True)


        
        
    

 

bot.run(config.DISCORD_TOKEN)