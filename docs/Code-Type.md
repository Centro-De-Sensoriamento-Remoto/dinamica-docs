---
title: "Code Type"
nav_exclude: true
---
{% raw %}
# Code Type

A Code value is a character string used specifically to hold source code — the Python or R script run by [Calculate Python Expression](Calculate-Python-Expression.html) and [Calculate R Expression](Calculate-R-Expression.html), for instance. It's a distinct type from [String](String-Type.html) rather than a subtype of it: moving between the two goes through an ordinary registered conversion, which is what lets the interface present a dedicated code editor for Code inputs instead of the plain text field used for String.

## GUI Editor

The code editor presents a larger, code-oriented text area suited to writing multi-line source, rather than the single-line field used for a String.

## EGO Script

Code Type has its own literal syntax, parsed directly rather than going through a conversion — it accepts either of two forms.

**Raw string.** The same `$"<delimiter>( raw_characters )<delimiter>"` syntax used by [String Type](String-Type.html) constants (see [String Type's Raw String Format](String-Type.html#raw-string-format-starting-on-dinamica-501)): `raw_characters` is used directly as the script text, with no encoding involved, and `<delimiter>` is any character that, together with the closing parenthesis, doesn't appear inside the script — it can be omitted entirely when the closing parenthesis alone doesn't appear in the content. This is the form the GUI code editor generates when it writes a constant:

```
$"(import numpy as np
dinamica.outputs['result'] = np.mean([1, 2, 3]))"
```

**Base64.** The legacy double-quoted string syntax (see [String Type's Legacy](String-Type.html#legacy) format), holding the script text encoded as base64:

```
"aW1wb3J0IG51bXB5IGFzIG5wCmRpbmFtaWNhLm91dHB1dHNbJ3Jlc3VsdCddID0gbnAubWVhbihbMSwgMiwgM10p"
```

Decoded, this represents the same script as the raw string example above. Encoding the source this way lets it keep any characters, quoting, or exact whitespace and line breaks without needing to escape anything for the script's own text syntax — useful for scripts generated or transformed programmatically rather than typed directly. Editing base64 text by hand risks introducing invalid base64, which the parser rejects.

## Automatic Conversions

- **Converted from**: [String Type](String-Type.html) — the string's text is taken directly as the script; no base64 encoding is required.
- **Converted to**: [String Type](String-Type.html) — produces the script's textual representation, not a base64 encoding.

See [Type System](Type-System.html) for the complete conversion reference across all types.
{% endraw %}
