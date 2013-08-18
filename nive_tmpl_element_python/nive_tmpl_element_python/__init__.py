
from nive.definitions import ObjectConf

configuration = ObjectConf(
    id="article",
    name="Article",
    dbparam="article",
    context="nive.components.objects.base.PageElementBase",
    template="nive_tmpl_element_python:article.pt",
    selectTag=20,
    icon="nive.cms.cmsview:static/images/types/element.png",
    description=""
)

configuration.data = (
    FieldConf(id="textblock", datatype="htext", size=10000, default="", name="Text", fulltext=1, description=""),
    FieldConf(id="image",     datatype="file",  size=0,     default="", name="Image file",       description=""),
    FieldConf(id="link",      datatype="url",   size=255,   default="", name="Link",             description=""),
)

configuration.forms = {
    "create": {"fields":["title", "textblock", "image"]}, 
    "edit":   {"fields":["title", "textblock", "image"]}
}
