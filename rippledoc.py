#!/usr/bin/env python3

# Copyright 2018 John Gabriele <jgabriele@fastmail.fm>
#           2022 Franklin Bristow <fbristow@gmail.com>
#
# This file constitutes the Rippledoc program.
#
# Rippledoc is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# Rippledoc is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Rippledoc.  If not, see <http://www.gnu.org/licenses/>."

import os, os.path, sys, subprocess, io, re, shutil
import panflute as pf

VERSION = "2022-12-15"

project_name = None
copyright_info = None

dirs_to_skip = []
fnm_to_doc_title = {}

# Needed for ToC in nav box.
full_ordered_list_of_paths = []

# Needed for for prev/next links.
full_ordered_list_of_fnms = []

using_readme_as_index = False

usage_msg = """\
You run this program in the root (top-level) of your
documentation directory to generate easily-navigable HTML files
from your (pandoc-)markdown-formatted doc files. For more info,
see the docs this program came with, or else its docs online at
<http://www.unexpected-vortices.com/sw/rippledoc/index.html>.

Usage:

    rippledoc.py

    rippledoc.py --readme-is-index  # Will copy ../README.md to
                                    # ./index.md. Any existing
                                    # ./index.md will be over-
                                    # written.

To remove all traces of this program having been used in your docs
directory, delete:

  * all toc.conf files
  * the styles.css and _copyright files
  * all generated .html files
  * if you used `--readme-is-index`, the copied-in ./index.md file
    as well.

Exiting.
"""

available_options = ["--readme-is-index"]

def main():
    print(f"================ Rippledoc, version {VERSION} ================")

    if len(sys.argv) > 1 and (sys.argv[1] not in available_options):
        print(usage_msg)
        sys.exit(0)

    if not os.path.exists("_copyright"):
        print(mlsl("""\
        [**] Unable to find a "_copyright" file here. Please make
        [**] sure you're running this program in the root (top-level)
        [**] of your doc directory, and that there's a _copyright file
        [**] present here. This file typically contains something like:
        [**]
        [**]     Copyright 2016–2018 Your Name
        [**]
        [**] (including raw HTML is ok too). Exiting.
        """))
        sys.exit(0)

    if os.path.exists("README.md"):
        print(mlsl("""\
        [**] Odd. Found a README.md file in this doc directory. Maybe you
        [**] meant to place it in the directory above this one (your main
        [**] project directory), or maybe you meant to name it "index.md"
        [**] instead? Please check it out. Exiting."""))
        sys.exit(0)

    global using_readme_as_index
    if len(sys.argv) == 2 and sys.argv[1] == '--readme-is-index':
        using_readme_as_index = True

    if using_readme_as_index and (not os.path.exists("../README.md")):
        print(mlsl("""\
        [**] You've opted to use ../README.md in place of a ./index.md file,
        [**] but there doesn't appear to be a ../README.md file present.
        [**] Exiting.
        """))
        sys.exit(0)

    # We already found a _copyright file here, so we know we're in the
    # top level of the doc dir.
    if (not using_readme_as_index) and (not os.path.exists("./index.md")):
        print(mlsl("""\
        [**] Unable to find an "index.md" file here. You either need one
        [**] present, or else must have a ../README.md file present and
        [**] pass `--readme-is-index` (which will cause Rippledoc to copy
        [**] it here as ./index.md). Exiting.
        """))
        sys.exit(0)

    # In case you previously ran with `--readme-is-index`, and we copied
    # the ../README.md to ./index.md, but then you forgot to pass
    # `--readme-is-index` on a subsequent run.
    if (not using_readme_as_index) and os.path.exists("../README.md") and \
       os.path.exists("./index.md"):
        res = input(mlsl("""\
        [?] Found a ../README.md file, as well as an ./index.md file,
        [?] and also noticed that you didn't pass the `--readme-is-index`
        [?] option. Continue, using ./index.md? y/n: """))
        if res == 'y':
            print("Ok, proceeding...")
            pass
        elif res == 'n':
            print("Ok, exiting.")
            sys.exit(0)
        else:
            print("I didn't understand your reply. Exiting.")
            sys.exit(0)

    print("Checking file and directory names for weirdness...")
    check_file_and_dir_names()

    if using_readme_as_index:
        print("As requested, copying ../README.md → ./index.md...")
        shutil.copy("../README.md", "./index.md")

    global project_name
    project_name = get_title_from('./index.md')
    print(f"""Generating docs for "{project_name}" ...""")

    global copyright_info
    copyright_info = io.open("_copyright").read().strip()

    if not os.path.exists("styles.css"):
        print("""Didn't find a styles.css file here. Creating one...""")
        with io.open("styles.css", "w") as sty_file:
            sty_file.write(styles_default_css_content)

    print("Noting any dirs to skip (i.e., those with no .md files in or below them)...")
    # These may be dirs containing only image files or what have you.
    populate_dirs_to_skip(".")
    if dirs_to_skip:
        for dir_to_skip in dirs_to_skip:
            print(f"  * Will skip {dir_to_skip}.")

    # full filename --> doc title (from first line of md file)
    print("Recording each md file's doc title...")
    populate_fnm_to_doc_title()

    print("Checking toc.conf files...")
    process_dirs_create_toc_conf_files()

    print("Reading in all toc.conf data...")
    populate_full_ordered_list_of_paths('.')

    global full_ordered_list_of_fnms
    full_ordered_list_of_fnms = \
        [pth for pth in full_ordered_list_of_paths if pth.endswith(".md")]

    print("Transmogrifying .md files into html files...")
    process_all_md_files()

    print("Done.")


# ================================================================
def mlsl(s):
    """Multi-Line Strip Left. Strips off number of spaces of
    the first line of `s` (which is a multi-line string)."""
    lines = s.splitlines()
    spaces_to_remove = len(lines[0]) - len(lines[0].lstrip())
    out = []
    for line in lines:
        out.append(
            line.replace(' ' * spaces_to_remove, '', 1))
    return "\n".join(out)


def check_file_and_dir_names():
    r1 = re.compile(r'[\w\./-]+$')
    msg = mlsl("""\
    [**] Should only contain letters, numbers, underscores, and
    [**] dashes (no spaces). Please have a look. Exiting.
    """)
    for (this_dir, dirs_here, files_here) in os.walk('.'):
        if not r1.match(this_dir):
            print(mlsl(f"""\
            [**] Don't like the look of the dir name "{this_dir}".
            {msg}
            """))
            sys.exit()
        for d in dirs_here:
            if not r1.match(d):
                print(mlsl(f"""\
                [**] Don't like the look of the dir name "{os.path.join(this_dir, d)}."
                {msg}
                """))
                sys.exit()
        for fnm in files_here:
            if not r1.match(fnm):
                print(mlsl(f"""\
                [**] Don't like the look of the file name "{os.path.join(this_dir, fnm)}".
                {msg}
                """))
                sys.exit()


def populate_dirs_to_skip(path):
    """If there are any md files here or below, we need to dig deeper
    and keep looking for subdirs that may have no md files below them."""
    if is_any_mds_here_or_below(path):
        for p in list_dirs_here(path):
            populate_dirs_to_skip(p)
    else:
        dirs_to_skip.append(path)


def is_any_mds_here_or_below(path):
    for (this_dir, dirs_here, files_here) in os.walk(path):
        for fnm in files_here:
            if fnm.endswith('.md'):
                return True
    return False


def list_dirs_here(pth):
    """Returns full path names."""
    res = []
    for p in os.listdir(pth):
        full_path = os.path.join(pth, p)
        if os.path.isdir(full_path):
            res.append(full_path)
    return res


def populate_fnm_to_doc_title():
    for (this_dir, dirs_here, files_here) in os.walk('.'):
        for fnm in [f for f in files_here if f.endswith('.md')]:
            full_fnm = os.path.join(this_dir, fnm)
            title = get_title_from(full_fnm)
            fnm_to_doc_title[full_fnm] = title


def get_title_from(fnm):
    title = ''
    if fnm == './index.md' and using_readme_as_index:
        fnm = '../README.md' # For potential error message below.
    with open (fnm) as markdown:
        doc = pf.convert_text(markdown.read(), standalone=True)
        try:
            title = doc.get_metadata('title')
        except:
            title = ''
    return title


def process_dirs_create_toc_conf_files():
    for (this_dir, dirs_here, files_here) in os.walk('.'):
        toc_fnm = os.path.join(this_dir, 'toc.conf')
        md_fnms = [fnm for fnm in files_here if fnm.endswith('.md')]
        if 'toc.md' in md_fnms:
            md_fnms.remove('toc.md')
        if this_dir == '.':
            md_fnms.remove('index.md')
        dirs_here_for_toc = [
            d for d in dirs_here if os.path.join(this_dir, d) not in dirs_to_skip
        ]
        if is_at_or_under_skipped_dir(this_dir):
            if os.path.exists(toc_fnm):
                print(f"  * Found a derelict toc.conf file in {this_dir}. Removing it.")
                os.remove(toc_fnm)
            continue
        if os.path.exists(toc_fnm):
            # Check that its contents match what's actually here.
            toc_conf_content = io.open(
                os.path.join(this_dir, 'toc.conf')).read().strip().splitlines()
            s_toc = set(toc_conf_content)
            s_found = set(md_fnms + dirs_here_for_toc)
            s_extra = s_found - s_toc
            if s_extra:
                print(f'''In {this_dir}, items were found that were absent from {toc_fnm}:''')
                for item in s_extra:
                    print(f'  * Adding {item} to the toc.conf.')
                with io.open(toc_fnm, 'a') as f:
                    f.write('\n'.join(list(s_extra)) + '\n')
            s_extra = s_toc - s_found
            if s_extra:
                print(f'''[**] {toc_fnm} contains items that aren't in {this_dir}:''')
                for item in s_extra:
                    print(f'[**]   * {item}')
                print(f'''[**] Please rectify. Exiting.\n''')
                sys.exit()
        else:
            print(f'''  * Didn't find "{toc_fnm}". Creating it ...''')
            with io.open(toc_fnm, 'w') as f:
                f.write('\n'.join(md_fnms + dirs_here_for_toc))
                f.write('\n')


def is_at_or_under_skipped_dir(tgt):
    """Checks if the target dir `tgt` is the same as or under any
    of the dirs in `dirs_to_skip`."""
    for d in dirs_to_skip:
        if d in tgt:
            return True
    return False


def populate_full_ordered_list_of_paths(path):
    """`path` is a directory name, typically started off like
    `populate_full_ordered_list_of_fnms('.')`. We call this function
    after all toc.conf files have been created/checked, so we assume
    `path` is a good one (with a toc.conf file in it)."""
    if path == '.':
        full_ordered_list_of_paths.append('./index.md')
    with io.open(os.path.join(path, 'toc.conf')) as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            line = os.path.join(path, line)
            full_ordered_list_of_paths.append(line)
            if not line.endswith('.md'):
                populate_full_ordered_list_of_paths(line)


def process_all_md_files():
    for (this_dir, dirs_here, files_here) in os.walk('.'):
        md_fnms = [f for f in files_here if f.endswith('.md')]
        for md_fnm in md_fnms:
            pandoc_process_file(os.path.join(this_dir, md_fnm))


def pandoc_process_file(md_fnm):
    html_fnm = md_fnm[:-2] + 'html'

    # Get the header and footer files ready, for this particular md_fnm.
    depth = md_fnm.count('/') - 1

    html_bef = html_before.replace('{{path-to-index}}', '../' * depth + 'index.html')
    html_bef = html_bef.replace('{{project-name}}', project_name)

    nav_box_content = get_nav_box_content(md_fnm)
    html_bef = html_bef.replace("{{nav-box-content}}", nav_box_content)

    nav_bar_content = get_nav_bar_content(md_fnm)
    html_bef = html_bef.replace('{{nav-bar-content}}', nav_bar_content)

    html_aft = html_after.replace('{{nav-bar-content}}', nav_bar_content)
    html_aft = html_aft.replace('{{copyright-info}}', copyright_info)
    html_aft = html_aft.replace('{{link-to-this-page-md}}', os.path.basename(md_fnm))

    io.open('/tmp/before.html', 'w').write(html_bef)
    io.open('/tmp/after.html' , 'w').write(html_aft)

    pandoc_cmd = ['pandoc', md_fnm]
    pandoc_cmd.extend(['-f', 'markdown+smart', '-s'])
    pandoc_cmd.append(
        '--mathjax=https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/latest.js?config=TeX-AMS_CHTML-full')
    if md_fnm != './index.md':
        pandoc_cmd.append('--toc')
    depth = md_fnm.count('/') - 1
    pandoc_cmd.append('--css=' + '../' * depth + 'styles.css')
    pandoc_cmd.extend(['-B', '/tmp/before.html', '-A', '/tmp/after.html'])
    pandoc_cmd.extend(['-o', html_fnm])
    subprocess.check_call(pandoc_cmd)


def get_nav_box_content(md_fnm):
    """Produces a full ToC, flush with links except for the entry for
    `md_fnm`."""
    nav_toc_md_fnm =   "/tmp/nav-toc.md"
    nav_toc_html_fnm = "/tmp/nav-toc.html"

    with io.open(nav_toc_md_fnm, "w") as f:
        f.write("Contents:\n\n")
        f.write("\n".join(make_toc_md_list_for(md_fnm)))
        f.write("\n")

    pandoc_cmd = ["pandoc", "/tmp/nav-toc.md", "-o", nav_toc_html_fnm]
    subprocess.check_call(pandoc_cmd)
    content = io.open(nav_toc_html_fnm).read()
    return content


def make_toc_md_list_for(md_fnm):
    res = []
    for fnm in full_ordered_list_of_paths:
        if fnm == "./index.md":
            continue

        depth = fnm.count("/") - 1
        indent = "    " * depth
        is_a_dir = not fnm.endswith(".md")

        if is_a_dir:
            try:
                with open(f"{fnm}/meta.yml") as meta:
                    dir_title = pf.convert_text(meta.read(), standalone=True)
                    title = dir_title.get_metadata('title')
            except:
                title = os.path.basename(fnm) + "/"
        else:
            title = fnm_to_doc_title[fnm]
            html_fnm = fnm[:-2] + "html"
            html_link = get_rel_path_from_to(md_fnm, html_fnm)

        if fnm == md_fnm:
            res.append(f"{indent}  * __{title}__")
        else:
            if is_a_dir:
                res.append(f"{indent}  * {title}")
            else:
                res.append(f"{indent}  * [{title}]({html_link})")
    return res


def get_nav_bar_content(md_fnm):
    prv, nxt = make_prev_next_links(md_fnm)
    nav_bar = f"""<div>{prv}</div><div class="nav-bar-push">{nxt}</div>"""
    return nav_bar


def make_prev_next_links(md_fnm):
    idx = None
    prev_text, next_text = '←prev', 'next→'
    prev_link, next_link = prev_text, next_text
    if not md_fnm.endswith('/toc.md'):
        idx = full_ordered_list_of_fnms.index(md_fnm)
        if idx > 0:
            md_fnm_prev = full_ordered_list_of_fnms[idx - 1]
            rel_path_md = get_rel_path_from_to(md_fnm, md_fnm_prev)
            rel_path_html = rel_path_md[:-2] + 'html'
            prev_link = f"""<a href="{rel_path_html}">{prev_text}</a>"""
        if idx < len(full_ordered_list_of_fnms) - 1:
            md_fnm_next = full_ordered_list_of_fnms[idx + 1]
            rel_path_md = get_rel_path_from_to(md_fnm, md_fnm_next)
            rel_path_html = rel_path_md[:-2] + 'html'
            next_link = f"""<a href="{rel_path_html}">{next_text}</a>"""
    return prev_link, next_link


def get_rel_path_from_to(fr, to):
    if os.path.dirname(fr) == os.path.dirname(to):
        return os.path.basename(to)
    else:
        depth = fr.count('/') - 1
        return '../' * depth + to


html_before = """
<div id="main-outer-box">

<div id="my-header">
  <a href="{{path-to-index}}">{{project-name}}</a>
</div>

<div id="trunk-box">

<div id="nav-box">
{{nav-box-content}}
</div>

<div id="article-box">

<div id="header-nav-bar">
{{nav-bar-content}}
</div>

<div id="article-content">
"""

# The boxes go like:
#
# body
#     #main-outer-box
#         #my-header
#         #trunk-box
#             #nav-box
#             #article-box
#                 #header-nav-bar
#                 #article-content
#                 #footer-nav-bar
#         #my-footer

html_after = """
</div> <!-- article-content -->

<div id="footer-nav-bar">
{{nav-bar-content}}
</div>

</div> <!-- article-box -->

</div> <!-- trunk-box -->

<div id="my-footer">
{{copyright-info}}<br/>
<a href="{{link-to-this-page-md}}">Pandoc-Markdown source for this page</a><br/>
(Docs processed by
<a href="http://www.unexpected-vortices.com/sw/rippledoc/index.html">Rippledoc</a>.)
</div> <!-- my-footer -->

</div> <!-- main-outer-box -->

"""

styles_default_css_content = """\
body {
    color: #222;
    line-height: 1.5;
    font-family: "Clear Sans", sans-serif;
    background-color: #fff;
}

#main-outer-box {
    /* Contains all other divs for the page. */
}

#my-header {
    font-weight: bold;
    font-size: large;
    padding: 4px 10px 10px 10px;
}

#my-header a {
    text-decoration: none;
}

#trunk-box {
    /* ... */
}

#nav-box {
    float: left;
    width: 280px;
    padding: 10px;
    font-size: small;
}

#article-box {
    margin-left: 320px;
    width: 800px;
}

#header-nav-bar, #footer-nav-bar {
    font-size: small;
    display: flex;
}

.nav-bar-push {
    margin-left: auto;
}

#header-nav-bar {
    padding: 6px 6px 8px 10px;
    border-bottom: 1px solid #ddd;
}

#article-content {
    /*padding: 20px;*/
}

/* Pandoc automatically puts title, subtitle, author, and date
   into a header elem at the top of the page. */
header .author { display: none; }
header .date   { display: none; }

/* Pandoc's doc-specific ToC. */
nav#TOC {
    background-color: #e5efdf;
    border: 1px solid #cedec4;
}

#footer-nav-bar {
    padding: 6px 6px 10px 10px;
    border-top: 1px solid #ddd;
}

caption {
    font-style: italic;
    font-size: small;
    color: #555;
}

a:link {
    color: #3A4089;
}

a:visited {
    color: #875098;
}

table {
    background-color: #eee;
    padding-left: 2px;
    border: 2px solid #d4d4d4;
    border-collapse: collapse;
}

th {
    background-color: #d4d4d4;
    padding-right: 4px;
}

tr, td, th {
    border: 2px solid #d4d4d4;
    padding-left: 4px;
    padding-right: 4px;
}

dt {
    font-weight: bold;
}

code {
    background-color: #eee;
}

pre {
    background-color: #eee;
    border: 1px solid #ddd;
    padding-left: 6px;
    padding-right: 2px;
    padding-bottom: 5px;
    padding-top: 5px;
}

blockquote {
    background-color: #d8deea;
    border: 1px solid #c6d1e7;
    border-radius: 6px;
    padding-top: 2px;
    padding-bottom: 2px;
    padding-left: 16px;
    padding-right: 16px;
}

blockquote code, blockquote pre {
    background-color: #cad2e4;
    border-style: none;
}

#my-footer {
    clear: both;
    padding: 10px;
    font-style: italic;
    font-size: x-small;
}

h1, h2, h3, h4, h5, h6 {
    color: #567EB5;
}

h3, h5 {
    font-style: italic;
}
"""

# -----------------------------------
main()
