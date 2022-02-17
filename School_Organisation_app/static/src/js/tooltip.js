QUnit.test('display a tooltip on a field', async function (assert) {
    assert.expect(4);

    var initialDebugMode = odoo.debug;
    odoo.debug = false;

    var list = await createView({
        View: ListView,
        model: 'foo',
        data: this.data,
        arch: '<tree>' +
                '<field name="foo"/>' +
                '<field name="bar" widget="toggle_button"/>' +
            '</tree>',
    });

    // this is done to force the tooltip to show immediately instead of waiting
    // 1000 ms. not totally academic, but a short test suite is easier to sell :(
    list.$('th[data-name=foo]').tooltip('show', false);

    list.$('th[data-name=foo]').trigger($.Event('mouseenter'));
    assert.strictEqual($('.tooltip .oe_tooltip_string').length, 0, "should not have rendered a tooltip");

    odoo.debug = true;
    // it is necessary to rerender the list so tooltips can be properly created
    await list.reload();
    list.$('th[data-name=foo]').tooltip('show', false);
    list.$('th[data-name=foo]').trigger($.Event('mouseenter'));
    assert.strictEqual($('.tooltip .oe_tooltip_string').length, 1, "should have rendered a tooltip");

    await list.reload();
    list.$('th[data-name=bar]').tooltip('show', false);
    list.$('th[data-name=bar]').trigger($.Event('mouseenter'));
    assert.containsOnce($, '.oe_tooltip_technical>li[data-item="widget"]',
        'widget should be present for this field');
    assert.strictEqual($('.oe_tooltip_technical>li[data-item="widget"]')[0].lastChild.wholeText.trim(),
        'Button (toggle_button)', "widget description should be correct");

    odoo.debug = initialDebugMode;
    list.destroy();
});