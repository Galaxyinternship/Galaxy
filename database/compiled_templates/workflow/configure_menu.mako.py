# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491895395.856025
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/workflow/configure_menu.mako'
_template_uri = 'workflow/configure_menu.mako'
_source_encoding = 'ascii'
_exports = ['init', 'center_panel', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view="workflow"
        self.message_box_visible=False
        
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        shared_by_others = context.get('shared_by_others', UNDEFINED)
        ids_in_menu = context.get('ids_in_menu', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        len = context.get('len', UNDEFINED)
        util = context.get('util', UNDEFINED)
        workflows = context.get('workflows', UNDEFINED)
        message = context.get('message', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <div style="overflow: auto; height: 100%;">\n        <div class="page-container" style="padding: 10px;">\n')
        if message:

            try:
                messagetype
            except:
                messagetype = "done"
            
            
            __M_writer(u'\n<p />\n<div class="')
            __M_writer(filters.html_escape(unicode(messagetype)))
            __M_writer(u'message">\n    ')
            __M_writer(filters.html_escape(unicode(message)))
            __M_writer(u'\n</div>\n')
        __M_writer(u'\n<form action="')
        __M_writer(filters.html_escape(unicode(h.url_for(controller='workflow', action='configure_menu'))))
        __M_writer(u'" method="POST">\n\n<table class="colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n    <tr class="header">\n        <th>Name</th>\n        <th>Owner</th>\n        <th># of Steps</th>\n')
        __M_writer(u'        <th>Show in menu</th>\n    </tr>\n        \n')
        if workflows:
            __M_writer(u'\n')
            for i, workflow in enumerate( workflows ):
                __M_writer(u'            <tr>\n                <td>\n                    ')
                __M_writer(filters.html_escape(unicode(util.unicodify( workflow.name ))))
                __M_writer(u'\n                </td>\n                <td>You</td>\n                <td>')
                __M_writer(filters.html_escape(unicode(len(workflow.latest_workflow.steps))))
                __M_writer(u'</td>\n                <td>\n                    <input type="checkbox" name="workflow_ids" value="')
                __M_writer(filters.html_escape(unicode(workflow.id)))
                __M_writer(u'"\n')
                if workflow.id in ids_in_menu:
                    __M_writer(u'                        checked\n')
                __M_writer(u'                    />\n                </td>\n            </tr>    \n')
            __M_writer(u'\n')
        __M_writer(u'\n')
        if shared_by_others:
            __M_writer(u'\n')
            for i, association in enumerate( shared_by_others ):
                __M_writer(u'            ')
                workflow = association.stored_workflow 
                
                __M_writer(u'\n            <tr>\n                <td>\n                    ')
                __M_writer(filters.html_escape(unicode(util.unicodify( workflow.name ))))
                __M_writer(u'\n                </td>\n                <td>')
                __M_writer(filters.html_escape(unicode(workflow.user.email)))
                __M_writer(u'</td>\n                <td>')
                __M_writer(filters.html_escape(unicode(len(workflow.latest_workflow.steps))))
                __M_writer(u'</td>\n                <td>\n                    <input type="checkbox" name="workflow_ids" value="')
                __M_writer(filters.html_escape(unicode(workflow.id)))
                __M_writer(u'"\n')
                if workflow.id in ids_in_menu:
                    __M_writer(u'                        checked\n')
                __M_writer(u'                    />\n                </td>\n            </tr>    \n')
            __M_writer(u'\n')
        __M_writer(u'\n')
        if not workflows and not shared_by_others:
            __M_writer(u'        <tr>\n            <td colspan="4">You do not have any accessible workflows.</td>\n        </tr>\n')
        __M_writer(u'\n</table>\n\n<p />\n<input type="Submit" value="Save" />\n\n</form>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'Configure workflow menu')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"128": 90, "134": 13, "138": 13, "144": 138, "27": 2, "32": 1, "33": 2, "34": 11, "35": 13, "36": 99, "42": 4, "47": 4, "48": 5, "55": 10, "61": 15, "73": 15, "74": 18, "75": 19, "82": 24, "83": 26, "84": 26, "85": 27, "86": 27, "87": 30, "88": 31, "89": 31, "90": 39, "91": 42, "92": 43, "93": 44, "94": 45, "95": 47, "96": 47, "97": 50, "98": 50, "99": 52, "100": 52, "101": 53, "102": 54, "103": 56, "104": 60, "105": 62, "106": 63, "107": 64, "108": 65, "109": 66, "110": 66, "112": 66, "113": 69, "114": 69, "115": 71, "116": 71, "117": 72, "118": 72, "119": 74, "120": 74, "121": 75, "122": 76, "123": 78, "124": 82, "125": 84, "126": 85, "127": 86}, "uri": "workflow/configure_menu.mako", "filename": "templates/webapps/galaxy/workflow/configure_menu.mako"}
__M_END_METADATA
"""
