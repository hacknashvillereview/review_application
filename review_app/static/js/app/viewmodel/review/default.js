define([
    'knockout',
    'app/util/templateLoader',
    'app/viewmodel/default'
    ], 
function (ko, loader, defaultModel) {
    var moduleDefaultModel;

    var ModuleDefaultModel = function () {
        var self = this;

        self.subsections = [
            {
                id: 'dashboard',
                title:'Dashboard'
            },
            {
                id: 'results',
                title: 'Search Results'
            }
        ];
        self.currentSubSection = ko.observable(self.subsections[0]);

        self.gotoSubSection = function (subsection) {
            location.hash = subsection.title;
            self.currentSubSection(subsection);
            console.log(self.currentSubSection());
        };
    };

    ModuleDefaultModel.prototype = defaultModel;
    moduleDefaultModel = new ModuleDefaultModel();

    loader.load('review-home-navigation', '/static/views/review/navigation.html', moduleDefaultModel, function () {} );

    return moduleDefaultModel;

});