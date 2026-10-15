---
title: "Frequently Answered Questions"
nav_order: 9
---
{% raw %}
# Frequently Answered Questions

## GNU/Linux

For GNU/Linux related questions, please refer to Dinamica GNU/Linux - Frequently Asked Questions

## Installation and Startup

#### Question I-1

**After installing Dinamica EGO it shows only a blank screen with a toolbar and a menubar. What is wrong?**

To work around the problem, open Dinamica EGO, go to the *Window* menu, and choose the *Reset Window Layout* item. Then close Dinamica EGO and start it again. Dinamica EGO should display the correct layout on the next run.

Typically, this problem only occurs on the first run of a new Dinamica EGO installation.

#### Question I-2

**Dinamica EGO will not start because it says 'Could not create the Java virtual machine'. What is wrong?**

Edit the file `Dinamica.vmoptions` located in the Dinamica EGO installation folder using a plain text editor (like Notepad or [Notepad++](https://notepad-plus-plus.org)). The content of the original file can be seen below:

```
-Xss1m
-Xms64m
-Xmx8096m
```

These values represent the maximum amount of memory available to the Dinamica graphical interface (in megabytes). If Dinamica still isn't launching, lower the `-Xmx` value and try again. Only lower it just far enough to allow Dinamica to launch — the lower this value is, the less memory the interface is allowed to use. Lowering this value doesn't impact model execution performance, but the graphical interface may become unusable.

#### Question I-3

**Dinamica EGO will not start because it says 'Unable to deserialize perspectives from XML'. What is wrong?**

The perspective file used to store the layout of the graphical interface is probably corrupted. To work around this issue, remove the folder containing the perspective configuration and restart the application.

The perspective configuration file is usually stored in the folder `C:\Users\<User>\.jydocking`.

#### Question I-4

**Dinamica EGO does not install on my computer. When I click on the Dinamica EGO installer, nothing happens. What is wrong?**

First, make sure the installer is not corrupted. Also, make sure your anti-virus is not blocking the Dinamica EGO installer.

Windows Defender (and some anti-virus software) tends to warn the user about a potential hazard when installing Dinamica EGO. This isn't caused by Dinamica itself — it's simply that Dinamica EGO isn't as widely used as software like Microsoft Office or Google Chrome, so anti-virus tools flag it as unknown or suspicious. It's safe to ignore these warnings and proceed with the installation, as long as you've downloaded Dinamica EGO from a reliable source, preferably the Dinamica EGO website.

#### Question I-5

**When I try to run Dinamica EGO, I get a message box that says 'Unable to load library "JavaBinding"'. What is wrong?**

Installing the "Visual C++ Redistributable for Visual Studio" on your computer will fix the issue. The Dinamica EGO installer usually installs the redistributable files automatically, but if that fails, you may need to install them manually:

Go to the [Microsoft website](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) and click "Download."

After installing this utility, try running Dinamica EGO again.

## Updates, Security, and Privacy

#### Question U-1

**My anti-virus is telling me that Dinamica EGO is trying to open an Internet connection. Why does Dinamica EGO need access to the Internet?**

Dinamica EGO uses an Internet connection to check for new updates and to access the online documentation. No information other than the version of the Dinamica EGO software installed on your system is sent — see question U-2.

If you prefer, you can turn off this version check by disabling "Tools => Options \| System \| Update," though this is not recommended.

#### Question U-2

**How does Dinamica EGO interact with the CSR/UFMG servers? What kind of information does it send back while I'm running the software?**

- From time to time, it sends a request to our servers checking whether the user has the latest version of the software. If not, it downloads and applies an update. The user is free to turn off automatic update checking, which prevents any version checking from happening at all. The only information ever sent to our servers during this check is the current version of the Dinamica software running on the computer — nothing that could be used to identify the user or the computer is ever sent.
- Users can send data to our servers by accessing the "[submodel](Submodels.html)" repository within the application, or by downloading "[submodels](Submodels.html)" from our server. Both actions have to be explicitly started by the user. When browsing the "[submodel](Submodels.html)" repository, the user sees a list of "[submodels](Submodels.html)" available for download; installing one downloads a file into the user's `%localappdata%\Dinamica EGO X` folder (where X is Dinamica EGO's major version number) so it can be used by the software.
- When browsing a model and clicking the "?" button on the action bar, the user opens an online wiki page with documentation for that functor or operator — for instance, [Calc Cost Map](functors/Calc-Cost-Map.html). This is just a standard request for a static page and doesn't send any information that could identify the user or the computer.

## Runtime Errors and Crashes

#### Question R-1

**When I'm running a simulation model, Dinamica EGO closes without showing any error message. What should I do?**

1. Open Dinamica EGO with administrator privileges, using "Run As Administrator."
1. Open the model and run it.
1. As soon as Dinamica EGO crashes and closes, go to the folder where it was installed — typically `C:\Program Files\Dinamica EGO` — and copy the files `hs_err_pidXXXX.log` and `hs_err_pidXXXX.mdmp` (XXXX is a number)((There may be more than one file with that name inside the installation folder. Make sure you get the most recent one)).
1. Compress these two files into a zip file and send it to dinamica@csr.ufmg.br so we can try to find out what's causing Dinamica EGO to crash.

#### Question R-2

**Sometimes when I try to load a model in Dinamica EGO, I get the following error message: 'The input port "\<\< some name here >>" is not defined.' What am I doing wrong?**

This is probably caused by an old Dinamica EGO version. Download and install the latest version from the [Download](https://www.csr.ufmg.br/dinamica/download) section of the website — it will likely solve your problem.

## Performance and Memory

#### Question P-1

**How can I maximize Dinamica EGO's performance?**

See "Useful Tips: Increasing performance".

#### Question P-2

**How can I prevent Dinamica EGO from showing "Memory allocation has failed" when it runs my models?**

A few things to try:

- Run Dinamica EGO on a machine with as much available memory as possible.
- Set the memory management option ("Tools" -> "Options" \| "Advanced") to "Balanced." If you're using the command line tool, use the option `-memory-allocation-policy` with value `1`.
- Reduce the number of lines and columns in your maps.
- Reduce the number of different transitions (2 to 1, 5 to 3, etc.) in your simulation — this reduces the number of layers in the probability map and uses less memory.
- Use sub-regions in your simulation. This lets [Patcher](functors/Patcher.html) and/or [Expander](functors/Expander.html) work through your landscape and probability map one sub-region at a time, using less memory.

#### Question P-3

**How do I change the folder where Dinamica EGO stores temporary images and temporary DLL libraries?**

By default, Dinamica EGO uses the Windows temporary folder to store temporary images and compiled libraries. You can change this directly in the GUI, via "Tools -> Options -> Advanced \| Use alternative folder for storing temporary files."

Alternatively, you can point Dinamica at a different folder — independent of the one Windows itself uses — by defining an environment variable named `DINAMICA_TEMP_DIR` with the path to the new folder. On Windows 10, go to "Start menu -> Settings -> System \| About \| System Info -> Advanced system settings -> Advanced \| Environment Variables \| System variables." Click "New," then type `DINAMICA_TEMP_DIR` as the variable name and choose the new path as its value.

## The Expression Language

#### Question E-1

**I am seeing the following message: 'This operator is deprecated and should be removed in future releases of Dinamica.' What does it mean?**

It means the operator is no longer recommended, since it will be removed in a future release. Avoid using it going forward, and if it's already used in an existing model, replace it with a newer operator that performs the same function.

#### Question E-2

**Why does Dinamica EGO automatically convert tests like `i1 == null` to `isNull(i1)`?**

The expression below doesn't have the meaning it appears to:

```
if i1 == null then
  null
else
  1
```

`i1 == null` always evaluates to `null`, because `null` can't be used in any algebraic expression without "poisoning" its result. For the same reason, expressions like `i1 + null`, `i1 / null`, and `if null then 1 else 2` always evaluate to `null` as well. To avoid this, an image's value has to be tested for null explicitly, using the `isNull` operator or `?`. The correct version of the expression above is:

```
if isNull(i1) then
  null
else
  1
```

Dinamica EGO automatically detects the incorrect expression and rewrites it to reflect what the user actually intended.

> **Editor's note:** The null-poisoning behaviour of `i1 == null` described above is confirmed and consistent with the rest of this wiki's documentation. The specific claim that Dinamica EGO **automatically rewrites** the expression in the saved model, however, is not something the editor has an independent source to confirm. It's plausible as a GUI-level safeguard, but should be verified before being relied upon.

For more on expression syntax, see the documentation of the [Image Expression Type](types/Image-Expression-Type.html). For more on how null values are handled during map and value calculations, see [Null Value Handling](Calculate-Functors.html#null-value-handling) on Calculate Functors.

## Modeling and Calibration

#### Question M-1

**Is it possible to automatically calibrate the values for "mean patch size," "patch variance," and "patch isometry" in Dinamica EGO?**

There is no mechanism for calibrating those values automatically in Dinamica EGO. If you'd rather not rely on trial and error, we recommend using different software, such as [Fragstats](https://fragstats.org/), to calculate the parameters.

#### Question M-2

**Why does Dinamica EGO say it can't calculate the multi-step transition matrix?**

The multi-step matrix can only be calculated with the [Determine Transition Matrix](functors/Determine-Transition-Matrix.html) functor if the single-step matrix has a decomposition into its corresponding eigenvectors and eigenvalues. Without that decomposition, the process can't be represented as an ergodic matrix — that is, the eigenvalues aren't real numbers. The time-step matrix is obtained as follows:

P = M \* V \* INVM

- `M` — matrix of eigenvectors
- `V` — matrix of eigenvalues (a diagonal matrix, with nonzero values only along its diagonal)
- `INVM` — inverse of the matrix of eigenvectors

To get the time-step matrix, the elements of matrix V must be raised to the power (1/t), where t is the number of time steps within the time period. Not every matrix has real-number eigenvalues, which is the source of the error.

It's still possible to work around this limitation by calculating a separate transition matrix for each year, using crude rates instead of net rates. The model variable_time_step_net_transition_rates and the submodel Calc Net Transition Rates, both available as part of the standard Dinamica EGO distribution, use this technique.

#### Question M-3

**How can I improve the similarity values resulting from my model calibration?**

See [this post](https://csr.ufmg.br/dinamica/2015/09/22/validation/) on the Dinamica website about validation.

## Documentation and Resources

#### Question D-1

**I can't find Dinamica's PDF guidebook file anywhere. Where was it installed?**

It's no longer distributed as a PDF — the guidebook is now part of the online documentation wiki.

#### Question D-2

**What image formats does Dinamica EGO support?**

Dinamica EGO supports most image formats supported by GDAL. See the list of supported map formats.

#### Question D-3

**I can't find Dinamica's examples. Where are they installed?**

Download them from [Dataset Download](https://csr.ufmg.br/dinamica/nui_download/1054/).

## General

#### Question G-1

**What languages is Dinamica EGO available in?**

For now, the software is only available in English.

#### Question G-2

**What's the difference between each log level available in Dinamica EGO?**

See [Log Levels](types/Log-Tag-Type.html#log-level).

#### Question G-3

**I'm interested in purchasing Dinamica EGO for use in my dissertation. How do I do that?**

Dinamica EGO is [free for scientific, commercial, and non-commercial use](https://csr.ufmg.br/dinamica/license). Go to the [Download](https://www.csr.ufmg.br/dinamica/dinamica-8) section of the website to get it — it includes everything you need to get started, including file examples.
{% endraw %}
