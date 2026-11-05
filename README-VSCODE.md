
# Customizing VS Code for This Project

## Syntax Highlighting for Style Files

To enable syntax highlighting for style definition files (`.sty.txt`), install
the **Highlight** extension by Fabio Spampinato and add the following configuration
to the `settings.json` file in the project's `.vscode` directory:

```json
{
    "highlight.enabled"   : true,
    "highlight.regexFlags": "gm", // <- 'g' para global, 'm' para habilitar el uso de ^ por línea
    "highlight.regexes"   :
    {
        "(^>##.*$)": {
            "filterFileRegex": "\\.sty\\.txt$",
            "decorations": [
                {
                    "color": "#68d473",
                    "fontStyle": "italic"
                }
            ]
        },
        "(^>>>.+$)": {
            "filterFileRegex": "\\.sty\\.txt$",
            "decorations": [
                {
                    "fontWeight": "bold",
                    "color"          : "#FF7F50",
                    "backgroundColor": "#1a2a3a"
                }
            ]
        },
        "(\\{\\$)([a-zA-Z0-9.@*#+\\-]+)([\\s\\S]*?)([|])([\\s\\S]*?)([}])": {
            "filterFileRegex": "\\.sty\\.txt$",
            "decorations": [
                { "color": "#e858d7", "fontWeight": "bold" },
                { "color": "#70C8FF", "fontWeight": "bold" },
                { "color": "#6294C7" },
                { "color": "#e858d7", "fontWeight": "bold" },
                { "color": "#966060" },
                { "color": "#e858d7", "fontWeight": "bold" }
            ]
        },
        "(\\{\\$)([a-zA-Z0-9.@*#+\\-]+)([^|]*?)([}])": {
            "filterFileRegex": "\\.sty\\.txt$",
            "decorations": [
                { "color": "#e858d7", "fontWeight": "bold" },
                { "color": "#70C8FF", "fontWeight": "bold" },
                { "color": "#6294C7" },
                { "color": "#e858d7", "fontWeight": "bold" },
            ]
        },
        "^(\\{-----)(COMMENT)\n^([\\s\\S]*?)\n(-----\\})\n": {
            "filterFileRegex": "\\.sty\\.txt$",
            "decorations": [
                {"color": "#333333" },
                {"color": "#888888", "fontWeight": "bold"  },
                {"color": "#666666", "fontStyle": "italic" },
                {"color": "#333333" }
            ]
        },
        "^(\\{-----)\n^[\\s\\S]*?\n^(------)\n^[\\s\\S]*?\n^(------)\n^[\\s\\S]*?\n^(-----\\})": {
            "filterFileRegex": "\\.sty\\.txt$",
            "decorations": [
                { "color": "#FFD700", "fontWeight": "bold" },
                { "color": "#FFD700", "fontWeight": "bold" },
                { "color": "#FFD700", "fontWeight": "bold" },
                { "color": "#FFD700", "fontWeight": "bold" },
            ]
        }
    }

}
```
