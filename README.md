# gemtext-html-converter
A Python script that converts text/gemini into HTML.

A simple script that converts gemtext to HTML. Takes two arguments from stdin -
args[1](gmi) is an input gemtext file and args[2](html) is an output HTML file. 
The output file consists of only the lines of gemtext in the input file converted
to their HTML equivalents: h1, h2, h3, p, a, blockquote, li, and 
pre tags. It does not include any boilerplate such as a default head
or wrapping html or body tags. I wrote it mainly so I could insert converted
gemtext into a webpage I already started using copy-paste or a templating system
like Jinja. Extend it as you see fit.

You can run it like so:

python3 path-to-input-file.gmi path-to-output-file.html
