define([
    'knockout',
    'app/util/templateLoader',
    'app/viewmodel/home/default'
    ], 
function (ko, loader, defaultViewModel) {

    var HomeMainModel = function () {
        var self = this;

    };

    HomeMainModel.prototype = defaultViewModel;
    homeMainModel = new HomeMainModel();

    loader.load('review-content', '/static/views/review/content.html', homeMainModel, function () {} );

    return homeMainModel;

});