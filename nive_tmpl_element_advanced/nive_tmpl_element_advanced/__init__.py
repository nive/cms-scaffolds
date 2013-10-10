
from nive.definitions import ObjectConf
from nive.utils.utils import ConvertHTMLToText
from nive_cms.baseobjects import PageElementBase


# object functionality ----------------------------------------------------------

class MyArticle(PageElementBase):
    """
    Custom functions 
    """
    
    def related(self, max=5):
        """
        Lookup articles with same topic anywhere on the website.
        """
        dataroot = self.root()
        r = dataroot.SearchType("article_adv", parameter={"topic":self.data.topic}, fields=["id", "title"], operators={"topic":"="}, max=max)
        return r["items"]
    

# views -------------------------------------------------------------------------

def astext(context, request):
    return context.title + "\r\n\r\n" + ConvertHTMLToText(context.textblock)


# configuration -----------------------------------------------------------------
    
configuration = ObjectConf(
    id="article_adv",
    name="Article",
    dbparam="article_adv",
    context=MyArticle,
    template="nive_tmpl_element_advanced:article.pt",
    selectTag=20,
    icon = "nive_cms.cmsview:static/images/types/element.png",
    description=""
)

category = (
    {"id": "politics", "name": "Politics"},
    {"id": "music", "name": "Music"},
    {"id": "tech", "name": "Technical"},
)

configuration.data = (
    FieldConf(id="textblock", datatype="htext", size=10000, default="", name="Text", fulltext=1, description=""),
    FieldConf(id="image",     datatype="file",  size=0,     default="", name="Image file",       description=""),
    FieldConf(id="link",      datatype="url",   size=255,   default="", name="Link",             description=""),
    FieldConf(id="topic",     datatype="list",  size=10,    default="music", name="Topic",       description=""),
)

configuration.forms = {
    "create": {"fields":["topic", "title", "textblock", "image"]}, 
    "edit":   {"fields":["title", "textblock", "image"]}
}

configuration.views = (
    ViewConf(name="astext", context=MyArticle, view=astext)
)
