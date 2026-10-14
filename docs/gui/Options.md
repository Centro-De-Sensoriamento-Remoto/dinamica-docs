---
title: "Options (Tools => Options)"
parent: Graphical Interface
nav_order: 1
---
{% raw %}
# Options (Tools => Options)

Several interface options are accessible from **Tools => Options**. They are grouped below by what each one actually controls.

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

The GUI option "Tools => Options \| System \| Message log level" controls the amount of messages generated during model execution — it is not a performance setting. Setting it to Result reduces the volume of messages shown. *This helps when running models with lots of loop containers like [Repeat](../Repeat.html), [While](../While.html), [For](../For.html) etc, which would otherwise generate a large number of messages*.

When the log level is set to Debug or above, it is also possible to define which specific debugging actions (called **log subsystems**) should be logged.

## Model Backups

The checkbox "Create backup copy of the current model script upon saving", under "Tools => Options \| General \| Model Backup", makes Dinamica EGO copy the content of a model script file every time it is about to be overwritten by a "Save" or "Save As" — this protects against accidental loss of a previous version of the model.

The "Backup Folder" field controls where these copies are placed. If left empty, copies are placed in the same folder as the original model. To restore a model to a previous state, copy the corresponding file back from the backup folder to its original location.

## EGO Script Formatting

The settings under "Options \| EGO Script" control how a model selection is formatted when it is copied and pasted as EGO Script into an external text editor. See [Sketch](Library-And-Sketch.html#sketch) for the copy/paste mechanism itself.
{% endraw %}
