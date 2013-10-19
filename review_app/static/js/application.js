requirejs.config({
   paths: {
        'jquery': 'bower_components/jquery/jquery.min',
        'knockout': 'bower_components/knockout.js/knockout',
        'q': 'bower_components/q/q',
        'bootstrap': 'bower_components/bootstrap/dist/js/bootstrap.min'
    }, 

    shim: {
        'knockout': ['jquery'],
        'bootstrap': ['jquery']
    }
});

require(['knockout'], function (ko) { 

    ko.bindingHandlers.stopBindings = {
        init: function() {
            return { controlsDescendantBindings: true };
        }
    };

    require(['app/viewmodel/review/review'], function () { });

});
