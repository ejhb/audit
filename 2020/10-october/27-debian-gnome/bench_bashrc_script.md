Il est possible de faire des script en bashrc pour automatisé des taches ou bien manipulé un grand nombre de dossier ou fichier. C'est possible également en python, mais il peut être pratique d'être au courant pour comprendre le code de collaborateur ou en cas d'extrême nécéssité. 

Pour faire des fichier runnable : 

Disagreeing with the other answers, there's a common convention to use a .sh extension for shell scripts -- but it's not a useful convention. It's better not to use an extension at all. The advantage of being able tell that foo.sh is a shell script because of its name is minimal, and you pay for it with a loss of flexibility.

To make a bash script executable, it needs to have a shebang line at the top:

```
#!/bin/bash
```*

nd use the chmod +x command so that the system recognizes it as an executable file. It then needs to be installed in one of the directories listed in your $PATH. If the script is called foo, you can then execute it from a shell prompt by typing foo. Or if it's in the current directory (common for temporary scripts), you can type ./foo.

Neither the shell nor the operating system pays any attention to the extension part of the file name. It's just part of the name. And by not giving it a special extension, you ensure that anyone (either a user or another script) that uses it doesn't have to care how it was implemented, whether it's a shell script (sh, bash, csh, or whatever), a Perl, Python, or Awk script, or a binary executable. The system is specifically designed so that either an interpreted script or a binary executable can be invoked without knowing or caring how it's implemented.

UNIX-like systems started out with a purely textual command-line interface. GUIs like KDE and Gnome were added later. In a GUI desktop system, you can typically run a program (again, whether it's a script or a binary executable) by, for example, double-clicking on an icon that refers to it. Typically this discards any output the program might print and doesn't let you pass command-line arguments; it's much less flexible than running it from a shell prompt. But for some programs (mostly GUI clients) it can be more convenient.

Shell scripting is best learned from the command line, not from a GUI.

(Some tools do pay attention to file extensions. For example, compilers typically use the extension to determine the language the code is written in: .c for C, .cpp for c++, etc. This convention doesn't apply to executable files.)

Keep in mind that UNIX (and UNIX-like systems) are not Windows. MS Windows generally uses a file's extension to determine how to open/execute it. Binary executables need to have a .exe extension. If you have a UNIX-like shell installed under Windows, you can configure Windows to recognize a .sh extension as a shell script, and use the shell to open it; Windows doesn't have the #! convention.