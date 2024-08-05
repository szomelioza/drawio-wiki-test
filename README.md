# drawio-wiki-test

In order to perform below steps there is need to install draw.io integration in GitHub.

Create new diagram:
1. Open draw.io.
2. Change storage to GitHub.
3. Select Create New Diagram.
4. Change name for diagram and type of file to "Editable Bitmap Image". Select Create.
5. Authorize to GitHub.
6. If integration is installed select repo in which diagram will be saved.
7. Create diagram and add commit message.
8. Open GitHub Wiki and reference image using:
`![<alternative_description>](../blob/<branch>/<file_name>?raw=true)` (for non-linked diagram) or `[![<alternative_description>](../blob/<branch>/<file_name>?raw=true)](https://app.diagrams.net/#H<username/org>%2F<repo_name>%2F<branch>%2F<file_name>)` (for linked diagram).

Edit existing diagram:
1. Open draw.io.
2. Change storage to GitHub.
3. Select Open Existing Diagram.
4. Select repo and file to edit.
5. Make changes and save them (commit).
6. Changes will be reflected in GitHub Wiki page after couple of minutes.
