
# Custom Nive design example based on bootstrap

Demonstrates how to build a new design and distribute it as an independent 
python module. The configuration file to register the design as nive
module is written in python. 

For the documentation and api how to use designs see: http://cms.nive.co

## Usage

Replace the current module name (nive_tmpl_design_python) with your own 
e.g. `my_design_module`. 

After installation (``path/to/bin/python setup.py develop``) activate the 
design by adding ``my_design_module`` to your website project module list.

For a default scaffold installation go to `__init__.py` of your website
and add the following line to the configuration 
``website.modules.append("my_design_module")`` and remove the original 
design e.g. ::

    website = AppConf("nive.cms.app",
        title=u"My website", 
        id="website",
        ...
    )
    website.modules.append("my_design_module")
    # -> remove these lines:
    #design = ViewModuleConf("nive.cms.design.view",
    #    templates="mywebsite:templates"
    #)
    #website.modules.append(design)

