define([
    'knockout', 
    'app/util/templateLoader', 
    'app/viewmodel/review/default'
    ],
function (ko, loader, defaultModel) {

    DashboardModel = function () {
        var self = this;

    };

    DashboardModel.prototype = defaultModel;
    dashboardModel = new DashboardModel();

    loader.load('review-dashboard', '/static/views/review/dashboard.html', dashboardModel, function () {} );

    return dashboardModel;
});