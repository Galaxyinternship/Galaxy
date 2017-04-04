# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491279718.168751
_enable_loop = True
_template_filename = u'templates/webapps/galaxy/dataset/security_common.mako'
_template_uri = u'/dataset/security_common.mako'
_source_encoding = 'ascii'
_exports = ['render_permission_form', 'render_select']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_permission_form(context,obj,obj_name,form_url,roles,do_not_render=[],all_roles=[]):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        def render_select(current_actions,action_key,action,roles):
            return render_render_select(context,current_actions,action_key,action,roles)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        if isinstance( obj, trans.app.model.User ):
            current_actions = obj.default_permissions
            permitted_actions = trans.app.model.Dataset.permitted_actions.items()
            obj_str = 'user %s' % obj_name
            obj_type = 'dataset'
        elif isinstance( obj, trans.app.model.History ):
            current_actions = obj.default_permissions
            permitted_actions = trans.app.model.Dataset.permitted_actions.items()
            obj_str = 'history %s' % obj_name
            obj_type = 'dataset'
        elif isinstance( obj, trans.app.model.Dataset ):
            current_actions = obj.actions
            permitted_actions = trans.app.model.Dataset.permitted_actions.items()
            obj_str = obj_name
            obj_type = 'dataset'
        elif isinstance( obj, trans.app.model.LibraryDatasetDatasetAssociation ):
            current_actions = obj.actions + obj.dataset.actions
            permitted_actions = trans.app.model.Dataset.permitted_actions.items() + trans.app.model.Library.permitted_actions.items()
            obj_str = obj_name
            obj_type = 'dataset'
        elif isinstance( obj, trans.app.model.Library ):
            current_actions = obj.actions
            permitted_actions = trans.app.model.Library.permitted_actions.items()
            obj_str = 'library %s' % obj_name
            obj_type = 'library'
        elif isinstance( obj, trans.app.model.LibraryDataset ):
            current_actions = obj.actions
            permitted_actions = trans.app.model.Library.permitted_actions.items()
            obj_str = 'library dataset %s' % obj_name
            obj_type = 'library'
        elif isinstance( obj, trans.app.model.LibraryFolder ):
            current_actions = obj.actions
            permitted_actions = trans.app.model.Library.permitted_actions.items()
            obj_str = 'library folder %s' % obj_name
            obj_type = 'library'
        else:
            current_actions = []
            permitted_actions = {}.items()
            obj_str = 'unknown object %s' % obj_name
            obj_type = ''
            
        
        __M_writer(u'\n    <script type="text/javascript">\n        $( document ).ready( function () {\n            $( \'.role_add_button\' ).click( function() {\n                var action = this.id.substring( 0, this.id.lastIndexOf( \'_add_button\' ) )\n                var in_select = \'#\' + action + \'_in_select\';\n                var out_select = \'#\' + action + \'_out_select\';\n                return !$( out_select + \' option:selected\' ).remove().appendTo( in_select );\n            });\n            $( \'.role_remove_button\' ).click( function() {\n                var action = this.id.substring( 0, this.id.lastIndexOf( \'_remove_button\' ) )\n                var in_select = \'#\' + action + \'_in_select\';\n                var out_select = \'#\' + action + \'_out_select\';\n                return !$( in_select + \' option:selected\' ).remove().appendTo( out_select );\n            });\n            $( \'form#edit_role_associations\' ).submit( function() {\n                $( \'.in_select option\' ).each(function( i ) {\n                    $( this ).attr( "selected", "selected" );\n                });\n            });\n            // Temporary removal of select2 for all permissions forms\n            $(\'#edit_role_associations select\').select2("destroy");\n        });\n    </script>\n    <div class="toolForm">\n        <div class="toolFormTitle">Manage ')
        __M_writer(unicode(obj_type))
        __M_writer(u' permissions on ')
        __M_writer(filters.html_escape(unicode(obj_str )))
        __M_writer(u'</div>\n        <div class="toolFormBody">\n            <form name="edit_role_associations" id="edit_role_associations" action="')
        __M_writer(unicode(form_url))
        __M_writer(u'" method="post">\n                <div class="form-row"></div>\n')
        for k, v in permitted_actions:
            if k not in do_not_render:
                __M_writer(u'                        <div class="form-row">\n')
                __M_writer(u'                            ')
                render_all_roles = k == 'LIBRARY_ACCESS' 
                
                __M_writer(u'\n')
                if render_all_roles:
                    __M_writer(u'                                ')
                    __M_writer(unicode(render_select( current_actions, k, v, all_roles )))
                    __M_writer(u'\n')
                else:
                    __M_writer(u'                                ')
                    __M_writer(unicode(render_select( current_actions, k, v, roles )))
                    __M_writer(u'\n')
                __M_writer(u'                        </div>\n')
        __M_writer(u'                <div class="form-row">\n                    <input type="submit" name="update_roles_button" value="Save"/>\n                </div>\n            </form>\n        </div>\n    </div>\n    <p/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_select(context,current_actions,action_key,action,roles):
    __M_caller = context.caller_stack._push_frame()
    try:
        filter = context.get('filter', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        import sets
        in_roles = sets.Set()
        for a in current_actions:
            if a.action == action.action:
                in_roles.add( a.role )
        out_roles = filter( lambda x: x not in in_roles, roles )
            
        
        __M_writer(u'\n    <p>\n        <b>')
        __M_writer(unicode(action.action))
        __M_writer(u':</b> ')
        __M_writer(unicode(action.description))
        __M_writer(u'\n')
        if action == trans.app.security_agent.permitted_actions.DATASET_ACCESS:
            __M_writer(u'            <br/>\n            NOTE: Users must have every role associated with this dataset in order to access it\n')
        __M_writer(u'    </p>\n    <div style="width: 100%; white-space: nowrap;">\n        <div style="float: left; width: 50%;">\n            Roles associated:<br />\n            <select name="')
        __M_writer(unicode(action_key))
        __M_writer(u'_in" id="')
        __M_writer(unicode(action_key))
        __M_writer(u'_in_select" class="in_select" style="max-width: 98%; width: 98%; height: 150px; font-size: 100%;" multiple>\n')
        for role in in_roles:
            __M_writer(u'                    <option value="')
            __M_writer(unicode(role.id))
            __M_writer(u'">')
            __M_writer(unicode(role.name))
            __M_writer(u'</option>\n')
        __M_writer(u'            </select> <br />\n            <div style="width: 98%; text-align: right"><input type="submit" id="')
        __M_writer(unicode(action_key))
        __M_writer(u'_remove_button" class="role_remove_button" value=">>"/></div>\n        </div>\n        <div style="width: 50%;">\n            Roles not associated:<br />\n            <select name="')
        __M_writer(unicode(action_key))
        __M_writer(u'_out" id="')
        __M_writer(unicode(action_key))
        __M_writer(u'_out_select" style="max-width: 98%; width: 98%; height: 150px; font-size: 100%;" multiple>\n')
        for role in out_roles:
            __M_writer(u'                    <option value="')
            __M_writer(unicode(role.id))
            __M_writer(u'">')
            __M_writer(unicode(role.name))
            __M_writer(u'</option>\n')
        __M_writer(u'            </select> <br />\n            <input type="submit" id="')
        __M_writer(unicode(action_key))
        __M_writer(u'_add_button" class="role_add_button" value="<<"/>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"128": 11, "129": 11, "130": 12, "131": 13, "132": 16, "133": 20, "134": 20, "135": 20, "136": 20, "137": 21, "138": 22, "139": 22, "140": 22, "141": 22, "142": 22, "143": 24, "16": 0, "145": 25, "146": 29, "147": 29, "148": 29, "21": 37, "22": 132, "151": 31, "152": 31, "153": 31, "154": 31, "155": 31, "28": 40, "157": 34, "150": 30, "149": 29, "36": 40, "37": 41, "156": 33, "158": 34, "164": 158, "80": 82, "81": 107, "82": 107, "83": 107, "84": 107, "85": 109, "86": 109, "87": 111, "88": 112, "89": 113, "90": 116, "91": 116, "93": 116, "94": 117, "95": 118, "96": 118, "97": 118, "98": 119, "99": 120, "100": 120, "101": 120, "102": 122, "103": 125, "144": 25, "109": 1, "115": 1, "116": 2, "125": 9, "126": 11, "127": 11}, "uri": "/dataset/security_common.mako", "filename": "templates/webapps/galaxy/dataset/security_common.mako"}
__M_END_METADATA
"""
