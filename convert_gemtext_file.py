"""
A simple script that converts gemtext to HTML. Takes two arguments from stdin -
args[1](gmi) is an input gemtext file and args[2](html) is an output HTML file. 
The output file consists of only the lines of gemtext in the input file converted
to their HTML equivalents: <h1>, <h2>, <h3>, <p>, <a>, <blockquote>, <li>, and 
<pre> tags. It does not include any boilerplate such as a default <head>
or wrapping <html> or <body> tags. I wrote it mainly so I could insert converted
gemtext into a webpage I already started using copy-paste or a templating system
like Jinja. Extend it as you see fit.

If you have any suggestions on how to make it better you can reach me at
hunterkb@ksu.edu
"""

# importing required libraries
import sys
import re

# A dictionary that maps regex to match at the beginning of gmi lines to their corresponding HTML tag names. Used by convert_single_line().
tags_dict = {
    r"^# (.*)": "h1",
    r"^## (.*)": "h2",
    r"^### (.*)": "h3",
    r"^\* (.*)": "li",
    r"^> (.*)": "blockquote",
    r"^=>\s*(\S+)(\s+.*)?": "a"
}

# This function takes a string of gemtext as input and returns a string of HTML
def convert_single_line(gmi_line):
    for pattern in tags_dict.keys():
        if match := re.match(pattern, gmi_line):
            tag = tags_dict[pattern]
            groups = match.groups()
            if tag == "a":
                href = groups[0]
                inner_text = groups[1].strip() if len(groups) > 1 else href
                return f"<{tag} href='{href}'>{inner_text}</{tag}>"
            else:
                inner_text = groups[0].strip()
                return f"<{tag}>{inner_text}</{tag}>"
    return f"<p>{gmi_line.strip()}</p>"
            
# Reads the contents of the input file line by line and outputs HTML. Renders text in preformat blocks (toggled by ```) as multiline <pre> tags.
def main(args):
    with open(args[1]) as gmi, open(args[2], "w") as html:
        preformat = False
        for line in gmi:
            line = line.strip()
            if len(line):
                if line.startswith("```") or line.endswith("```"):
                    preformat = not preformat
                    repl = "<pre>" if preformat else "</pre>"
                    html.write(re.sub(r"```", repl, line))
                    html.write("\n")
                    continue
                if preformat:
                    html.write(line)
                    html.write("\n")
                    continue
                else:
                    html_line = convert_single_line(line)
                    html.write(html_line)
                    html.write("\n")

# Main guard
if __name__ == "__main__":
    main(sys.argv)
