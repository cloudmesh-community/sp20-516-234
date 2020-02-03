# How do you activate the virtual env in your OS?

Using a Mac OS to activate a python virtual env manually you must first create the path to virtual env using 

`python -m venv /path/path1/path2`

Once that is created the command to launch your virtual environment is `source`. You must point your command to the 
`activate` binary generated in your virtual environment. 

`source /<venv path>/activate`

# How do you modify your .bashrc file so that the python venv is loaded automatically upon the start of a new terminal?

Modifying your `.bashrc` to launch your virtual environment automatically takes a single line change. The `.bashrc` file
applies profile configurations to sub-terminals only, so it important to first modify your `.bash_profile` file to 
automatically load the scripts from the `.bashrc` file. That can be done by writing a three line logic statement to check
if the `.bashrc` file exists on startup of your login terminal and read from it on startup.

```
if [ -f ~/.bashrc ]; then
	source ~/.bashrc
fi
```

Once that logic is set up, you can input the single like that points the source command directly at the venv `activate` 
binary.

`source /Users/andrewgoldfarb/e516-spring/ENV3/bin/activate`

# In case you use zsh, either switch to bash or describe how do you modify zsh so that the python venv is loaded.

# Why do you need to use venv for this class? Provide a one-paragraph answer in your notebook.md file.”

Please see [notebook.md file](./notebook.md)
