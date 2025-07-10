# Manim 插件

### Rendering Scenes

##### Working with multiple scenes

After rendering a scene for the first time, the extension creates a persistent job tied to the source file to maintain your scene names and configurations.

##### Changing the Scene Name
Manim Sideview renders one scene at a time. To switch between scenes, you can:

Use the `Manim: Set A New SceneName` command through the command palette (`Shift + Command + P` on Mac / `Ctrl + Shift + P` on Windows/Linux)
Use the default hotkey Ctrl + ' followed by c
Click the render-change icon in the sideview:

##### Scene Auto-Detection
When you first render a file, the extension will scan for any class that inherits from a Scene class and present them as options for easy selection.

Action	|Windows/Linux	|Mac
---|---|---
Render current scene	|Ctrl+' r	|Ctrl+' r
Change scene name	|Ctrl+' c	|Ctrl+' c
Stop rendering	|Ctrl+' s	|Ctrl+' s
Open mobject gallery	|Via command palette	|Via command palette