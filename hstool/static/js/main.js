$(function () {
    $('.launch-modal').on('click', function () {
        var url = $(this).data('action');
        var title = $(this).data('title');
        $.ajax({
            type: "GET",
            url: url,
            success: function (data) {
                $('.modal-body').html(data);
                $('h4.modal-title').html(title);
                $('#add-modal-submit').data('action', url)
            },
            error: function (data) {
                alert('Error launching the modal')
            }
        })
    });

    $('#add-modal-submit').on('click', function () {
        var form = $('#add-form');
        var url = $(this).data('action');
        var formdata = false;
        if (window.FormData){
            formdata = new FormData(form[0]);
        }
        $.ajax({
            url: url,
            data: formdata ? formdata : form.serialize(),
            cache: false,
            contentType: false,
            processData: false,
            type: "POST",
            success: function (data) {
                $('.modal-body').html(data);
            },
            error: function (data) {
                alert('Error saving the data')
            }
        });
    });

    $('.view-figure-modal').on('click', function () {
        var url = $(this).data('action');
        var name = $(this).data('name');
        $.ajax({
            type: "GET",
            url: url,
            success: function (data) {
                $('.modal-body').html(data);
                $('h4.modal-title').html(name);
            },
            error: function (data) {
                alert('Error launching the modal')
            }
        })
    });

    $('#geo_scope').change(function () {
        var opt = $(this).find(":selected").val();
        if (opt) {
            var url = $(this).attr('href');
            var data = {'geo_scope_id': opt};
            $.ajax({
                url: url,
                data: data,
                type: "GET",
                success: function(resp) {
                    if (resp['required'] == true) {
                        $('#invisible').show();
                    } else {
                        $('#visible').attr("id", "invisible");
                        $('#invisible').hide();
                        $('#id_country option').prop('selected', function(){
                            return '';
                        });
                    }
                },
                error: function(resp) {
                    alert('Error on selection')
                }
            });
        }
        else {
            $('#visible').hide();
            $('#id_country option').prop('selected', function(){
                return '';
            });
        }
    }).change();

    $('[name="draft"]').on('click', function() {
        $('#id_draft').value = $(this).attr("value");
    });
});
