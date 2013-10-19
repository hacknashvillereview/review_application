define(['app/model/review/default'], function (DefaultModel) {

    var ConceptModel = function (record) {};
    ConceptModel.prototype = new DefaultModel();

    /*
        Override the simplistic default creation process if you want 
        to use Knockout bindings or have complex logic involved
    */
    // ConceptModel.prototype.create = function (record) {};

    return ConceptModel;
});