define([
    'knockout',
    'app/util/templateLoader',
    'app/viewmodel/review/default'
    ],
function (ko, loader, defaultModel) {

    var SearchModel = function () {
        var self = this;

        self.mutable = ko.observable('0.00');
        
        self.searchResults = [];
        for (var i = 0; i < 24; i++) {
            self.searchResults.push({ id: Math.random() * 100, title: 'Test' });
        };

        self.updateMutable = function () {
            self.mutable(Math.random().toString());
        };
    };

    SearchModel.prototype = defaultModel;
    searchModel = new SearchModel();

    loader.load('review-results', '/static/views/review/searchResults.html', searchModel, function () {} );

    return searchModel;

});