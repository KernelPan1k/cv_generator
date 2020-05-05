(function ($) {
    function ckOnSortStart(ui) {
        var textareas = $(ui.item).find('textarea');

        textareas.each(function (i, element) {
            try {
                var id = $(element).prop('id');
                CKEDITOR.instances[id] && CKEDITOR.instances[id].destroy();
                element.setAttribute("data-processed", "0");
            } catch (err) {
                /* intentionally left empty */
            }
        });
    }

    function ckOnSortEnd(ui) {
        var textareas = $(ui.item).find('textarea');

        textareas.each(function (i, element) {
            if (element.getAttribute("data-processed") !== "1") {
                element.setAttribute("data-processed", "1");
                $($(element).data("external-plugin-resources")).each(function () {
                    CKEDITOR.plugins.addExternal(element[0], element[1], element[2]);
                });
                var config = $(element).data("config");
                config.width = "100%";
                CKEDITOR.replace(element.id, config);
            }
        });
    }

    $(document).on('nestedsortablestart', function (event, ui) {
        ckOnSortStart(ui);
    });

    $(document).on('sortstart', function (event, ui) {
        ckOnSortStart(ui);
    });

    $(document).on('nestedsortablestop', function (event, ui) {
        ckOnSortEnd(ui);
    });

    $(document).on('sortstop', function (event, ui) {
        ckOnSortEnd(ui);
    });
}($ || django.jQuery || window.jQuery));
