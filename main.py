# discord embeed background color - #2f3136
# server image link - https://cdn.icon-icons.com/icons2/1852/PNG/512/iconfinder-valueserver-4417114_116617.png
import discord, os, psutil, platform
from datetime import datetime

os.systme('sudo mount -o remount,rw /')
os.system('apt update')
os.system('apt-get install net-tools')

client = discord.Client()
image_url = 'https://cdn.icon-icons.com/icons2/1852/PNG/512/iconfinder-valueserver-4417114_116617.png'
now = datetime.now()

def message_log(msg):
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"{date} --- {msg}")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):

    def get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor
        return get_size


    if message.author == client.user:
        return


    # help
    if message.content.startswith('/help'):
        embedVar = discord.Embed(title=f"Commands: \n", description="**`/stats` - system stats\n`/system` - system information\n`/cpu` - cpu information\n`/ram` - ram information\n`/drives` - drive information\n`/lan` - local network information \n`/wifi` - wifi information\n`/run [your command]` - run a custom command\n `/tasks` - see all running proceesses \n`/kill [process id]` -  kill a process by it's id \n`/killall [process name]` - kill a prcocess by it's name \n`/ports` - check network ports \n`/auth.log` -  authentication logs\n`/secure` -  authentication logs\n`/kern.log` -   kernel logs\n`/boot.log` - boot records**", color=0x0066ff)
        embedVar.set_thumbnail(url=image_url)
        await message.channel.send(embed=embedVar)
        msg = message.content
        message_log(msg)


    # server statistics
    if message.content.startswith('/stats'):
        bt =  datetime.fromtimestamp(psutil.boot_time())
        disk_io = psutil.disk_io_counters()
        embedVar = discord.Embed(title=f"Server stats", description=f"**Cpu usage:  `{psutil.cpu_percent()}%` \nRam usage:  `{psutil.virtual_memory().percent}%` \nBoot time:  `{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}` \nDisk reads: `{get_size(disk_io.read_bytes)}` \nDisk writes: `{get_size(disk_io.write_bytes)}`**", color=0x0066ff)
        embedVar.set_thumbnail(url=image_url)
        await message.channel.send(embed=embedVar)
        msg = message.content
        message_log(msg)


    # system info
    if message.content.startswith('/system'):
        uname = platform.uname()
        embedVar = discord.Embed(title=f"System information" ,description=f"**System: `{uname.system}` \nNode name: `{uname.node}` \nRelease: `{uname.release}` \nVersion: `{uname.version}` \nMachine: `{uname.machine}` \nProcessor: `{uname.processor}`**", color=0x0066ff)
        embedVar.set_thumbnail(url=image_url)
        await message.channel.send(embed=embedVar)
        msg = message.content
        message_log(msg)


    # cpu details
    if message.content.startswith('/cpu'):
        cpufreq = psutil.cpu_freq()
        embedVar = discord.Embed(title=f"CPU info" ,description=f"**Physical cores: `{psutil.cpu_count(logical=False)}` \nLogical cores: `{psutil.cpu_count(logical=True)}` \nMax frequency: `{cpufreq.max:.2f}Mhz` \nMin frequency: `{cpufreq.min:.2f}Mhz` \nCurrent frequency: `{cpufreq.current:.2f}Mhz` \nTotal CPU usage: `{psutil.cpu_percent()}%` \n`/ports` - check network ports**", color=0x0066ff)
        embedVar.set_thumbnail(url=image_url)
        await message.channel.send(embed=embedVar)
        msg = message.content
        message_log(msg)

    # ram details
    if message.content.startswith('/ram'):
        ram  = psutil.virtual_memory()
        embedVar = discord.Embed(title=f"RAM info" ,description=f"**Total: `{get_size(ram.total)}` \nAvailable: `{get_size(ram.available)}` \nUsed: `{get_size(ram.used)}` \nPercentage: `{ram.percent}%`**", color=0x0066ff)
        embedVar.set_thumbnail(url=image_url)
        await message.channel.send(embed=embedVar)
        msg = message.content
        message_log(msg)

    # drive details
    if message.content.startswith('/drives'):
        os.system('df -h > drives.txt')
        files = 'drives.txt'
        await message.channel.send(file=discord.File(files))
        os.remove(files)
        msg = message.content
        message_log(msg)

    # lan info
    if message.content.startswith('/lan'):
        os.system('ifconfig > lan.txt')
        files = 'lan.txt'
        await message.channel.send(file=discord.File(files))
        os.remove(files)
        msg = message.content
        message_log(msg)

    # wifi info
    if message.content.startswith('/wifi'):
        os.system('iwconfig > wifi.txt')
        files = 'wifi.txt'
        await message.channel.send(file=discord.File(files))
        os.remove(files)
        msg = message.content
        message_log(msg)
        
    # running a custom command to the server
    if message.content.startswith('/run'):
        msg = message.content
        command = msg.split()
        command = command[1]
        command = f'{command} > output.txt'
        os.system(command)
        files = 'output.txt'
        await message.channel.send(file=discord.File(files))
        os.remove(files)
        msg = message.content
        message_log(msg)
    
    # search for specific procces by name
    if message.content.startswith('/tasks'):
        msg = message.content
        command = msg.split()
        if len(command) > 1:
            command = command[1]
            command = f'ps aux | grep {command} > output.txt'
            os.system(command)
            files = 'output.txt'
            await message.channel.send(file=discord.File(files))
            os.remove(files)
            msg = message.content
            message_log(msg)
        else:
            os.system('ps aux > output.txt')
            files = 'output.txt'
            await message.channel.send(file=discord.File(files))
            os.remove(files)
            msg = message.content
            message_log(msg)


    # kill a process by it's process id
    if message.content.startswith('/kill'):
        msg = message.content
        process_id = msg.split()
        process_id = process_id[1]
        process_id = f'kill {process_id}'
        await message.channel.send(file=discord.File(files))
        os.remove(files)
        msg = message.content
        message_log(msg)

    # killall - kill a process by it's name
    if message.content.startswith('/killall'):
        msg = message.content
        process_name = msg.split()
        process_name = process_name[1]
        process_name = f'kill {process_name}'
        await message.channel.send(file=discord.File(files))
        os.remove(files)
        msg = message.content
        message_log(msg)

    # check network ports
    if message.content.startswith('/ports'):
        os.system('ss > ports.txt')
        files = 'ports.txt'
        await message.channel.send(file=discord.File(files))
        os.remove(files)
        msg = message.content
        message_log(msg) 

    # authentication logs
    if message.content.startswith('/auth.log'):
        os.system('cat /var/log/auth.log > output.txt')
        files = 'output.txt'
        await message.channel.send(file=discord.File(files))
        os.remove(files)
        msg = message.content
        message_log(msg)

    # authentication file
    if message.content.startswith('/secure'):
        os.system('cat /var/log/secure > output.txt')
        files = 'output.txt'
        await message.channel.send(file=discord.File(files))
        os.remove(files)
        msg = message.content
        message_log(msg)

    # check the kernel logs
    if message.content.startswith('/kern.log'):
        os.system('cat /var/log/kern.log > output.txt')
        files = 'output.txt'
        await message.channel.send(file=discord.File(files))
        os.remove(files)
        msg = message.content
        message_log(msg)

    # boot records
    if message.content.startswith('/boot.log'):
        os.system('cat /var/log/boot.log > output.txt')
        files = 'output.txt'
        await message.channel.send(file=discord.File(files))
        os.remove(files)
        msg = message.content
        message_log(msg)
    

client.run(os.environ['DISCORD_TOKEN'])
