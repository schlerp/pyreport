# pyreport

This is a python module for creating a $\LaTeX$ report structure with python.

## Installation

Clone this repository and cd into the folder then run the following:

```bash
pip install .
```

## Usage

You must create a project using this tool, edit the `config.yml` file, then update the project using this tool. The update step will create the actual tex file and section files in the report directory.

### Create project
create a new project by running the following and answering the prompts

```bash
python -m pyreport 
```

### Update project

Once a project has been created, cd into the project directory. Update the `config.yml` file with desired settings then run the following. There is a brief description at the top of the `config.yml` file that explains what the configuration settings do.

```bash
python -m pyreport update
```

This will parse the config file and set up the rest of the project. Edit the section files with the text of your report. 

### Compiling report

The report directory will contain a standard $\LaTeX$ report which can be compiled using your favourite latex compiler.

## Disclaimer

This is not intended to allow an complete novice to produce a latex report. This software intends to automate some of the initial boilerplate code and set up that is required. The user still needs a moderate knowlege of $\LaTeX$ to finish the report
