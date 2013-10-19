define(['app/model/review/default'], function (DefaultModel) {

    var ParticipantModel = function (record) {};
    ParticipantModel.prototype = new DefaultModel();

    /*
        Override the simplistic default creation process if you want 
        to use Knockout bindings or have complex logic involved
    */
    // ParticipantModel.prototype.create = function (record) {};

    return ParticipantModel;
});