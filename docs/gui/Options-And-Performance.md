---
title: "Options and Performance"
parent: Graphical Interface
nav_order: 4
---
{% raw %}
# Options and Performance

Several interface options are accessible from **Tools => Options**. This page groups them by what each one controls, starting with the ones that make models run faster, and then covers how model files are located and loaded.

## Increasing Performance

- Select "Tools => Options \| Advanced \| Automatically detect the number of processors available". When running models from the command line, set the `-processor` option of each model to 0.
- Set the memory management option under "Tools => Options \| Advanced" to "Balanced" or "Aggressive". On the command line, use the option `-memory-allocation-policy` with the value 1 or 4, respectively.
- Install the Enhancement Plugin for Dinamica EGO and clear "Tools => Options \| Advanced \| Disable compilation of native expressions".
- Set "Tools => Options \| System \| Message log level" to Result. This helps most in models with many loop containers such as [Repeat](../functors/Repeat.html), [While](../functors/While.html), and [For](../functors/For.html).
- Avoid maps with the [cell type](../types/Cell-Type.html) "1 Bit Integer". It saves memory, but has a large negative impact on performance.
- Keep Dinamica EGO updated.

Each of these settings is described below.

## Number of Workers

The GUI option "Tools => Options \| Advanced \| Automatically detect the number of processors available" controls how many workers Dinamica EGO uses to execute a model in parallel. Here, "processors" refers to the number of CPU cores (or logical processors) available on the machine. If you are running your models using the command line, the equivalent is the "-processors" option, set to 0 for automatic detection (uses the total number of processor cores).

Automatic detection sizes the number of workers to the number of processors available. However, oversubscribing this number — i.e., using more workers than you have processors — can be beneficial when the task being executed is heavily I/O-bound, since workers spend part of their time waiting on I/O rather than using the CPU, and extra workers can keep the CPU busy during those waits.

## Memory Management

The memory management option "Tools => Options \| Advanced" controls how Dinamica EGO handles input and resulting maps in memory versus on disk. If you are using the command line tool, the equivalent is the "-memory-allocation-policy" option.

Five policies are available:

- **Prefer Memory** — keeps input and resulting maps in memory whenever possible. If there isn't enough free memory, maps are stored on disk and brought back piece by piece. Execution might fail if there isn't enough free memory left for other operations.
- **Balanced** — keeps input maps on disk and tries to keep resulting maps in memory whenever possible, storing them on disk instead if memory is limited or if doing so could constrain memory available for other operations. *(-memory-allocation-policy 1)*
- **Prefer Disk** — keeps all maps, including resulting ones, on disk, loading them into memory piece by piece as needed.
- **Memory Only** — keeps input and resulting maps entirely in memory. If there isn't enough free memory, an error is reported and execution is aborted.
- **Aggressive** — keeps resulting maps in memory whenever possible, falling back to disk (and reloading piece by piece) only when memory is insufficient. *(-memory-allocation-policy 4)*

**Aggressive** is the preferred setting for maximizing performance, since it favors keeping resulting maps in memory. **Balanced** is a more conservative, safer choice — it keeps input maps on disk and is more cautious about keeping resulting maps in memory, reducing the risk of running low on memory for other operations at some cost to performance.

## Native Expression Compilation

Make sure the "Enhancement Plugin for Dinamica EGO" extension is installed and the GUI option "Tools => Options \| Advanced \| Disable compilation of native expressions" is unchecked. This allows expressions to be compiled to native code, which improves performance.

## Virtualization

The "Tools => Options \| Advanced \| Virtualization" option controls how Dinamica EGO handles maps with different extents, resolutions, or numbers of lines and columns (also known as raster map virtualization). See [Image Virtualization](../Image-Virtualization.html) for the full explanation of what virtualization does and what each of the available options (Not Allowed, Unrestricted, Limited) means.

## Message Log Level

The GUI option "Tools => Options \| System \| Message log level" controls the amount of messages generated during model execution — it is not a performance setting. Setting it to Result reduces the volume of messages shown. *This helps when running models with lots of loop containers like [Repeat](../functors/Repeat.html), [While](../functors/While.html), [For](../functors/For.html) etc, which would otherwise generate a large number of messages*.

When the log level is set to Debug or above, it is also possible to define which specific debugging actions (called **log subsystems**) should be logged.

## Model Backups

The checkbox "Create backup copy of the current model script upon saving", under "Tools => Options \| General \| Model Backup", makes Dinamica EGO copy the content of a model script file every time it is about to be overwritten by a "Save" or "Save As" — this protects against accidental loss of a previous version of the model.

The "Backup Folder" field controls where these copies are placed. If left empty, copies are placed in the same folder as the original model. To restore a model to a previous state, copy the corresponding file back from the backup folder to its original location.

## EGO Script Formatting

The settings under "Options \| EGO Script" control how a model selection is formatted when it is copied and pasted as EGO Script into an external text editor. See [Copying and Pasting](Interface-Elements.html#copying-and-pasting) for the copy/paste mechanism itself.

## File Paths

The interface shows absolute file paths for readability, but the paths are stored as relative paths. To move a model without breaking its file references, keep the same relative location between the script file ([EGO Script](../EGO-Script.html) or [EGOML](../EGOML-Script.html)) and the data directory.

Alternatively, use the [Workdir](../functors/Workdir.html) functor: every Load and Save functor inside it is relative to the directory set in the Workdir. A model can contain several Workdir containers. For an example, see the folder `Examples\run_lucc_northern_mato_grosso\run_roads_with_comments_and_workdirs` in the Dinamica EGO examples.

## Loading Files from Zip Files

Maps, tables, lookup tables, and Weights of Evidence files can be loaded from [zip](https://en.wikipedia.org/wiki/ZIP_(file_format)) files.

- A zip file packs all the files of a model in a single archive. It does not increase the amount of data Dinamica EGO can handle at once: Dinamica unzips the files into a temporary folder and loads them from there.
- Zip files are limited to 4 GB. Files kept outside the archive can be larger.
- To read a file inside a zip file, use a [Workdir](../functors/Workdir.html) container. Set its `folder` input port to the zip file name, and place a loader such as [Load Map](../functors/Load-Map.html) or [Load Weights](../functors/Load-Weights.html) inside it. The file name in the loader must match the name of the file in the archive.
{% endraw %}
