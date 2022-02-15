class WebArticle:
    """Simple class representing a web article"""

    def __init__(self, title, lead_text, link, text=None, when_published=None,
                 title_int=None, lead_text_int=None, author=None, source=None, portal=None):
        self.title = title
        self.title_int = title_int
        self.lead_text = lead_text
        self.lead_text_int = lead_text_int
        self.link = link
        self.text = text
        self.when_published = when_published
        self.author = author
        self.source = source
        self.portal = portal

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    def _repr_pretty_(self, p, cycle):
        p.text(str(self) if not cycle else '...')

