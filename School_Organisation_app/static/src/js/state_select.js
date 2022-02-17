odoo.define('js_framework_sample.SampleFrameWork', function (require) {
"use strict";
var selection_field=require("web.basic_fields");

var core = require('web.core');
var deprecatedFields = require('web.basic_fields.deprecated');
var _t = core._t;
var _lt = core._lt;    

selection_field.StateSelectionWidget.include({
            _prepareDropdownValues: function () {
                var self = this;
                var _data = [];
                var current_stage_id = self.recordData.stage_id && self.recordData.stage_id[0];
                var stage_data = {
                    id: current_stage_id,
                    legend_normal: this.recordData.legend_normal || undefined,
                    legend_blocked : this.recordData.legend_blocked || undefined,
                    legend_done: this.recordData.legend_done || undefined,
                   
                };
                _.map(this.field.selection || [], function (selection_item) {
                    var value = {
                        'name': selection_item[0],
                        'tooltip': selection_item[1],
                        
                    };
                    if (selection_item[0] === 'normal') {
                        value.state_name = stage_data.legend_normal ? stage_data.legend_normal : selection_item[1];
                    } else if (selection_item[0] === 'done') {
                        value.state_class = 'o_status_green';
                        value.state_name = stage_data.legend_done ? stage_data.legend_done : selection_item[1];
                    } else if (selection_item[0] === 'update') {
                        value.state_class = 'o_status_yellow';
                        value.state_name = stage_data.legend_yellow ? stage_data.legend_yellow : selection_item[1];
                    }else {
                        value.state_class = 'o_status_red';
                        value.state_name = stage_data.legend_blocked ? stage_data.legend_blocked : selection_item[1];
                    }
                    _data.push(value);
                });
                console.log("JS is working");
                return _data;
            },
});

});