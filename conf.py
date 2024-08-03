# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# -- ABlog ---------------------------------------------------

blog_baseurl = "https://adriaan90.github.io/"
blog_title = "Adriaan's Blog"
blog_path = "blog"
blog_post_pattern = "blog/*/*"
blog_feed_fulltext = True
blog_feed_subtitle = ""
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

project = "Adriaan's Blog"
copyright = '2024, Adriaan van Niekerk'
author = 'Adriaan van Niekerk'
release = ""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
"ablog",
"sphinx.ext.intersphinx",
"sphinx_panels",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "logo": {
        # In a left-to-right context, screen readers will read the alt text
        # first, then the text, so this example will be read as "P-G-G-P-Y
        # (short pause) Home A pretty good geometry package"
        "text": "Adriaan's Blog"
    }
}

html_static_path = ['_static']

def setup(app):
    app.add_css_file("custom.css")

html_sidebars = {
    "index": ["aboutme.html"],
    "about": ["aboutme.html"],
    "blog": ["ablog/tagcloud.html", "ablog/archives.html"],
    "blog/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
}
