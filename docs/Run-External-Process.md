---
title: "Run External Process"
nav_exclude: true
---
{% raw %}
# Run External Process

## Description

Runs an executable file external to Dinamica EGO, passing it the necessary parameters. It can either block the model's execution until the process finishes (or for a specified number of seconds), or launch the process and let the model continue running in parallel with it.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| File Name | [String Type](String-Type.html) | Full path of the executable file to run. This port is compact — its value is typed directly rather than supplied through a connection. If no extension is given, .exe is appended automatically, except when the name ends in a bare period or already includes a directory path, in which case nothing is appended. An executable with a different extension (for example, .com) must include it explicitly. Enclose the value in double quotes if it contains spaces. |
| Parameters | [String Type](String-Type.html) | Parameters passed to the executable. May be left empty if no parameters are needed. This port is compact. To run a prompt command or a batch file on Windows, set File Name to cmd.exe and Parameters to "/c NAME_OF_FILE_OR_COMMAND". |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Wait Process Completion | [Boolean Value Type](Boolean-Value-Type.html) | If true, the model waits for the external process to finish before continuing. If false, the model continues running in parallel with the launched process. This is an advanced port. | Yes |
| Seconds To Wait | [Integer Value Type](Integer-Value-Type.html) | After launching the process, the number of seconds the model waits before continuing execution. If zero, the model waits for the process to finish entirely. This is an advanced port. | 0 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Exit Code | [Integer Value Type](Integer-Value-Type.html) | Value returned by the process, if its execution has completed. This output can be ignored. |

## Group

[Control](Functor-List.html#control)

## Notes

When File Name has no directory path, the executable is located by searching, in order: the current directory, Dinamica EGO's own directory, the 64-bit Windows system directory, the 32-bit Windows system directory, the 16-bit Windows system directory, and finally the Windows directory itself.

If Wait Process Completion is true and Seconds To Wait is zero, the model waits indefinitely for the process to finish. If Seconds To Wait is greater than zero, the model waits only that many seconds and then continues, detaching from the process, which keeps running on its own. If Wait Process Completion is false, the model detaches from the process immediately after launching it.

On Windows, the process is created, waited on, and its handles are closed using the operating system's own process APIs; the process is terminated if the model is aborted while it is still running. When the model does not wait for the process to finish, or the process does not finish within the specified wait time, a background thread watches for the process's termination so its handles can still be closed, and terminates it if the model itself is aborted. The process runs under the same security context as Dinamica EGO itself.

The process's standard output and standard error are shown in the message log while, and if, the model waits for it: standard output is logged as an informational message, and standard error is logged as an error message. Standard error is only shown in the log when the process execution reports an error; otherwise, its content is not shown.

## Internal Name

RunExternalProcess
{% endraw %}
