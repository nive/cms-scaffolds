
# Advanced Nive page element scaffold and example

This example defines an advanced article element to be used as nive
plugin. All configuration is included in the modules __init__.py.

Including:

- customized object
- api example
- configuration
- data field definitions
- form drop down list
- additional views
- template

This is a good starting point to define your own elements.

Nive documentation and api: http://cms.nive.co

## Usage

Replace the current module name (nive_tmpl_element_advanced) with your own 
e.g. `my_element`. 

After installation (``path/to/bin/python setup.py develop``) activate the 
element by adding ``my_element`` to your websites project module list.

For a default scaffold installation go to `__init__.py` of your website
and add the following line to the configuration 
``website.modules.append("my_element")`` e.g. ::

    website = AppConf("nive.cms.app",
        title=u"My website", 
        id="website",
        ...
    )
    website.modules.append("my_element")



