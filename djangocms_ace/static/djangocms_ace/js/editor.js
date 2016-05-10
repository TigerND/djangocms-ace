/*global ace*/
window.djangocms_ace_create_editor = function(content, opts, callback) {
    try {
        var element_name = opts.variable_name + '_element';
        var editor = ace.edit(element_name);
        editor.setOptions({
            maxLines: Infinity
        });
        editor.setReadOnly(opts.readonly);
        editor.setTheme(opts.theme);
        editor.getSession().setMode(opts.mode);
        editor.$blockScrolling = Infinity;
        editor.setValue(content);
        editor.selection.clearSelection();
        document.getElementById(element_name).style.fontSize = '14px';
        editor.resize();
        callback(undefined, editor);
    }
    catch (err) {
        console.log(err);
        callback(err);
    }
};