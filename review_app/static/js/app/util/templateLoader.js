define(['jquery', 'knockout'], function ($, ko) {

    return {
        load : function (target, templateURL, vm, callback) {
            console.log('Binding ', target, ' to ', templateURL);
            $(target).load(templateURL, function () {
                ko.applyBindings(vm, document.querySelector(target));

                if (callback) {
                    callback.call(document.querySelector(target));
                }
            });
        }
    }
});