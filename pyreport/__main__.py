import os
import yaml
import sys

from . import templating
from . import constants


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def create_section():
    pass


def create_project():
    # get the project folder
    project_folder_default = "./"
    project_folder = (
        input(f"Project folder [{project_folder_default}] >>>")
        or project_folder_default
    )

    print("All settings can be configured via config.yml")

    # create project folder
    if project_folder != project_folder_default:
        create_dir(project_folder)

    # create the report subdirs
    report_dir = os.path.join(project_folder, "report")
    create_dir(report_dir)
    create_dir(os.path.join(report_dir, "images"))
    create_dir(os.path.join(report_dir, "tables"))

    # create the output subdir
    output_dir = os.path.join(project_folder, "output")
    create_dir(output_dir)

    # create the template
    template_dir = os.path.join(project_folder, "templates")
    create_dir(template_dir)

    # copy template
    with open(os.path.join(template_dir, "template.tex"), "w+") as f:
        f.write(constants.template_text)

    # set up config file
    with open(os.path.join(project_folder, "config.yml"), "w+") as f:
        f.write(constants.config_desc)
        f.write(yaml.dump(constants.default_config))


def update_report(
    template_name="template.tex",
    template_dir="./templates",
    output_file="report/report.tex",
):
    with open("./config.yml", "r") as f:
        context = yaml.load(f)

    # set up templating engine
    jinja_env = templating.create_jinja_latex_env(template_dir)

    # fill template
    filled_template = templating.fill_template(
        context, jinja_env, template_name=template_name
    )

    # write template
    with open(output_file, "w+") as f:
        f.write(filled_template)


def _test(
    template_name="root.tex", template_dir="pyreport/templates", output_file="test.tex"
):

    # set up templating engine
    jinja_env = templating.create_jinja_latex_env(template_dir)

    # fill template
    filled_template = templating.fill_template(constants.default_config, jinja_env)

    # write template
    with open(output_file, "w+") as f:
        f.write(filled_template)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        create_project()
    elif sys.argv[1] == "create":
        create_project()
    elif sys.argv[1] == "update":
        update_report()
