define([
    'q',
    'knockout',
    'app/util/templateLoader',
    'app/viewmodel/review/default',
    'app/api/review/API'
    ], 
function (Q, ko, loader, defaultViewModel, API) {

    require(['app/viewmodel/review/dashboard','app/viewmodel/review/search'], function () {});

    var ReviewModel = function () {
        var self = this;

        // API.Concepts.search('obama')
        //     .then(function (mappedResults) {
        //         console.log('mappedResults',mappedResults);
        //     });

    };

    ReviewModel.prototype = defaultViewModel;
    reviewModel = new ReviewModel();

    return reviewModel;

});