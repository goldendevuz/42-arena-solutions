# Notion-mkdocs

`notion-mkdocs` is a Python package that allows you to convert Notion pages into Markdown files and then build a static site using MkDocs. This tool streamlines the process of turning your Notion content into a well-structured, easily navigable documentation site.

## Features

- **Export Notion pages to Markdown**: Convert your Notion pages into Markdown format.
- **MkDocs integration**: Seamlessly integrate with MkDocs to generate static documentation sites.
- **Automatic Table of Contents**: Generate a table of contents for your documentation.
- **Customizable templates**: Customize the output using MkDocs templates.

## Installation

To install the package, you can use pip:

```bash
pip install notion-mkdocs
```

## Usage
Configuration
Before using notion-mkdocs, you need to configure it with your Notion API token and the ID of the Notion page you want to export. You can do this by creating a configuration file config.yml:

```yaml
notion:
  token: YOUR_NOTION_API_TOKEN
  page_id: YOUR_NOTION_PAGE_ID

mkdocs:
  site_name: Your Site Name
  nav:
    - Home: index.md
    - Section:
        - Page 1: page1.md
        - Page 2: page2.md
  theme:
    name: material
```

## Exporting Notion Pages
To export your Notion pages, run the following command:


```shell
notion-mkdocs export
```
This command will fetch the content from Notion and convert it into Markdown files, which will be placed in the docs/ directory.

Building the Documentation Site
After exporting the Notion pages, you can build your MkDocs site:


```shell
mkdocs build
```
This will generate a static site in the site/ directory.

## Serving the Documentation Site
To serve the documentation site locally and view it in your browser, run:

```shell
mkdocs serve
```
This command will start a local server at http://127.0.0.1:8000 where you can view your documentation.

## Advanced Usage
Custom Templates
You can customize the look and feel of your documentation site by modifying the MkDocs templates. Refer to the MkDocs documentation for more details.

## Additional Configuration Options
You can specify additional configuration options in the config.yml file to further customize the behavior of notion-mkdocs and MkDocs. Refer to the MkDocs configuration documentation for more options.

## Troubleshooting
If you encounter any issues, make sure your Notion API token and page ID are correct. Check the console output for any error messages and refer to the Notion API documentation for more details.

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request on the GitHub repository.

## License
notion-mkdocs is licensed under the MIT License. See the LICENSE file for more details.

With notion-mkdocs, you can easily turn your Notion pages into beautiful, \
static documentation sites powered by MkDocs. Happy documenting!
