import subprocess
from zerver.lib.str_utils import force_bytes
from typing import Text

def render_tex(tex, is_inline=True):
    # type: (Text, bool) -> Text
    """Render a TeX string into HTML using KaTeX

    Returns the HTML string, or None if there was some error in the TeX syntax

    Keyword arguments:
    tex -- Text string with the TeX to render
           Don't include delimiters ('$$', '\[ \]', etc.)
    is_inline -- Boolean setting that indicates whether the render should be
                 inline (i.e. for embedding it in text) or not. The latter
                 will show the content centered, and in the "expanded" form
                 (default True)
    """
    command = ['npm', 'run', '-s', 'katex']
    if not is_inline:
        command.extend(['--', '--display-mode'])
    katex = subprocess.Popen(command,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)
    stdout = katex.communicate(input=force_bytes(tex))[0]
    if katex.returncode == 0:
        return stdout
    else:
        return None
