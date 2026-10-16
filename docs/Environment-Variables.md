---
title: "Environment Variables"
nav_order: 3
parent: "Getting Started"
---
{% raw %}
# Environment Variables

Some Dinamica EGO settings can be defined through environment variables. Every variable name starts with `DINAMICA_EGO_X_`, where `X` is Dinamica EGO's major version number. For example, the temporary folder of Dinamica EGO 8 is set with `DINAMICA_EGO_8_TEMP_DIR`.

## How Settings Are Looked Up

Each setting is read from the first of these places where it is defined:

1. **Environment variable** of the Dinamica EGO process.
1. **User configuration**, where the values chosen in *Tools => Options* are saved. On Windows, this is the Windows registry (`HKEY_CURRENT_USER`); on Linux, the file `~/.dinamica_ego_X.conf`.
1. **System configuration**. On Windows, this is the Windows registry (`HKEY_LOCAL_MACHINE`); on Linux, the file `/etc/dinamica_ego_X.conf`.

An environment variable therefore takes precedence over the value chosen in *Tools => Options*.

## Variables

In the table, `X` stands for the major version number.

| Variable | Description |
| --- | --- |
| `DINAMICA_EGO_X_TEMP_DIR` | Folder where temporary maps and compiled libraries are stored. When not defined, the system's temporary folder is used (on Linux, the folder in `TMPDIR`, or `/tmp`). Equivalent to the *Use alternative folder for storing temporary files* option. |
| `DINAMICA_EGO_X_MEMORY_ALLOCATION_POLICY` | Memory allocation policy, as a number: `0` Prefer Memory, `1` Balanced, `2` Prefer Disk, `3` Memory Only, `4` Aggressive. When not defined or not a valid number, Balanced is used. See [Memory Management](gui/Options-And-Performance.html#memory-management) for what each policy does. |
| `DINAMICA_EGO_X_MAX_DETECTED_CORES` | Upper limit for the number of processor cores Dinamica EGO detects, and therefore for the number of workers chosen automatically. Only positive values take effect. |
| `DINAMICA_EGO_X_ALTERNATIVE_PATH_FOR_R` | Path to the `Rscript` executable of a local R installation, used by [Calculate R Expression](functors/Calculate-R-Expression.html). When not defined on Linux, `/usr/bin/Rscript` is used if it exists. |
| `DINAMICA_EGO_X_R_CRAN_MIRROR` | URL of the CRAN mirror used to install R packages. When not defined, `http://cran.us.r-project.org` is used. |
| `DINAMICA_EGO_X_GDAL_DATA` | Folder with the GDAL data files (such as projection definitions) used when reading and writing maps. When not defined, the `Data/GDAL` folder of the Dinamica EGO installation is used. |
| `DINAMICA_EGO_X_GDAL_TOOLS` | Folder containing the GDAL utilities `gdal_rasterize`, `gdal_translate`, and `gdalwarp`, run by [Transform Map](functors/Transform-Map.html) and [Rasterize Shape](functors/Rasterize-Shape.html). When not defined, the Dinamica EGO installation folder is used. |
| `DINAMICA_EGO_X_GDAL_TOOLS_DATA` | Data folder handed to the GDAL utilities above (as their `GDAL_DATA` and `PROJ_LIB`). When not defined, the `Data/GDAL` folder of the Dinamica EGO installation is used. |
| `DINAMICA_EGO_X_CL_CONFIG` | Use of accelerator (OpenCL) devices: `0` none, `1` detected automatically, `2` only the devices listed in `DINAMICA_EGO_X_CL_DEVICES`. The [Dinamica Console](Dinamica-Console.html) option `-accelerators-policy` sets the same choice for a single run. |
| `DINAMICA_EGO_X_CL_DEVICES` | Devices used when `DINAMICA_EGO_X_CL_CONFIG` is `2`, separated by semicolons (`;`). Each name must match one printed by `DinamicaConsole -list-accelerators` (letter case is ignored); devices not present on the machine are skipped. |
| `DINAMICA_EGO_X_LOG_PATH` | Folder where the log files are written. When not defined, the user's Dinamica EGO folder is used (`Documents\Dinamica EGO X` on Windows, `~/Dinamica EGO X` on Linux). On Windows, Dinamica Console writes its log files to the current folder instead; on Linux, it also uses this folder. |

## Development and Support Variables

These variables are meant for development builds and for troubleshooting. Regular installations do not need them.

| Variable | Description |
| --- | --- |
| `DINAMICA_EGO_X_INSTALLATION_DIRECTORY` | Folder where Dinamica EGO is installed, used to locate its own files (libraries, plugins, and the `Data` folder). It must be defined for Dinamica EGO to start on Windows and Linux; change it only to run Dinamica EGO from another folder, such as a development build. On Windows, the portable Dinamica Console defines it for its own process when it is missing. |
| `DINAMICA_EGO_X_PDB_PATH` | Windows only. Folder with the debug symbol (`.pdb`) files used to print stack traces when Dinamica EGO crashes. When not defined, the installation folder is used. |
| `DINAMICA_EGO_X_MAC_DEV_PATH` | macOS only. Folder with the Dinamica EGO binaries, used instead of the folder of the running executable. Intended for development builds. |

## Defining an Environment Variable

- **Windows:** open *Edit the system environment variables* from the Start menu, click *Environment Variables*, and click *New* under *User variables* (only for your user) or *System variables* (for every user). Type the variable name and its value.
- **Linux:** add a line such as `export DINAMICA_EGO_8_TEMP_DIR=/path/to/folder` to your shell startup file (for example, `~/.profile`), then log out and back in.

Restart Dinamica EGO after defining or changing a variable, so it reads the new value.
{% endraw %}
