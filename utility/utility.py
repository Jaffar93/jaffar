import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import random
import asyncio
import time

class UtilityCommands(commands.Cog):
    """Fun commands for members to use!!"""
    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.plugin_db.get_partition(self)
     
    async def get_channel(self, channel_id):
        """Returns a discord.Channel object for the specified channel ID."""
        return discord.utils.get(self.bot.guilds[0].channels, id=channel_id)

   

    @checks.has_permissions(PermissionLevel.MODERATOR)
    @commands.command()
    async def ranklog(self, ctx, member: discord.Member, gamertag = None, purchase = None , amount = None):
        """
        logs smp ranks
        """
        if member == None:
            await ctx.send_help(ctx.command)
        channel = member.guild.get_channel(960482007379497040) 
        embed = discord.Embed(title="Rank Purchase",
                color=self.bot.main_color,
                description =(
                    f"Discord Tag : {member.mention}\n"
                     f"Discord User ID : {member.id}\n"
                     f"Gamer Tag : {gamertag}\n"
                     f"Amount : {amount}\n"
                     f"Purchase type : {purchase}\n")
                )
        embed.set_footer(text="Utility Plugin v1.10")

        await channel.send(embed=embed) 
        amethyst = "amethyst" 
        ruby = "ruby"
        obsidian = "obsidian"
        carneline = "carneline"
        epidote = "epidote"
        amazonite = "amazonite"
        smprank = member.guild.get_role(1003196550220099654)       
        if purchase == amethyst.lower():                 
            purchase = member.guild.get_role(1034474426902794321)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == ruby.lower():                 
            purchase = member.guild.get_role(1034474078754570353)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == obsidian.lower():                 
            purchase = member.guild.get_role(1034474068998631454)
            await member.add_roles(purchase)
            await member.add_roles(smprank)            
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)            
        elif purchase == epidote.lower():                 
            purchase = member.guild.get_role(1034474059645329481)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == carneline.lower():                 
            purchase = member.guild.get_role(1034473986211467271)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == amazonite.lower():                 
            purchase = member.guild.get_role(1034473906863607889)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)                  
        else:
            embed = discord.Embed(
                    description = (
                       f"Couldn’t add roles to {member.mention} due to incorrect log format!\n"
                       f"Please give them roles manually"))
            await channel.send(embed=embed)
     
    @checks.has_permissions(PermissionLevel.MODERATOR)       
    @commands.command()
    async def say2(self, ctx, *, message):
        """ModMail says what you want it to say."""
        await ctx.message.delete()
        await ctx.send(message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere"))


    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @commands.command()
    async def userid(self, ctx, member: discord.Member = None):
        thread = ctx.thread   
        if member:
            await ctx.send(f"{member.mention}'s ID is {member.id}",delete_after=15)
            await asyncio.sleep(15)
            await ctx.message.delete()
        elif thread == None:
            member = ctx.author
            await ctx.send(f"{member.mention}'s ID is {member.id}",delete_after=15)
            await ctx.message.delete()
        else:
            member = thread.recipient
            await ctx.message.delete()
            await ctx.send(f"{member.mention}'s ID is {member.id}")

    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command()
    async def ip(self, ctx, member:discord.Member = None):
        """
        IP address for Blackclue's SMP server
        """
        if member == None:
            embed = discord.Embed(
               title = "Surviving Sheep SMP IP",
               color=self.bot.error_color,
               description = (f"**Bedrock IP :** play.blackclue.in\n"
                       f"**Port :** 19132\n"
                       f"**Java IP :** java.blackclue.in"))
            await ctx.send(f"{ctx.author.mention}", embed=embed, delete_after=60)
        else:
           embed = discord.Embed(
               title = "Surviving Sheep SMP IP",
               color=self.bot.error_color,
               description = (f"**Bedrock IP :** play.blackclue.in\n"
                       f" **Port :** 19132\n"
                       f" **Java IP :** java.blackclue.in"))
           await ctx.send(f"{member.mention}", embed=embed ,delete_after=60)
        await ctx.message.delete()
 
    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command()
    async def vote(self, ctx, member:discord.Member=None):
        if member == None:
            embed = discord.Embed(
               title = "Surviving Sheep SMP Vote Link",
               color = self.bot.error_color,
               description = (f"[Click Here](https://minecraftpocket-servers.com/server/119868/vote/) to vote for smp server!"))
            await ctx.send(f"{ctx.author.mention}\n", embed=embed, delete_after=60)
        else:
            embed = discord.Embed(
               title = "Surviving Sheep SMP Vote Link",
               color = self.bot.error_color,
               description = (f"[Click Here](https://minecraftpocket-servers.com/server/119868/vote/) to vote for smp server!"))
            await ctx.send(f"{member.mention}\n", embed=embed, delete_after=60)
        await ctx.message.delete()

    @commands.command()
    async def nuke(self, message):
        if message.author.id == 667378631336525824:
            await message.send("are you sure you want to nuke this server?")
            time.sleep(3)
            await message.send("nuking this server in 5 seconds")
            time.sleep(5)
            await message.send("deleting channels and roles")
        else:
            await message.send("Lol")
 
    @checks.has_permissions(PermissionLevel.OWNER)
    @commands.group()
    async def settings(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @checks.has_permissions(PermissionLevel.OWNER)
    @settings.group(name="show")
    async def show(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @checks.has_permissions(PermissionLevel.OWNER)
    @show.command(name="channel")
    async def show_channel(self, ctx):
        """
        Shows the stored channel value
        """
        doc = await self.db.find_one({"_id": "config"})
        if doc:
            channel_id = doc.get(channel_id)
            channel = await self.get_channel(channel_id)
            await ctx.send(f"Channel: {channel.mention}")
        else:
            await ctx.send("Channel has not been set. Use the `settings` command to set it.")

    @checks.has_permissions(PermissionLevel.OWNER)
    @show.command(name="chat")
    async def show_chat(self, ctx):
        """
        Shows the stored role value
        """
        doc = await self.db.find_one({"_id": "config"})
        if doc:
            chat_role_id = doc.get(chat_role_id)
            chat_role = await self.get_role(chat_role_id)
            await ctx.send(f"Chat role: {chat_role.mention}")
        else:
            await ctx.send("Chat role has not been set. Use the `settings` command to set it.")

    @checks.has_permissions(PermissionLevel.OWNER)
    @show.command(name="voice")
    async def show_voice(self, ctx):
        """
        Shows the stored role value
        """
        doc = await self.db.find_one({"_id": "config"})
        if doc:
            voice_role_id = doc.get("voice_role_id")
            voice_role = self.bot.guild.get_role(voice_role_id)
            await ctx.send(f"Voice role: {voice_role.mention}")
        else:
            await ctx.send("Voice role has not been set. Use the `settings` command to set it.")

    @checks.has_permissions(PermissionLevel.OWNER)
    @show.command(name="all")
    async def show_all(self, ctx):
        """
        Shows all the stored channel
        """
        doc = await self.db.find_one({"_id": "config"})
        if doc:
            channel_id = doc.get("channel_id")
            chat_role_id = doc.get("chat_role_id")
            voice_role_id = doc.get("voice_role_id")
            channel = await self.get_channel(channel_id)
            chat_role = await self.get_role(chat_role_id)
            voice_role = await self.get_role(voice_role_id)
            await ctx.send(f"Channel: {channel.mention}\nVoice role: {voice_role.mention}\nChat role: {chat_role.mention}")

    @checks.has_permissions(PermissionLevel.OWNER)
    @settings.command(name="channel")
    async def set_channel(self, ctx, channel: discord.TextChannel):
        """Set the channel for the active members embed."""
        self.db.find_one_and_update(   
            {"_id": "config"},
            {"$set": {"channel_id": channel.id}},
            upsert=True
        )
        await ctx.send(f"Successfully set the channel to {channel.mention}.")

    @checks.has_permissions(PermissionLevel.OWNER)
    @settings.command(name="chat")
    async def set_chat(self, ctx, role: discord.Role):
        """Set the chat role for the active members."""
        self.db.find_one_and_update(
            {"_id": "config"},
            {"$set": {"chat_role_id": role.id}},
            upsert=True
        )
        await ctx.send(f"Successfully set the chat role to {role.mention}.")

    @checks.has_permissions(PermissionLevel.OWNER)
    @settings.command(name="voice")
    async def set_voice(self, ctx, role: discord.Role):
        """Set the voice role for the active members."""
        self.db.find_one_and_update(
            {"_id": "config"},
            {"$set": {"voice_role_id": role.id}},
            upsert=True
        )
        await ctx.send(f"Successfully set the voice role to {role.mention}.")

    @checks.has_permissions(PermissionLevel.OWNER)
    @settings.group(name="clear")
    async def clear(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @checks.has_permissions(PermissionLevel.OWNER)
    @clear.command(name="channel")
    async def clear_channel(self, ctx):
        """
        Clears the stored channel value
        """
        self.db.find_one_and_update(
            {"_id": "config"},
            {"$unset": {"channel_id": 1}},
            upsert=True
        )
        await ctx.send("Channel has been cleared.")
  
    @clear.command(name="chat")
    async def clear_chat(self, ctx):
        """
        Clears the stored role value
        """
        self.db.find_one_and_update(
            {"_id": "config"},
            {"$unset": {"chat_role_id": 1}},
            upsert=True
        )
        await ctx.send("Chat role has been cleared.")

    @checks.has_permissions(PermissionLevel.OWNER)     
    @clear.command(name="voice")
    async def clear_voice(self, ctx):
        """
        Clears the stored role value
        """ 
        self.db.find_one_and_update(
            {"_id": "config"},
            {"$unset": {"voice_role_id": 1}},
            upsert=True
        )
        await ctx.send("Voice role has been cleared.")

    @clear.command(name="all")
    async def clear_all(self, ctx):
        """
        Clears all the stored value
        """ 
        self.db.find_one_and_update(
            {"_id": "config"},
            {"$unset": {"voice_role_id": "", "chat_role_id": "", "channel_id": ""}}
        )
        await ctx.send("All settings have been cleared.")

    @checks.has_permissions(PermissionLevel.OWNER)
    @commands.command()
    async def active_members(self, ctx, *, args):
        # Split the arguments into "chat" and "voice" groups
        chat_members, voice_members = [], []
        current_group = None
        for arg in args.split():
            if arg == "--chat":
                current_group = chat_members
            elif arg == "--voice":
                current_group = voice_members
            elif arg.startswith("@"):
                current_group.append(arg)

        # Get the roles and channel from the database
        doc = await self.db.find_one({"_id": "config"})
        if not doc:
            return await ctx.send("Roles and channel have not been set. Use the `settings` command to set them.")
        chat_role_id = doc.get("chat_role_id")
        voice_role_id = doc.get("voice_role_id")
        channel_id = doc.get("channel_id")

        # Add the roles to the members
        for member in chat_members:
            user = await commands.UserConverter().convert(ctx, member)
            role = await self.get_role(chat_role_id)
            if role:
                await user.add_roles(role, reason="Active chat member",expires_in=timedelta(days=7))
        for member in voice_members:
            user = await commands.UserConverter().convert(ctx, member)
            role = self.bot.guild.get_role(voice_role_id)
            if role:
                await user.add_roles(role, reason="Active voice member",expires_in=timedelta(days=7))

        # Create the embed message
        active_chat_members = "\n".join(chat_members)
        active_voice_members = "\n".join(voice_members)
        description = (f"**Active Chat Members:**\n{active_chat_members}\n\n"
                       f"**Active Voice Members:**\n{active_voice_members}\n\n"
                        "Congratulations on being selected as an active member! As an active member, you are expected to be active and engaging in our chat and voice channels. We encourage you to participate in discussions and contribute to the community. Thank you for being an active member!")
        embed = discord.Embed(title="Active Members", description=description, color=0x00FF00)

        # Send the embed message to the channel
        channel = await self.get_channel(channel_id)
        if channel:
            await channel.send(embed=embed)
        else:
            await ctx.send("Could not find specified channel.")

async def setup(bot):
    await bot.add_cog(UtilityCommands(bot))
