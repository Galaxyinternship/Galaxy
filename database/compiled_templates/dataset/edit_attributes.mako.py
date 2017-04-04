# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491279718.111382
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/dataset/edit_attributes.mako'
_template_uri = '/dataset/edit_attributes.mako'
_source_encoding = 'ascii'
_exports = ['stylesheets', 'datatype', 'javascripts', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7fc6446a3c90', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc6446a3c90')] = ns

    ns = runtime.TemplateNamespace('__anon_0x7fc65e27a050', context._clean_inheritance_tokens(), templateuri=u'/dataset/security_common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc65e27a050')] = ns

    ns = runtime.TemplateNamespace('__anon_0x7fc6446a3cd0', context._clean_inheritance_tokens(), templateuri=u'/refresh_frames.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc6446a3cd0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc6446a3c90')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7fc65e27a050')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x7fc6446a3cd0')._populate(_import_ns, [u'handle_refresh_frames'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_permission_form = _import_ns.get('render_permission_form', context.get('render_permission_form', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        all_roles = _import_ns.get('all_roles', context.get('all_roles', UNDEFINED))
        data_annotation = _import_ns.get('data_annotation', context.get('data_annotation', UNDEFINED))
        def datatype(dataset,datatypes):
            return render_datatype(context._locals(__M_locals),dataset,datatypes)
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        current_user_roles = _import_ns.get('current_user_roles', context.get('current_user_roles', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        util = _import_ns.get('util', context.get('util', UNDEFINED))
        datatypes = _import_ns.get('datatypes', context.get('datatypes', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        data = _import_ns.get('data', context.get('data', UNDEFINED))
        dataset_id = _import_ns.get('dataset_id', context.get('dataset_id', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        if message:
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        __M_writer(u'\n\n<ul class="nav nav-tabs">\n    <li class="active"><a href="#attributes" data-toggle="tab">Attributes</a></li>\n    <li><a href="#convert" data-toggle="tab">Convert Format</a></li>\n    <li><a href="#datatype" data-toggle="tab">Datatype</a></li>\n    <li><a href="#permissions" data-toggle="tab">Permissions</a></li>\n</ul>\n\n<div class="tab-content">\n\n<div class="tab-pane active toolForm" id="attributes">\n    <div class="toolFormTitle">')
        __M_writer(unicode(_('Edit Attributes')))
        __M_writer(u'</div>\n    <div class="toolFormBody">\n        <form name="edit_attributes" action="')
        __M_writer(unicode(h.url_for( controller='dataset', action='edit', dataset_id=dataset_id )))
        __M_writer(u'" method="post">\n            <div class="form-row">\n                <label>\n                    Name:\n                </label>\n                <div style="float: left; width: 250px; margin-right: 10px;">\n                    <input type="text" name="name" value="')
        __M_writer(filters.html_escape(unicode(data.get_display_name() )))
        __M_writer(u'" size="40"/>\n                </div>\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>\n                    Info:\n                </label>\n                <div style="float: left; width: 250px; margin-right: 10px;">\n                    ')
        info = data.info if data.info else '' 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['info'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n                    <textarea name="info" cols="40" rows="2">')
        __M_writer(filters.html_escape(unicode( util.unicodify( info ) )))
        __M_writer(u'</textarea>\n                </div>\n                <div style="clear: both"></div>\n            </div>\n')
        if trans.get_user() is not None:
            __M_writer(u'                <div class="form-row">\n                    <label>\n                        Annotation / Notes:\n                    </label>\n                    <div style="float: left; width: 250px; margin-right: 10px;">\n                        ')
            annotation = data_annotation if data_annotation else '' 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['annotation'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n                        <textarea name="annotation" cols="40" rows="2">')
            __M_writer(filters.html_escape(unicode(annotation )))
            __M_writer(u'</textarea>\n                    </div>\n                    <div style="clear: both"></div>\n                    <div class="toolParamHelp">Add an annotation or notes to a dataset; annotations are available when a history is viewed.</div>\n                </div>\n')
        for name, spec in data.metadata.spec.items():
            if spec.visible:
                __M_writer(u'                    <div class="form-row">\n                        <label>\n                            ')
                __M_writer(unicode(spec.desc))
                __M_writer(u':\n                        </label>\n                        <div style="float: left; width: 250px; margin-right: 10px;">\n                            ')
                __M_writer(unicode(data.metadata.get_html_by_name( name, trans=trans )))
                __M_writer(u'\n                        </div>\n                        <div style="clear: both"></div>\n                    </div>\n')
        __M_writer(u'            <div class="form-row">\n                <input type="submit" name="save" value="')
        __M_writer(unicode(_('Save')))
        __M_writer(u'"/>\n            </div>\n        </form>\n        <form name="auto_detect" action="')
        __M_writer(unicode(h.url_for( controller='dataset', action='edit', dataset_id=dataset_id )))
        __M_writer(u'" method="post">\n            <div class="form-row">\n                <div style="float: left; width: 250px; margin-right: 10px;">\n                    <input type="submit" name="detect" value="')
        __M_writer(unicode(_('Auto-detect')))
        __M_writer(u'"/>\n                </div>\n                <div class="toolParamHelp" style="clear: both;">\n                    This will inspect the dataset and attempt to correct the above column values if they are not accurate.\n                </div>\n            </div>\n        </form>\n')
        if data.missing_meta():
            __M_writer(u'            <div class="form-row">\n                <div class="errormessagesmall">')
            __M_writer(unicode(_('Required metadata values are missing. Some of these values may not be editable by the user. Selecting "Auto-detect" will attempt to fix these values.')))
            __M_writer(u'</div>\n            </div>\n')
        __M_writer(u'    </div>\n</div>\n\n<div class="tab-pane toolForm" id="convert">\n    <div class="toolFormTitle">')
        __M_writer(unicode(_('Convert to new format')))
        __M_writer(u'</div>\n    <div class="toolFormBody">\n        ')
        converters = data.get_converter_types() 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['converters'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if len( converters ) > 0:
            __M_writer(u'            <form name="convert_data" action="')
            __M_writer(unicode(h.url_for( controller='dataset', action='edit', dataset_id=dataset_id )))
            __M_writer(u'" method="post">\n                <div class="form-row">\n                    <div style="float: left; width: 250px; margin-right: 10px;">\n                        <select name="target_type">\n')
            for key, value in converters.items():
                __M_writer(u'                                <option value="')
                __M_writer(unicode(key))
                __M_writer(u'">')
                __M_writer(unicode(value.name))
                __M_writer(u'</option>\n')
            __M_writer(u'                        </select>\n                    </div>\n                    <div class="toolParamHelp" style="clear: both;">\n                        This will create a new dataset with the contents of this dataset converted to a new format.\n                    </div>\n                    <div style="clear: both"></div>\n                </div>\n                <div class="form-row">\n                    <input type="submit" name="convert_data" value="')
            __M_writer(unicode(_('Convert')))
            __M_writer(u'"/>\n                </div>\n            </form>\n')
        else:
            __M_writer(u'            No conversions available\n')
        __M_writer(u'    </div>\n</div>\n\n<div class="tab-pane toolForm" id="datatype">\n    <div class="toolFormTitle">')
        __M_writer(unicode(_('Change data type')))
        __M_writer(u'</div>\n    <div class="toolFormBody">\n')
        if data.datatype.allow_datatype_change:
            __M_writer(u'            <form name="change_datatype" action="')
            __M_writer(unicode(h.url_for( controller='dataset', action='edit', dataset_id=dataset_id )))
            __M_writer(u'" method="post">\n                <div class="form-row">\n                    <label>\n                        ')
            __M_writer(unicode(_('New Type')))
            __M_writer(u':\n                    </label>\n                    <div style="float: left; width: 250px; margin-right: 10px;">\n                        ')
            __M_writer(unicode(datatype( data, datatypes )))
            __M_writer(u'\n                    </div>\n                    <div class="toolParamHelp" style="clear: both;">\n                        ')
            __M_writer(unicode(_('This will change the datatype of the existing dataset but <i>not</i> modify its contents. Use this if Galaxy has incorrectly guessed the type of your dataset.')))
            __M_writer(u'\n                    </div>\n                    <div style="clear: both"></div>\n                </div>\n                <div class="form-row">\n                    <input type="submit" name="change" value="')
            __M_writer(unicode(_('Save')))
            __M_writer(u'"/>\n                </div>\n            </form>\n')
        else:
            __M_writer(u'            <div class="form-row">\n                <div class="warningmessagesmall">')
            __M_writer(unicode(_('Changing the datatype of this dataset is not allowed.')))
            __M_writer(u'</div>\n            </div>\n')
        __M_writer(u'    </div>\n</div>\n<p />\n\n<div class="tab-pane" id="permissions">\n')
        if trans.app.security_agent.can_manage_dataset( current_user_roles, data.dataset ):
            __M_writer(u'    ')
            __M_writer(u'\n    ')
            __M_writer(unicode(render_permission_form( data.dataset, data.get_display_name(), h.url_for( controller='dataset', action='edit', dataset_id=dataset_id ), all_roles )))
            __M_writer(u'\n')
        elif trans.user:
            __M_writer(u'    <div class="toolForm">\n        <div class="toolFormTitle">View Permissions</div>\n        <div class="toolFormBody">\n            <div class="form-row">\n')
            if data.dataset.actions:
                __M_writer(u'                    <ul>\n')
                for action, roles in trans.app.security_agent.get_permissions( data.dataset ).items():
                    if roles:
                        __M_writer(u'                                <li>')
                        __M_writer(unicode(action.description))
                        __M_writer(u'</li>\n                                <ul>\n')
                        for role in roles:
                            __M_writer(u'                                        <li>')
                            __M_writer(unicode(role.name))
                            __M_writer(u'</li>\n')
                        __M_writer(u'                                </ul>\n')
                __M_writer(u'                    </ul>\n')
            else:
                __M_writer(u'                    <p>This dataset is accessible by everyone (it is public).</p>\n')
            __M_writer(u'            </div>\n        </div>\n    </div>\n')
        else:
            __M_writer(u'    Permissions not available (not logged in)\n')
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc6446a3c90')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7fc65e27a050')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x7fc6446a3cd0')._populate(_import_ns, [u'handle_refresh_frames'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(h.css( "base", "autocomplete_tagging" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_datatype(context,dataset,datatypes):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc6446a3c90')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7fc65e27a050')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x7fc6446a3cd0')._populate(_import_ns, [u'handle_refresh_frames'])
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <select name="datatype">\n')
        for ext in datatypes:
            if dataset.ext == ext:
                __M_writer(u'                <option value="')
                __M_writer(unicode(ext))
                __M_writer(u'" selected="yes">')
                __M_writer(unicode(_(ext)))
                __M_writer(u'</option>\n')
            else:
                __M_writer(u'                <option value="')
                __M_writer(unicode(ext))
                __M_writer(u'">')
                __M_writer(unicode(_(ext)))
                __M_writer(u'</option>\n')
        __M_writer(u'    </select>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc6446a3c90')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7fc65e27a050')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x7fc6446a3cd0')._populate(_import_ns, [u'handle_refresh_frames'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        handle_refresh_frames = _import_ns.get('handle_refresh_frames', context.get('handle_refresh_frames', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        __M_writer(unicode(handle_refresh_frames()))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.js(
        "libs/jquery/jquery.autocomplete",
    )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc6446a3c90')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x7fc65e27a050')._populate(_import_ns, [u'render_permission_form'])
        _mako_get_namespace(context, '__anon_0x7fc6446a3cd0')._populate(_import_ns, [u'handle_refresh_frames'])
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(unicode(_('Edit Dataset Attributes')))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 2, "26": 177, "29": 3, "35": 0, "61": 1, "62": 2, "63": 3, "64": 5, "65": 9, "66": 17, "67": 29, "68": 31, "69": 32, "70": 32, "71": 32, "72": 34, "73": 46, "74": 46, "75": 48, "76": 48, "77": 54, "78": 54, "79": 63, "83": 63, "84": 64, "85": 64, "86": 68, "87": 69, "88": 74, "92": 74, "93": 75, "94": 75, "95": 81, "96": 82, "97": 83, "98": 85, "99": 85, "100": 88, "101": 88, "102": 94, "103": 95, "104": 95, "105": 98, "106": 98, "107": 101, "108": 101, "109": 108, "110": 109, "111": 110, "112": 110, "113": 113, "114": 117, "115": 117, "116": 119, "120": 119, "121": 120, "122": 121, "123": 121, "124": 121, "125": 125, "126": 126, "127": 126, "128": 126, "129": 126, "130": 126, "131": 128, "132": 136, "133": 136, "134": 139, "135": 140, "136": 142, "137": 146, "138": 146, "139": 148, "140": 149, "141": 149, "142": 149, "143": 152, "144": 152, "145": 155, "146": 155, "147": 158, "148": 158, "149": 163, "150": 163, "151": 166, "152": 167, "153": 168, "154": 168, "155": 171, "156": 176, "157": 177, "158": 177, "159": 178, "160": 178, "161": 179, "162": 180, "163": 184, "164": 185, "165": 186, "166": 187, "167": 188, "168": 188, "169": 188, "170": 190, "171": 191, "172": 191, "173": 191, "174": 193, "175": 196, "176": 197, "177": 198, "178": 200, "179": 203, "180": 204, "181": 206, "187": 7, "196": 7, "197": 8, "198": 8, "204": 19, "213": 19, "214": 21, "215": 22, "216": 23, "217": 23, "218": 23, "219": 23, "220": 23, "221": 24, "222": 25, "223": 25, "224": 25, "225": 25, "226": 25, "227": 28, "233": 11, "244": 11, "245": 12, "246": 12, "247": 13, "248": 13, "249": 14, "252": 16, "258": 5, "267": 5, "273": 267}, "uri": "/dataset/edit_attributes.mako", "filename": "templates/webapps/galaxy/dataset/edit_attributes.mako"}
__M_END_METADATA
"""
