define(['knockout', 'app/util/templateLoader'],
function (ko, loader) {

    var DefaultModel = function () {
        var self = this;

        self.sections = [
            {
                title: 'Home', 
                id: 'home'
            },
            {
                title: 'Packages', 
                id: 'packages'
            }
        ];
        self.currentSection = ko.observable();

        self.gotoSection = function (section) {
            location.hash = section.title;
            self.currentSection(section);
            console.log(self.currentSection());
        };

        // Take the user to the stacks section
        self.gotoSection(self.sections[0]);
    };

    var defaultModel = new DefaultModel();

    loader.load('review-navigation', '/static/views/navbar.html', defaultModel, function () {} );

    return defaultModel;
});