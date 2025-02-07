# Static Site Generator

A Python-based static site generator that converts Markdown files to HTML, with support for various Markdown features and custom templating.

## Features

- Converts Markdown to HTML with support for:
  - Headings
  - Paragraphs
  - Bold and italic text
  - Code blocks
  - Blockquotes
  - Ordered and unordered lists
  - Links and images
- Custom HTML templating system
- Static file handling
- Recursive directory processing
- Title extraction from Markdown files

## Project Structure

```
.
├── main.py                 # Main entry point
├── block_markdown.py       # Block-level Markdown parsing
├── inline_markdown.py      # Inline Markdown parsing
├── markdown_parser.py      # Main Markdown to HTML conversion
├── htmlnode.py            # HTML node representation
├── textnode.py            # Text node representation
├── title_extractor.py     # Markdown title extraction
└── copy_static.py         # Static file handling
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd static-site-generator
```

2. No additional dependencies are required as the project uses Python standard library.

## Usage

1. Place your Markdown content in the `content` directory.
2. Add any static files (CSS, images, etc.) to the `static` directory.
3. Create your HTML template in `template.html` with placeholders:

   - Use `{{ Title }}` for the page title
   - Use `{{ Content }}` for the main content

4. Run the generator:

```bash
python main.py
```

or

```bash
./main.sh
```

The generated site will be available in the `public` directory.

## Code Examples

### Converting Markdown to HTML

```python
from markdown_parser import markdown_to_html_node

markdown = """
# Hello World

This is a paragraph with **bold** and *italic* text.

* List item 1
* List item 2
"""

html_node = markdown_to_html_node(markdown)
html = html_node.to_html()
```

### Using the Template System

Your template.html file:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{{ Title }}</title>
  </head>
  <body>
    {{ Content }}
  </body>
</html>
```

## Supported Markdown Syntax

- Headers: `# H1`, `## H2`, etc.
- Bold: `**text**`
- Italic: `*text*` or `_text_`
- Code: `` `code` ``
- Links: `[text](url)`
- Images: `![alt text](image-url)`
- Lists:
  - Unordered: `* item` or `- item`
  - Ordered: `1. item`
- Blockquotes: `> quote`
- Code blocks: ` ```code``` `

## Testing

The project includes comprehensive unit tests. Run them using:

```bash
python -m unittest discover tests
```

or

```bash
./test.sh
```

## Technical Details

### Core Components

1. **HTMLNode**: Base class for HTML element representation

   - LeafNode: For elements without children
   - ParentNode: For elements with children

2. **TextNode**: Represents different types of text content

   - Regular text
   - Bold
   - Italic
   - Code
   - Links
   - Images

3. **Markdown Parser**:
   - Block-level parsing
   - Inline parsing
   - Custom delimiter handling

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
