---
title: "Release Notes 8.14.0"
nav_exclude: true
---
{% raw %}
# Dinamica EGO 8.14.0

Changes compared to version 8.13.0.

## 1. GDAL virtual file systems

The support for GDAL virtual file systems was reworked. Loaders and writers, and the [Workdir](functors/Workdir.html) container, can now read from remote locations and archives.

- **URLs** - an input path starting with `<scheme>://` (for example `https`, `http` or `ftp`) is read through `/vsicurl/`.
- **STACIT queries** - STACIT queries are accepted as input.
- **Archives** - when the Workdir is set to an archive, the matching virtual file system is selected from the file extension:

| Extension | Virtual file system |
| --- | --- |
| `.7z` | `/vsi7z/` |
| `.gz` | `/vsigzip/` |
| `.rar` | `/vsirar/` |
| `.tar`, `.tar.gz`, `.tgz` | `/vsitar/` |
| `.zip` | `/vsizip/` |

- **Special schemes** - `mem://` maps to `/vsimem/`, `s3://` maps to `/vsis3/`, and `vsi://` accepts a string with an explicit chain of virtual file systems.
- **Cascading** - virtual file systems can be chained. A Workdir can retrieve an image (for example a `.tif`) from an archive (for example a `.tar.gz`) located at a URL; the chain of prefixes is built automatically.
- **Read-only archives** - archive Workdirs are reported as read-only instead of failing on write attempts.
- **Memory Workdirs** - fixed a regression that prevented writing to memory Workdirs.
- **Case-insensitive extensions** - file extensions are matched regardless of case.
- **Bypassing the Workdir** - the behavior when a loader or writer receives a full path or URL as its input name was clarified in the documentation.
- **Filename editors** - the filename editors accept URLs and STACIT queries.
- **Folder filter** - the file filter for folders also lists the supported archive formats.
- Fixed the validation of a virtual file system Workdir, which could fail.
- Fixed a potential bug when validating the null value of multilayer images with the GDAL map reader and writer.
- Fixed the cleanup when GDAL fails to open a file or virtual file system.

---

## 2. Remote and parallel execution

- **[Run Remotely](functors/Run-Remotely.html) in parallel loops** - fixed a bug where a Run Remotely container executed as part of a parallel loop could fail to transfer its output back to the client.
- Fixed concurrency and memory problems in distributed execution.
- **Text content in parallel loops** - fixed a bug where a parallel loop could remove internal whitespace from text content such as `StringType` and `CodeType`. The global XML parsing settings are now changed only when the application starts.
- Distributed tests now restore the current path when they finish, and no longer depend on the default script reader.

---

## 3. Python integration

- **System-wide pip lock** - the lock used to serialize `pip install` is now system-wide and shared between the Python and C++ sides. If the lock cannot be obtained within 30 minutes, an error is raised.
- **Communication timeout** - [Calculate Python Expression](functors/Calculate-Python-Expression.html) now stops waiting after 30 minutes if Dinamica EGO does not acknowledge the communication.
- **Interpreter creation** - the main GIL is now acquired when the interpreter is created.
- **Error details** - the details of a Python exception now include a header line identifying which log refers to `stdout` and which to `stderr`.
- Lookup table strings are read only when the table has rows.
- Fixed uninitialized pointers, which now start as `nullptr`.
- Fixed a Python test that could fail on some computers.

---

## 4. Process and file system handling

- **Windows** - fixed `stdout` and `stderr` handling in external processes.
- **Linux** - external processes now use `boost::process`, and the process creation flags were fixed.
- **Linux file permissions** - the check for writing a file now verifies the owner and group ids.
- **User name in WSL** - `SystemUtils::getUsername` has an alternative path on Linux when `getlogin_r` is unavailable, as in WSL.
- **System error messages** - on Linux, the last system error is obtained with `std::system_category`, replacing the non thread-safe `strerror`.
- **File locks** - `FilenameLock` has a timeout, and the unused `preventSharing` flag was removed.
- `FilesystemUtils::writeFilename` now raises an error when the write fails.

---

## 5. Elevation graphs

- **Faster traversal** - traversing an elevation graph no longer revisits nodes that were already traversed. The change is especially noticeable on Linux, where repeated visits caused a large increase in the number of analyzed nodes.
- Elevation graph tests were updated to avoid failures caused by evaluation order and concurrency, and the slow ones were removed from the fast test sets.
- Added test cases that run the latest version of the hilltop detection model.

---

## 6. Image expressions

- **Fixed: value distortion** - the expression `iX[exp1, exp2]` could distort double-precision values and large 32-bit integer values in map calculations. The values are now returned correctly.

---

## 7. Sequence ports in Print, Execution Policy and Log Policy

[Print](functors/Print.html), [Execution Policy](functors/Execution-Policy.html) and [Log Policy](functors/Log-Policy.html) have a new optional input port `sequenceInput` and a new output port `sequenceOutput`, both of type `NoneType`. They force the execution order between these functors and other functors:

- `sequenceInput` - the functor connected to this port executes before the group.
- `sequenceOutput` - the group executes before the functor connected to this port.

---

## 8. EGO Script defaults

The following options under *Tools => Options \| EGO Script* are now enabled by default:

- Inlining using the extended syntax.
- Use abbreviated syntax for Calculate family functors.

---

## 9. Interface

- **Port editors** - new icons indicate connected ports and exported inputs, which makes clear why the content of a port cannot be edited directly.
- **Documentation panel** - added a navigation toolbar.
- **Documentation links** - the application links to the new documentation site, including the functor documentation and the release notes of the running version. The reference to the DokuWiki was removed from the About window, and the list of authors was updated.
- **Functor list** - after the list of functors is dumped in the message log, the panel is made visible.
- Renamed `PackageInfo` to `GroupInfo` in the source code for clarity.

---

## 10. Console and diagnostics

- **Functor list format** - the dump of the functor factory prints a preamble describing the output format, followed by a less verbose description of functors and ports. The new `dumpScheme` parameter (default true) makes the console functor list print the submodel preamble only once.
- **Temporary files** - the environment variable `DINAMICA_EGO_SKIP_TEMP_CLEANUP` disables the removal of temporary files when the application quits. See [Environment Variables](Environment-Variables.html).
- Fixed the exception propagation flag and the initial values of the common arguments in the console.
- Fixed the reference to the Dinamica version in the `run_console` script.
- Added debug logging to the OpenCL kernel building functions.

---

## 11. Build and development

- **vcpkg 2026.07.29** - compatibility updates for the `fmt` library, removal of unnecessary copies of the `minizip-ng` libraries, and a workaround for an interaction between `nameof` and the newest `fmt`.
- **Linux setup** - added missing packages to the setup script, and a script that integrates R from the terminal.
- **README** - translated to English, with corrections to the compilation instructions.
- **String conversion** - `fromU8String()` and `fromU8StringString()` were integrated into the `toString()` family (the latter as `toStringView()`), and overloads for all string types were added.
- Comments in the Coupling, Image, Prim, Region and Simulation plugins and in the test files were translated from Portuguese to English.
- Removed compilation warnings and fixed the inclusion of `FilenameLock.h`.
- Fixed table tests on Linux, the copy of `dinamica.h` in the Linux test scripts, and a test that could hang in the fast test set.

---

## 12. Documentation

The documentation moved to a new site, built from the `dinamica-docs` repository.
{% endraw %}
