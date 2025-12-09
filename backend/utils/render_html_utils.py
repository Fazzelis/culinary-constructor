from jinja2 import Template


def render_html_template(dish: dict):
    with open("templates/template.html", "r", encoding="utf-8") as f:
        template_content = f.read()
    template = Template(template_content)
    html_content = template.render(dish=dish)

    return html_content
