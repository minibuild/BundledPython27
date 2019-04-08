#pragma build output-wsl='output/wsl'

#pragma os:windows nasm executable='C:\NASM\nasm.exe'

#pragma os:windows toolset required=1 module=mingw    arch=x86_64        alias=sys:native package='H:\mingw-w64\x86_64-5.4.0-win32-seh-rt_v5-rev0\mingw64'
#pragma os:linux   toolset required=1 module=gcc                         alias=sys:native
#pragma os:macosx  toolset required=1 module=clang    arch=x86_64:10.9   alias=sys:native
