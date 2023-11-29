This vault already take effect on all these changes, but the below is my setup (vary from the default setting)

- Editor:
	- Spellcheck: ON
- Files and links:
	- Automatically update internal links: ON
	- Default location for new notes: In the folder specified below, "NewNotes"
	- Default location for new attachments: In the folder specified below, "Attachements"
- Hotkey:
	- Template: insert template: Ctrl + T
- Core plugin:
	- Template: Template folder location: Template_sheet, DD-MM-YYYY, HH:mm
	- Random note: On
- Community plugin:
	- Collapse ALL
	- Extended MathJax
	- Pandoc Plugin: Export markdown to doc, pdf etc. 
	- TikZJax: which allows showing LaTeX graph with (3dots-tikz). Go to enable it on settings. 
	- Vault Changelog
		- Changelog location: `Changelog/changelog.md`, 
		- Number of recent files: `1000`, 
		- Autoupdate: Yes
- CSS snippets
	- Add a `max_depth.css` snippet in `vault/.obsidian/snippets` folder, which controls the depth of the embedded notes. 
	- Enable the snippets on Setting > Appearance > Final node.

- max_depth.css:
```css
.markdown-embed-content {
    max-height: 500px;
  }
```