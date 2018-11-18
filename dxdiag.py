import os, sys
import xml.etree.ElementTree as xml
from halo import Halo
from colorama import init, Fore, Back, Style
from utils.styles import TextStyles
CustomStyles = TextStyles("--nocolor" in sys.argv)
init(autoreset=True)

if not "--noloader" in sys.argv:
    loader = Halo(spinner = {"interval": 150, "frames": ["|", "/", "-", "\\"]})
if (not os.name == "nt") and (not "--force-os" in sys.argv):
    print(Fore.RED + "dxdiag.py requires Windows to work properly. To force-run the program, add the --force-os flag. (expected 'nt', got '{}')".format(os.name))
    exit(1)

def loaddxdiag():
    global sysinfo
    if not "--noloader" in sys.argv:
        loader.start("Fetching dxdiag information...")
    os.system("dxdiag /x dxdiag.xml")
    root = xml.parse('dxdiag.xml').getroot()
    if not "--noloader" in sys.argv:
        loader.stop()
    sysinfo = root.find('SystemInformation')
    display = root.find('DisplayDevices').find('DisplayDevice')
    return (sysinfo, display)

def sysinfocall(sysinfo):
    print(CustomStyles.TITLE + "System Information")
    print(CustomStyles.SETTING + "Computer name:         " + Style.RESET_ALL + sysinfo.find('MachineName').text)
    print(CustomStyles.SETTING + "Operating system:      " + Style.RESET_ALL + sysinfo.find('OperatingSystem').text)
    print(CustomStyles.SETTING + "System model:          " + Style.RESET_ALL + sysinfo.find('SystemManufacturer').text + " " + sysinfo.find('SystemModel').text)
    print(CustomStyles.SETTING + "CPU:                   " + Style.RESET_ALL + sysinfo.find('Processor').text)
    print(CustomStyles.SETTING + "Memory:                " + Style.RESET_ALL + sysinfo.find('Memory').text + " ({} available)".format(sysinfo.find('AvaliableOSMem').text))
    print(CustomStyles.SETTING + "Page file:             " + Style.RESET_ALL + sysinfo.find('PageFile').text)

def displaycall(display):
    print(CustomStyles.TITLE + "Display")
    print(CustomStyles.SETTING + "Graphics card:         " + Style.RESET_ALL + display.find('ChipType').text)
    print(CustomStyles.SETTING + "Manufacturer:          " + Style.RESET_ALL + display.find('Manufacturer').text)
    print(CustomStyles.SETTING + "Device type:           " + Style.RESET_ALL + display.find('DeviceType').text)
    print(CustomStyles.SETTING + "Display memory (VRAM): " + Style.RESET_ALL + display.find('DisplayMemory').text)
    print(CustomStyles.SETTING + "Shared memory:         " + Style.RESET_ALL + display.find('SharedMemory').text)

def directxcall(sysinfo, display):
    print(CustomStyles.TITLE + "DirectX")
    print(CustomStyles.SETTING + "Version:               " + Style.RESET_ALL + sysinfo.find('DirectXVersion').text)
    print(CustomStyles.SETTING + "DirectX Draw:          " + Style.RESET_ALL + display.find('DDrawStatus').text)
    print(CustomStyles.SETTING + "Dirext3D:              " + Style.RESET_ALL + display.find('D3DStatus').text)
    print(CustomStyles.SETTING + "AGP Texture:           " + Style.RESET_ALL + display.find('AGPStatus').text)

def help():
    print(CustomStyles.TITLE + "dxdiag.py help")
    print(CustomStyles.SETTING + "--help     : " + Style.RESET_ALL + "Shows help for dxdiag.py")
    print(CustomStyles.SETTING + "--version  : " + Style.RESET_ALL + "Shows version info for dxdiag.py")
    print(CustomStyles.SETTING + "--sysinfo  : " + Style.RESET_ALL + "Only show the system information section of diagnostics")
    print(CustomStyles.SETTING + "--display  : " + Style.RESET_ALL + "Only show the display section of diagnostics")
    print(CustomStyles.SETTING + "--directx  : " + Style.RESET_ALL + "Only show the DirectX section of diagnostics")
    print(CustomStyles.SETTING + "--nocolor  : " + Style.RESET_ALL + "Do not use color when displaying diagnostic info")
    print(CustomStyles.SETTING + "--noloader : " + Style.RESET_ALL + "Do not show the loading symbol when displaying diagnostic info")
    print(CustomStyles.SETTING + "--specs    : " + Style.RESET_ALL + "Display simple computer specs (such as CPU, Memory, etc.)")
    print(CustomStyles.SETTING + "--nologo   : " + Style.RESET_ALL + "Do not show the Windows 10 logo when printing stats for --specs")

if "--help" in sys.argv:
    help()
    sys.exit(0)
if "--version" in sys.argv:
    print("dxdiag.py version: 1.0.0")
    sys.exit(0)
if any(x in sys.argv for x in ['--sysinfo', '--display', '--directx']):
    sysinfo, display = loaddxdiag()
    if "--sysinfo" in sys.argv:
        sysinfocall(sysinfo)
    if "--display" in sys.argv:
        displaycall(display)
    if "--directx" in sys.argv:
        directxcall(sysinfo, display)
    exit(0)
if "--specs" in sys.argv:
    sysinfo, display = loaddxdiag()
    lines = []
    lines.append(CustomStyles.TITLE + sysinfo.find('SystemManufacturer').text + " " + sysinfo.find('SystemModel').text)
    lines.append("")
    lines.append(CustomStyles.SETTING + "Windows version: " + Style.RESET_ALL + sysinfo.find('OperatingSystem').text.split("(")[0] + "- " + sysinfo.find('OperatingSystem').text.split(")")[0].split(", ")[1])
    lines.append(CustomStyles.SETTING + "Processor:       " + Style.RESET_ALL + sysinfo.find('Processor').text.split(",")[0])
    lines.append(CustomStyles.SETTING + "Memory:          " + Style.RESET_ALL + sysinfo.find('AvaliableOSMem').text)
    lines.append(CustomStyles.SETTING + "Graphics card:   " + Style.RESET_ALL + display.find('CardName').text + " - " + display.find('SharedMemory').text + " VRAM")
    if "--nologo" in sys.argv:
        for line in lines:
            print(line)
        exit(0)
    with open("win_logo.txt", 'r') as f:
        index = 0
        for line in f.read().split("\n"):
            try:
                print(CustomStyles.SETTING + Style.DIM + line + Style.RESET_ALL + " " + lines[index])
            except:
                print(CustomStyles.SETTING + Style.DIM + line)
            index += 1
    exit(0)

sysinfo, display = loaddxdiag()
sysinfocall(sysinfo)
displaycall(display)
directxcall(sysinfo, display)
