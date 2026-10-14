---
title: "Connection Info Type"
nav_exclude: true
---
{% raw %}
# Connection Info Type

A Connection Info identifies a remote network Coordinator by its address and port. [Run Remotely](Run-Remotely.html) uses one, via its `coordinatorConnectionInfo` input, to know where to send the functors it contains for remote execution; if left unset, the address configured in the application settings is used instead. [Create Connection Info](Create-Connection-Info.html) builds one from separate `address` and `port` inputs.

## GUI Editor

The connection info editor presents fields for the network address and port.

## EGO Script

A Connection Info constant is written in [EGO Script](EGO-Script.html) as an address and a port, in that order, separated by a required comma. The address is a hostname, IPv4, or IPv6 string enclosed in double quotes; the port is an integer from 0 to 65535:

```
[ "192.168.0.1", 8080 ]
```

```
[ "2001:0db8:85a3:0000:0000:8a2e:0370:7334", 8080 ]
```

## Automatic Conversions

None — Connection Info Type converts to or from no other type.

See [Type System](Type-System.html) for the complete conversion reference across all types.
{% endraw %}
