define(function () {

    var DefaultModel = function (record) {};
    DefaultModel.prototype.create = function (record) {
        var self = this;
        for (k in record) { self[k] = record[k]; }
        return self;
    };

    return DefaultModel;
});