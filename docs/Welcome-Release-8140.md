---
title: "Welcome"
nav_exclude: true
---
{% raw %}
# Welcome to Dinamica EGO 8

Dinamica EGO 8.14.0 is installed.

## Release Notes

The changes in this version are listed in the [Release Notes for 8.14.0](Release-Notes-8-14-0.html).

## Documentation

- [Documentation home](index.html) - reference for the interface, EGO Script, expressions, and every functor and data type.
- [Guidebook](guidebook/index.html) - a step-by-step course, from the basics of the interface to land-use change simulation and calibration.
- [Videos](http://www.dinamicaego.com/media) - short videos on the basic features.

## Discussions

Questions about using Dinamica EGO are discussed in the [GitHub Discussions](https://github.com/Centro-De-Sensoriamento-Remoto/dinamica-docs/discussions) of the documentation repository. This is the preferred place for discussions.

The earlier [Dinamica EGO Discussion Group](https://groups.google.com/forum/#!forum/dinamica-ego), a Google Groups forum, remains available as a reference for past discussions.

## Troubleshooting

The [FAQ](FAQ.html) lists solutions for common problems with installation, startup, and runtime errors.

## Enhancement Plugin

The [Enhancement Plugin for Dinamica EGO 8.14.0](https://csr.ufmg.br/dinamica_utils/download/SetupDinamicaEGO-8140-EnhancementPlugin.exe) (Windows) is optional. Its use depends on the feature:

- **Python** - [Calculate Python Expression](functors/Calculate-Python-Expression.html) does not require the plugin.
- **R** - the plugin is needed only to use R without providing your own R installation. It supplies the R interpreter used by [Calculate R Expression](functors/Calculate-R-Expression.html) on Windows. Setup is described in [Coupling With R](Coupling-With-R.html).
- **Native expression compilation** - expressions are compiled to native code only when the plugin is installed and the option *Tools => Options \| Advanced \| Disable compilation of native expressions* is cleared. See [Native Expression Compilation](gui/Options-And-Performance.html#native-expression-compilation).
{% endraw %}
