define([
    'q',
    'app/api/review/settings',
    'app/model/review/models'
],
function (Q, settings, models) {

    return {
        search : function (search_criteria) {
            var self = this;
            var deferred = Q.defer();
            var api = JSON.stringify({'api': 'concepts.textsearch'});

            console.log('starting search', settings.conceptsProxy);

            $.ajax({
                url: settings.conceptsProxy,
                type: 'GET',
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "password": settings.baseKBAuth
                },
                data:  {
                    knowledge_base: settings.baseKBName,
                    query: api,
                    search_criteria: search_criteria
                },
                success: function (response) {
                    var mappedResults = $.map(response, function (item) { return new ImpalaConcept(item) });
                    console.log('search ended');

                    deferred.resolve(mappedResults);
                },
                error: function (request, status, error) {
                    deferred.reject(new Error(error));
                }
            });

            return deferred.promise;
        }
    }
});