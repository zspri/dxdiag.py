# dxdiag.py

A Python script for getting information from Windows' dxdiag

## Requirements
 - Python 3
 - `halo` and `colorama` from pip
 - A Windows system

## Installation
```sh
git clone https://github.com/devakira/dxdiag.py.git
cd dxdiag.py
pip install -r requirements.txt
```

## Usage

```
--help     : Shows help for dxdiag.py
--version  : Shows version info for dxdiag.py
--sysinfo  : Only show the system information section of diagnostics
--display  : Only show the display section of diagnostics
--directx  : Only show the DirectX section of diagnostics
--nocolor  : Do not use color when displaying diagnostic info
--noloader : Do not show the loading symbol when displaying diagnostic info
--specs    : Display simple computer specs (such as CPU, Memory, etc.)
--nologo   : Do not show the Windows 10 logo when printing stats for --specs
```

## Examples

```sh
PS ~\dxdiag.py> py dxdiag.py
```
```
System Information
Computer name:         DESKTOP-31NJDVL
Operating system:      Windows 10 Home 64-bit (10.0, Build 17758) (17758.rs5_release.180907-1536)
System model:          Dell Inc. Inspiron 5680
CPU:                   Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz (12 CPUs), ~3.2GHz
Memory:                16384MB RAM (16270MB RAM available)
Page file:             11259MB used, 11310MB available
Display
Graphics card:         GeForce GTX 1070
Manufacturer:          NVIDIA
Device type:           Full Device (POST)
Display memory (VRAM): 16223 MB
Shared memory:         8135 MB
DirectX
Version:               DirectX 12
DirectX Draw:          Enabled
Dirext3D:              Enabled
AGP Texture:           Enabled
```
