# Dinamica EGO Documentation

Reference documentation for [Dinamica EGO](https://dinamicaego.com), the environmental modeling and simulation platform developed by the Centro de Sensoriamento Remoto (CSR/UFMG).

**[Read the documentation →](https://centro-de-sensoriamento-remoto.github.io/dinamica-docs/)**

## Where to start

| If you want to… | Go to |
| --- | --- |
| Write or read a model as text | [EGO Script](https://centro-de-sensoriamento-remoto.github.io/dinamica-docs/EGO-Script.html) |
| Understand how a model executes | [Basic Data Flow](https://centro-de-sensoriamento-remoto.github.io/dinamica-docs/Basic-Data-Flow.html) |
| Reuse parts of a model | [Submodels](https://centro-de-sensoriamento-remoto.github.io/dinamica-docs/Submodels.html) |
| Run a model from the command line | [Dinamica Console](https://centro-de-sensoriamento-remoto.github.io/dinamica-docs/Dinamica-Console.html) |
| Look up a functor | [Functor List](https://centro-de-sensoriamento-remoto.github.io/dinamica-docs/Functor-List.html) |
| Look up a data type | [Type System](https://centro-de-sensoriamento-remoto.github.io/dinamica-docs/Type-System.html) |
| Troubleshoot an issue | [FAQ](https://centro-de-sensoriamento-remoto.github.io/dinamica-docs/FAQ.html) |

## Contributing

The site is built by GitHub Pages (Jekyll with the [just-the-docs](https://just-the-docs.com) theme) from the `docs/` folder. To update a page, edit the corresponding Markdown file in `docs/` and keep links relative, e.g. `[Map Type](types/Map-Type.html)`. Functor pages are in `docs/functors/`, type pages in `docs/types/`, and the graphical interface pages in `docs/gui/`; the other pages are in `docs/`. Each page starts with a front matter block (`title`, plus `nav_order` or `nav_exclude`), and its content is wrapped in `{% raw %}` / `{% endraw %}` so that EGO Script's `{{` and `{%` are not interpreted by Liquid.

## License

[MIT](LICENSE) © Centro de Sensoriamento Remoto / UFMG
