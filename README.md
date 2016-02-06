# notepad

I have spent near more two weeks to write this Notepad application. At this moment, I want to share with you.

I wonder that do you know the Notepad in Windows XP/7. If you have no idea, I am pleasure to display the Notepad 

in Windows 7 with you, and it displays as below:
![Example](https://github.com/Hongten/notepad/blob/master/image/windows_notepad_panel.png)

It has large future and simple interface, so does my Notepad!

Well, I will introduce my Notepad.

First, Let's look at the structure of the my Notepad application:

![Example](https://github.com/Hongten/notepad/blob/master/image/structure.png)

# How to add substance to your project build path?

NOTE:
Your computer should install the Maven(apache-maven-3.2.2 is good choice) before running this project!

There are TWO ways to provided.

1. Using eclipse tool to add the substance-1.0.jar to project build path.

  1.1.Finding the substance-1.0.jar with the path "[notepad/lib/skin/substance-1.0.jar](https://github.com/Hongten/notepad/blob/master/lib/skin/substance-1.0.jar)".
	
    Right Click --> Build Path --> Add to Build Path.

  1.2.Then open the opm.xml(with the path "[notepad/pom.xml](https://github.com/Hongten/notepad/blob/master/pom.xml)")
  
    Deleting the substance dependency:
```xml
<dependency>
  <artifactId>substance</artifactId>
  <artifactId>substance</artifactId>
  <version>1.0</version>
</dependency>
```
  
2. Copy the substance-1.0.jar to your repository.
	2.1.Finding the substance-1.0.jar with the path "[notepad/lib/skin/substance-1.0.jar](https://github.com/Hongten/notepad/blob/master/lib/skin/substance-1.0.jar)".
	
	Copying the substance-1.0.jar file to your repository.
	
	The default path of the repository is "${user.home}/.m2/repository/org/jvnet/substance/substance/1.0/substance-1.0.jar"

# How to run notepad project?

Using the eclipse tool and finding the Client.java file with the path 

"notepad/src/main/java/com/b510/notepad/client/[Client.java](https://github.com/Hongten/notepad/blob/master/src/main/java/com/b510/notepad/client/Client.java)".

Right Click --> Run As --> Java Application



-----------------------------------------------------
# The Notepad Main UI

![Example](https://github.com/Hongten/notepad/blob/master/image/main_panel.png)

# File Menu

![Example](https://github.com/Hongten/notepad/blob/master/image/file_menu_panel.png)

# Edit Menu

![Example](https://github.com/Hongten/notepad/blob/master/image/edit_menu_panel.png)

# Format Menu

![Example](https://github.com/Hongten/notepad/blob/master/image/format_menu_panel.png)

# View Menu

![Example](https://github.com/Hongten/notepad/blob/master/image/view_menu_panel.png)

# Time Menu

![Example](https://github.com/Hongten/notepad/blob/master/image/time.png)

# Open File

![Example](https://github.com/Hongten/notepad/blob/master/image/open_file_panel.png)

# About

![Example](https://github.com/Hongten/notepad/blob/master/image/about_panel.png)

# Change Skin

![Example](https://github.com/Hongten/notepad/blob/master/image/change_skin_panel.png)

# Describe for all files

**Client.java** --> The entry of the notepad application. It contains the main method.

**Common.java** --> All constants in here.

**AboutUI.java** --> About notepad page.

**FindManagerUI.java** --> Find page.

**FontManagerUI.java** --> Font setting page.

**FontSizeManagerUI.java** --> Font sizt setting page.

**UI.java** --> The parent class for the NotepadUI, It extends JFrame.

**MainUI.java** --> The main page of the notepad.

**NotepadUI.java** --> The parent class for the MainUI, It extends JUI and implements ActionListener.

**ReplaceManagerUI.java** --> Replace page. 

**SkinManagerUI.java** --> Skin setting page.

**EditMenuUtil.java** --> Edit menu functions provider.

**FileMenuUtil.java** --> File menu functions provider.

**FormatMenuUtil.java** --> Format menu functions provider.

**HelpMenuUtil.java** --> Help menu functions provider.

**NotepadUtil.java** --> Common functions provider.

**ViewMenuUtil.java** --> View menu functions provider.

**log4j.properties** --> A properties for the log4j.

**substance-1.0.jar** --> substance dependency.

**pom.xml** --> pom.xml

# More Information

* Author            : Hongten
* E-mail            : [hongtenzone@foxmail.com](mailto:hongtenzone@foxmail.com)
* Home Page         : [http://www.cnblogs.com/hongten](http://www.cnblogs.com/hongten)
* Refer Skin Page   : [http://www.cnblogs.com/hongten/p/hongten_notepad_substance_skins.html](http://www.cnblogs.com/hongten/p/hongten_notepad_substance_skins.html)
* Substance URL     : [https://substance.dev.java.net/](https://substance.dev.java.net/)
