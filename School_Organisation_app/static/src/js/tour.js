odoo.define('my_module.tour', function(require) {
    "use strict";
    
    var core = require('web.core');
    var tour = require('web_tour.tour');
    var selection_field=require("web.basic_fields");
    var deprecatedFields = require('web.basic_fields.deprecated');

    var _t = core._t;
    var _lt = core._lt;   
    
    tour.register('my_module_tour', {
        url: "/web",
    }, [tour.STEPS.MENU_MORE, {
        trigger: '.o_app[data-menu-xmlid="my_module.my_module_parent_menu"], .oe_menu_toggler[data-menu-xmlid="my_module.my_module_parent_menu"]',
        content: _t('Explore the information in smarter way...'),
        position: 'bottom',
    } 
    , {
        trigger: ".oe_link",
        extra_trigger: '.oe_highlight',
        content:  _t("Information for second step of tour."),
        position: "right"
    }
    , {
        trigger: ".o_form_required",
        extra_trigger: '.oe_highlight',
        content:  _t("Information for third step of tour."),
        position: "top"
    }
    , {
        trigger: ".o_address_street",
        extra_trigger: '.oe_highlight',
        content:  _t("Information for next and so on"),
        position: "left"
    }
    
    
    ]);
    
    });