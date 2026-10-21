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
- **Requirement Expression** sets the requirements an agent must meet to receive the job. See [Choosing Agents with Requirements](#choosing-agents-with-requirements).

This makes it possible to change the connection while the model runs, which helps when the network configuration varies or when several distributed setups are in use.

## Choosing Agents with Requirements

The **Requirement Expression** port of [Run Remotely](functors/Run-Remotely.html) limits which agents can run the container's content.

When an agent connects to the coordinator, it reports four values about its machine. The requirement expression reads them as a lookup table, `t1`, with these keys:

| Key | Value |
| --- | --- |
| `t1["numCpus"]` | Number of logical processors. |
| `t1["memoryGB"]` | Total memory, in whole gigabytes. |
| `t1["numGpus"]` | Number of OpenCL compute devices (accelerator devices). |
| `t1["tempSpaceGB"]` | Free space in the temporary folder, in whole gigabytes. |

The values are measured once, when the agent connects. Memory and free space are rounded down to whole gigabytes.

The coordinator evaluates the expression for each agent. An agent can run the job when the result is greater than zero; a result of zero or less, a null result or an evaluation error excludes the agent. For example, this expression only accepts agents with at least 8 logical processors and 32 GB of memory:

```
t1["numCpus"] >= 8 and t1["memoryGB"] >= 32
```

The expression is checked at these moments:

- **When the job is posted.** The coordinator evaluates the expression for every connected agent and sends the job only to the agents that meet it. If none does, the job is rejected with the message "There are no agents capable of running with the required specifications", and the container follows its **Network Error Behavior**.
- **When an agent connects later.** The coordinator evaluates the expression of the jobs that are still waiting, and the new agent can receive the ones it meets.

Without a requirement expression, any agent can run the job. If no agent is connected, the job is rejected with the message "There are no agents registered into the coordinator to run any job."

## Using Multiple Coordinators

Different Run Remotely containers in the same model can connect to different coordinators. Each part of the model is then processed by its own coordinator and agents, which spreads large workloads across separate groups of machines.

## Example Model

This model calculates the area of each class of two landscape maps, each on a different agent, and saves the results on the machine that runs the model. It uses the maps `23267 1997.tif` and `23267 2000.tif` from `guidebook dinamica\database\lucc files` in the [Guidebook dataset](extra/guidebook_dinamica.7z).

```
@charset = UTF-8
Script {{
    // Coordinator that distributes the jobs to the agents.
    coordinator := CreateConnectionInfo $"(192.168.0.10)" 5555;

    // Calculates the class areas of the 1997 landscape on an agent.
    _ := RunRemotely {
        coordinatorConnectionInfo = coordinator,
        networkErrorBehavior = .runLocally
    } {{
        landscape1997 := LoadCategoricalMap "D:/guidebook dinamica/database/lucc files/23267 1997.tif";

        areas1997 := CalcAreas landscape1997 .no;
    }};

    // Calculates the class areas of the 2000 landscape on an agent with at least 4 logical processors.
    _ := RunRemotely {
        coordinatorConnectionInfo = coordinator,
        networkErrorBehavior = .runLocally,
        requirementExpression = [
            t1["numCpus"] >= 4
        ]
    } {{
        landscape2000 := LoadCategoricalMap "D:/guidebook dinamica/database/lucc files/23267 2000.tif";

        areas2000 := CalcAreas landscape2000 .no;
    }};

    // Saves the tables calculated by the agents on the machine that runs the model.
    SaveTable areas1997 "areas 1997.csv";

    SaveTable areas2000 "areas 2000.csv";
}};
```

How it works:

- **Two jobs at the same time.** The two Run Remotely containers do not depend on each other, so they run at the same time, as any two independent functors do (see [Parallel Execution](Parallel-Execution.html)). Each one posts its content to the coordinator as a separate job, and the coordinator assigns the jobs to two agents.
- **Coordinator.** [Create Connection Info](functors/Create-Connection-Info.html) builds the address and port of the coordinator, passed to both containers. Without it, the containers use the coordinator set in **Tools → Options → Execution → Remote Computing**. Replace `192.168.0.10` and `5555` with the address and port of your coordinator.
- **Requirement.** The second container only goes to an agent with at least 4 logical processors. See [Choosing Agents with Requirements](#choosing-agents-with-requirements).
- **Maps stay on the agent.** Maps cannot cross the border of a Run Remotely container, so each container loads its own map. The file is read by the agent, on the agent's machine, so the path must point to a copy of the file there. In this example, the dataset is in `D:\guidebook dinamica` on every agent.
- **Results come back.** The area tables calculated by the agents are used outside the containers, by Save Table, which runs on the machine that runs the model and saves the files there.
- **Network errors.** With **Network Error Behavior** set to **Run Locally**, a container whose job cannot be run remotely runs on the local machine instead.

The same approach works with loops: when the steps of a loop meet the conditions to run at the same time, a Run Remotely container inside the loop posts one job per step, and each step can run on a different agent.

### Example with a Loop

This model calculates the area of each class in the four quadrants of a landscape map, each quadrant on an agent, and combines the results in a single table. It uses `23267 1997.tif` from the same folder of the Guidebook dataset.

```
@charset = UTF-8
Script {{
    // Coordinator that distributes the jobs to the agents.
    coordinator := CreateConnectionInfo $"(192.168.0.10)" 5555;

    // Corners of the four quadrants of 23267 1997.tif, in the map's coordinates (degrees).
    quadrants := Table [
        "Quadrant*", "X1", "Y1", "X2", "Y2",
        1, -64.593132, -9.272404, -63.673027, -10.113268,
        2, -63.673027, -9.272404, -62.752922, -10.113268,
        3, -64.593132, -10.113268, -63.673027, -10.954131,
        4, -63.673027, -10.113268, -62.752922, -10.954131
    ];

    // Table that receives the areas of all the quadrants.
    emptyAreas := Table [ "Quadrant*#real", "Category*#real", "Area_In_Cells#real", "Area_In_Hectares#real", "Area_In_Square_Meters#real" ];

    TableManager {{
        // Each step calculates the class areas of one quadrant.
        loopDone := For 1 4 {{
            quadrant := Step;

            x1 := GetTableValue quadrants quadrant "X1";

            y1 := GetTableValue quadrants quadrant "Y1";

            x2 := GetTableValue quadrants quadrant "X2";

            y2 := GetTableValue quadrants quadrant "Y2";

            // Loads the quadrant and calculates its class areas on an agent.
            _ := RunRemotely {
                coordinatorConnectionInfo = coordinator,
                networkErrorBehavior = .runLocally
            } {{
                landscape := LoadCategoricalMap {
                    filename = "D:/guidebook dinamica/database/lucc files/23267 1997.tif",
                    firstWindowCoordinateX = x1,
                    firstWindowCoordinateY = y1,
                    secondWindowCoordinateX = x2,
                    secondWindowCoordinateY = y2
                };

                quadrantAreas := CalcAreas landscape .no;
            }};

            // Registers the areas of this quadrant, identified by the quadrant number.
            _ := SubTable "areas" quadrant quadrantAreas;
        }};

        // Waits for all the steps and combines the areas of the four quadrants in one table.
        _ := Group loopDone {{
            allAreas := MergeSubTables emptyAreas "areas";

            SaveTable allAreas "areas by quadrant.csv";
        }};
    }};
}};
```

How it works:

- **One job per step.** The steps of the loop do not depend on each other: the loop has no mux, and nothing inside it is used outside it. So the four steps run at the same time, and each Run Remotely container posts its own job. With four agents connected, each quadrant is calculated by a different agent; with fewer, the coordinator gives the remaining jobs to the agents as they become free.
- **Values into the container.** The quadrant corners are read from the `quadrants` table outside the container and passed in as numbers. [Load Categorical Map](functors/Load-Categorical-Map.html) uses them as its crop window, so each agent loads only its quadrant.
- **Tables out of the container.** The area table calculated by the agent is used outside the container, by [Sub Table](functors/Sub-Table.html), which registers it in the enclosing [Table Manager](functors/Table-Manager.html) with the quadrant number as its key.
- **Combining the results.** [Merge Sub Tables](functors/Merge-Sub-Tables.html) inserts the four tables in `emptyAreas`, which gets a `Quadrant` key column before the columns of [Calc Areas](functors/Calc-Areas.html). The [Group](functors/Group.html) that contains it waits for the loop through `loopDone`, so the merge only runs after every step has finished. See [Table Manager](Manipulating-Tables-And-Lookup-Tables.html#table-manager).

The quadrants meet at a cell border. To check that no cell is counted twice or left out, compare the total area of the combined table with the result of Calc Areas for the whole map.

## Limitations

- Most data types can be passed from functors outside a Run Remotely container to functors inside it. Maps are the exception: connecting a map from outside to a functor inside the container raises an error.
- Values produced inside a Run Remotely container, such as numbers, strings, tables and lookup tables, can be used by functors outside it. Maps are again the exception: using a map produced inside the container outside it raises an error.
- A viewer attached to a map output port inside a Run Remotely container raises an error.
{% endraw %}
