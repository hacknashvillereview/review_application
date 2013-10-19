define([
    'knockout',
    'app/util/templateLoader',
    'app/viewmodel/default'
    ], 
function (ko, loader, defaultModel) {
    var moduleDefaultModel;

    var ModuleDefaultModel = function () {
        var self = this;

        // self.subsections = [
        //     {
        //         id: 'about-review',
        //         title:'About'
        //     },
        //     {
        //         id: 'contact-review',
        //         title: 'Contact Us'
        //     }
        // ];
        // self.currentSubSection = ko.observable(self.subsections[0]);

        // self.gotoSubSection = function (subsection) {
        //     location.hash = subsection.id;
        //     self.currentSubSection(subsection);
        //     console.log(self.currentSubSection());
        // };
    };

    ModuleDefaultModel.prototype = defaultModel;
    moduleDefaultModel = new ModuleDefaultModel();

    // loader.load('home-page', '/static/views/home/navigation.html', moduleDefaultModel, function () {} );

    return moduleDefaultModel;

});