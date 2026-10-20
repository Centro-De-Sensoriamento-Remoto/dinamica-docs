---
title: "Remote Execution"
nav_order: 6
parent: "Modeling Guides"
---
{% raw %}
# Remote Execution

Dinamica EGO can run parts of a model on other machines. Three programs take part:

- **Coordinator**: receives the jobs posted by models and distributes them to the connected agents.
- **Agent**: runs the jobs assigned by the coordinator. Several agents, on one or more machines, can connect to the same coordinator.
- **Dinamica EGO**: runs the model. The parts of the model placed inside a [Run Remotely](functors/Run-Remotely.html) container are sent to the coordinator; the rest runs locally.

## Coordinator Setup

On the machine that will act as the coordinator, go to a folder where you have write permission and run:

**Windows**

```
"C:\Program Files\Dinamica EGO <major>\DinamicaCoordinator<major>" --address X.X.X.X --port YYYY
```

**Linux**

```
./DinamicaEGO-<version>-Ubuntu-LTS.AppImage --coordinator --address X.X.X.X --port YYYY
```

`<major>` is the major version of Dinamica EGO, which is part of the installation folder and of the program name on Windows. For example, in Dinamica EGO 8 the coordinator is `C:\Program Files\Dinamica EGO 8\DinamicaCoordinator8`. `<version>` is the full version in the name of the AppImage file. `X.X.X.X` is the IP address of the coordinator machine and `YYYY` is the port where it listens for connections.

The main coordinator options are:

| Option | Description |
| --- | --- |
| `--address` | Network address of the coordinator. Required. |
| `--port` | Port of the coordinator. Required. |
| `--receive-interval` | Interval, in milliseconds, between polls for new messages. Default: 1500. |
| `--disconnect-timeout-ms` | Time, in milliseconds, after which an unresponsive peer is disconnected. |
| `--job-pending-timeout-ms` | Time, in milliseconds, after which an unresponsive pending job is dropped from the queue. |
| `--job-executing-timeout-ms` | Time, in milliseconds, after which an unresponsive executing job is dropped from the queue. |
| `--job-confirmation-timeout-ms` | Time, in milliseconds, after which an unresponsive confirmation job is dropped from the queue. |
| `--status-filename` | File where the coordinator writes its status, in JSON format, every 5 seconds. A file with the same name and the extension `.lock` prevents two processes from accessing it at the same time. |
| `--ui` | Shows a text interface instead of printing to the standard output and error. |

Run the coordinator with `--help` to list all options.

## Agent Setup

On each machine that will run jobs, go to a folder where you have write permission and run:

**Windows**

```
"C:\Program Files\Dinamica EGO <major>\DinamicaAgent<major>" --address X.X.X.X --port YYYY
```

**Linux**

```
./DinamicaEGO-<version>-Ubuntu-LTS.AppImage --agent --address X.X.X.X --port YYYY
```

`<major>` and `<version>` follow the same rule as for the coordinator; in Dinamica EGO 8 the agent is `C:\Program Files\Dinamica EGO 8\DinamicaAgent8`. `X.X.X.X` and `YYYY` are the address and port of the coordinator. An agent can run on the same machine as the coordinator, but this is not recommended when its jobs are computationally intensive.

The main agent options are:

| Option | Description |
| --- | --- |
| `--address` | Network address of the coordinator. Required. |
| `--port` | Port of the coordinator. Required. |
| `--identifier` | Custom identifier sent to the coordinator. |
| `--receive-interval` | Interval, in milliseconds, between polls of the coordinator. Default: 1500. |
| `--poll-interval` | Interval, in milliseconds, between polls of the coordinator looking for work. Default: 1000. |
| `--reconnect-retry-attempts` | Overrides the number of reconnection attempts. |

Run the agent with `--help` to list all options.

## Running Parts of a Model Remotely

1. On the machine where the model is, go to **Tools → Options → Execution → Remote Computing** and enter the coordinator's address and port.
2. Place the functors that should run remotely inside a [Run Remotely](functors/Run-Remotely.html) container.
3. Run the model as usual. The content of each Run Remotely container is sent to the coordinator, which assigns it to an agent.

## Overriding the Coordinator Settings

The input ports of [Run Remotely](functors/Run-Remotely.html) override the settings defined in the options:

- **Coordinator Connection Info** sets the coordinator address and port. Build it with [Create Connection Info](functors/Create-Connection-Info.html).
- **Network Error Behavior** chooses between stopping the model and running the content locally when the coordinator cannot be reached.
- **Job Wait Time Limit** sets how long to wait for the job to finish.
- **Requirement Expression** sets the requirements an agent must meet to receive the job.

This makes it possible to change the connection while the model runs, which helps when the network configuration varies or when several distributed setups are in use.

## Using Multiple Coordinators

Different Run Remotely containers in the same model can connect to different coordinators. Each part of the model is then processed by its own coordinator and agents, which spreads large workloads across separate groups of machines.

## Limitations

- Most data types can be passed from functors outside a Run Remotely container to functors inside it. Maps are the exception: connecting a map from outside to a functor inside the container raises an error.
- Data cannot be passed from functors inside a Run Remotely container to functors outside it. Doing so raises an error.
{% endraw %}
