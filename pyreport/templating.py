import os
import jinja2

# inspired by: https://miller-blog.com/latex-with-jinja2/


def create_jinja_latex_env(
    template_dir,
    block_start_string=r"\BLOCK{",
    block_end_string=r"}",
    variable_start_string=r"\VAR{",
    variable_end_string=r"}",
    comment_start_string=r"\#{",
    comment_end_string=r"}",
    line_statement_prefix=r"%%",
    line_comment_prefix=r"%#",
    trim_blocks=True,
    autoescape=False,
):
    return jinja2.Environment(
        block_start_string=block_start_string,
        block_end_string=block_end_string,
        variable_start_string=variable_start_string,
        variable_end_string=variable_end_string,
        comment_start_string=comment_start_string,
        comment_end_string=comment_end_string,
        line_statement_prefix=line_statement_prefix,
        line_comment_prefix=line_comment_prefix,
        trim_blocks=trim_blocks,
        autoescape=autoescape,
        loader=jinja2.FileSystemLoader(template_dir),
    )


def fill_template(context, jinja_env, template_name="root.tex"):
    print(jinja_env.list_templates())
    template = jinja_env.get_template(template_name)
    return template.render(**context)
