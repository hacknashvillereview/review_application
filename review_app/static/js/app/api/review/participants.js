define([
    'q',
    'app/model/review/models'
],
function (Q, settings, models) {

    return {
        search : function (search_criteria) {
            var self = this;
            var deferred = Q.defer();

            $.ajax({
                url: 'tbd',
                type: 'GET',
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                success: function (response) {
                    deferred.resolve(response);
                },
                error: function (request, status, error) {
                    deferred.reject(new Error(error));
                }
            });

            return deferred.promise;
        }
    }
});