---
title: "Dinamica Console"
nav_order: 2
parent: "Getting Started"
---
{% raw %}
# Dinamica Console

Dinamica Console is the command-line interface for running Dinamica EGO model scripts without opening the graphical interface. It is well suited for batch processing, scheduled runs, and execution on machines without a display.

## Syntax

```
DinamicaConsole {OPTIONS} <model script filename>
```

The `<model script filename>` argument is required and specifies the model script that will be executed. The special argument `--` can be used to terminate flag options, forcing all following arguments to be treated as positional arguments.

## Execution Options

- `-predefined-seed` — Use a predefined value as the seed of the random number generators, instead of a value derived from the current time. Useful for producing reproducible runs.
- `-granularity=[granularity]` — Override the default granularity multiplier value used to break jobs into parallel tasks.
- `-propagate-exceptions` — Propagate top-level exceptions instead of only reporting them and exiting.
- `-disable-submodel-expansions` — Disable submodel expansions before running the script. See [Submodel Expansion and Execution](Submodels.html#submodel-expansion-and-execution) for details on what expansion does.
- `-disable-copy-optimization` — Disable data copy optimization during script execution. *Only use this setting if you know what you are doing*.
- `-remove-redundant-carriers` — Remove all unnecessary intermediate carrier functors before executing a model. See [Submodel Expansion and Execution](Submodels.html#submodel-expansion-and-execution) for details.
- `-dont-run` — Parse and validate the model script, but do not execute it. Useful together with `-output` to only convert a script.

## Workers and Memory

- `-processors=[processors]` — Override the number of logical processors (workers) that should be used. Pass 0 to automatically use the total number of processor cores instead.
- `-disable-parallel-functors` — Disable parallel processing of independent functors.
- `-disable-parallel-steps` — Disable parallel processing of independent loop steps.
- `-disable-parallel-map-load` — Disable loading maps in parallel.
- `-memory-allocation-policy=[memory-allocation-policy]` — Policy used to control memory allocation. Values: `PREFER_MEMORY=0`, `BALANCED=1`, `PREFER_DISK=2`, `MEMORY_ONLY=3`, `AGGRESSIVE=4`. See Memory Management for what each policy does; `BALANCED` and `AGGRESSIVE` are generally recommended for performance, with `AGGRESSIVE` being the more performance-oriented and `BALANCED` the more conservative choice.
- `-disable-native-expressions` — Disable compilation of image expressions to native code. Expressions are evaluated using the default interpretation facility instead.

## Accelerators

- `-accelerators-policy=[accelerators-policy]` — Policy used to select accelerator (OpenCL) devices. Values: `NO_DEVICES=0`, `ALL_DEVICES=1`, `USER_CONFIG=2`.
- `-list-accelerators` — Show the available accelerator devices and exit, without running the script.

## Logging

- `-log-level=[log-level]` — Set the execution log level. Values: `UNCONDITIONAL=0`, `ERROR=1`, `WARNING=2`, `RESULT=3`, `INFO=4`, `INFO2=5`, `DEBUG=6`, `DEBUG2=7`. Note that this controls the volume of messages generated, not performance.
- `-log-subsystem=[log-subsystem]` — Set the execution log subsystem flags, restricting debugging information to specific subsystems. Only takes effect when `-log-level` is set to `DEBUG` or `DEBUG2`. Values are bit flags that can be combined by summing them: `GENERAL=1`, `OPENCL=2`, `SCRIPT_READER_WRITER=4`, `FUNCTOR_SCHEDULER=8`, `FUNCTOR_DEPENDENCE_GRAPH=16`, `FUNCTOR_EXECUTION=32`, `FILESYSTEM=64`, `MAP_IO_HANDLER=128`, `FUNCTOR_COPY_ANALYSIS=256`, `SUBMODEL=512`, `EXECUTION_BASICS=1024`, `GRAPHICAL_INTERFACE=2048`, `DATABASE=4096`, `TABLE_IO_HANDLER=8192`, `MAP_HANDLING=16384`, `TABLE_HANDLING=32768`, `SYSTEM_COMMUNICATION=65536`.
- `-beep` — Beep to indicate that the execution has completed.

During execution, the console only displays messages at the `INFO2` level and below, regardless of the configured `-log-level`. Each worker also writes its own log file, named `log_X.txt` (where `X` is the worker number), which mirrors what the console shows: only messages at the `INFO2` level and below, even if a `DEBUG`/`DEBUG2` level is configured. When debug information is enabled, it is written separately to a per-worker file named `debug_X.txt` instead, following the same naming scheme; `DEBUG` and `DEBUG2` messages never appear in `log_X.txt` or on the console. Both the log and debug files are created in the same folder as the model script being executed.

## Metadata

Options for the metadata files written next to saved maps. See [Map Metadata](Map-Metadata.html) for the template keywords.

- `-metadata-profile=[metadata-profile]` — Type of the profile used to write file metadata. Values: `CUSTOM=0`, `CSR/UFMG_ptBR=1`, `CSR/UFMG_en=2`.
- `-map-metadata-template-filename=[filename]` — Filename with the template used to write map metadata. Assumes the use of the `CUSTOM` profile.
- `-map-metadata-file-extension=[extension]` — File extension used to write map metadata. Assumes the use of the `CUSTOM` profile.

## Model Output

- `-output=[output]` — Write an output file representing the input model script, without needing to open the GUI to export it. The output format is chosen based on the file extension: `.ego` for EGO Script, `.egoml` for EGOML Script, `.dot` for a Graphviz representation of the model, and `.egomlx` for a bundle script.
- `-dont-run` — Combine with `-output` to only convert a script to another format without executing it.
- `-verifier=[verifier]` — Set the functor verifier used to validate the script before execution. Values: `NonIntrusiveScriptVerifier`, `IntrusiveScriptVerifier`.
- `-write-semicolon-in-csv` — Write CSV files using semicolons as value separators (and commas as decimal marks) instead of the English standard format.

## Integration

- `-session-name=[session-name]` — Create a session with the given name to share data between Dinamica EGO and an external R application via the "Calculate R Expression" functor.

## Miscellaneous

- `-profile` — Enable profiling the execution. When combined with an interactive terminal, this opens a text-based UI with tabs for the message log, worker status, accelerator usage, and resource (memory) tracking.
- `-ask-to-start` — Wait for a confirmation (press ENTER) before running the model.
- `-ask-to-close` — Wait for a confirmation (press ENTER) before closing the console window after execution finishes.
- `-list-functors` — Show the available functors and exit, without running the script.
- `-version` — Show version information and exit.
- `+h`, `-help` — Display the help menu.

## Deprecated Options

The following options are accepted for backward compatibility but are ignored:

- `-scheduler=[scheduler]`
- `-disable-map-swapping`

## Examples

Run a model script using automatic worker detection and the default settings:

```powershell
DinamicaConsole "C:\models\my_model.ego"
```

Run a model script with 4 workers, the Aggressive memory policy, and beep when finished:

```powershell
DinamicaConsole -processors=4 -memory-allocation-policy=4 -beep "C:\models\my_model.ego"
```

Convert a model script to EGOML without running it:

```powershell
DinamicaConsole -dont-run -output="C:\models\my_model.egoml" "C:\models\my_model.ego"
```

List the available accelerator devices:

```powershell
DinamicaConsole -list-accelerators "C:\models\my_model.ego"
```

Run a model script with a reduced, more verbose log level for troubleshooting, restricted to the functor scheduler subsystem:

```powershell
DinamicaConsole -log-level=6 -log-subsystem=8 "C:\models\my_model.ego"
```

Run a model script at the Debug level, logging multiple subsystems at once by summing their flags — here, `GENERAL=1` + `FUNCTOR_SCHEDULER=8` + `MAP_IO_HANDLER=128` = `137`:

```powershell
DinamicaConsole -log-level=6 -log-subsystem=137 "C:\models\my_model.ego"
```
{% endraw %}
