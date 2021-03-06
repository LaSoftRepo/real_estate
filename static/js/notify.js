/**
 * Created by varunok on 08.03.17.
 */

    function notify_success_reload(title, text) {
         new PNotify({
             title: title || 'Успешно',
             text: text || 'Сохранено',
             type: 'success',
             styling: 'bootstrap3',
             delay: 2000,
             animate: {
                animate: true,
                in_class: 'fadeInUp',
                out_class: 'fadeOutDown'
            },
            afterClose: setTimeout(function(){ location.reload() }, 2500)
         });
    }
    function notify_success_not_reload(title, text) {
         new PNotify({
             title: title || 'Успешно',
             text: text || 'Сохранено',
             type: 'success',
             styling: 'bootstrap3',
             delay: 2000,
             animate: {
                animate: true,
                in_class: 'fadeInUp',
                out_class: 'fadeOutDown'
            }
         });
    }
    function notify_success(title, text) {
         new PNotify({
             title: title || 'Успешно',
             text: text || 'Сохранено',
             type: 'success',
             styling: 'bootstrap3',
             delay: 2000,
             animate: {
                animate: true,
                in_class: 'fadeInUp',
                out_class: 'fadeOutDown'
            }
         });
    }

    function notify_error(title, text) {
         new PNotify({
             title: title || 'Ошибка',
             text: text || '500',
             type: 'error',
             styling: 'bootstrap3',
             delay: 2000,
             animate: {
                animate: true,
                in_class: 'fadeInUp',
                out_class: 'fadeOutDown'
            }
         });
    }
    function notify_confirm(id, _this, title, text, fun) {
        (new PNotify({
            title: title || 'Подтверждение',
            text: text || 'Вы уверены, что хотите удалить?',
            icon: 'glyphicon glyphicon-question-sign',
            hide: false,
            styling: 'bootstrap3',
            confirm: {
                confirm: true
            },
            buttons: {
                closer: false,
                sticker: false
            },
            history: {
                history: false
            }
            })).get().on('pnotify.confirm', function() {
                        fun(id, _this);
            }).on('pnotify.cancel', function() {});
    }

    $(document).ready(function () {
        function not() {
            $.get('check-notify/')
               .then(function(response) {
                    var data = $.parseJSON(response);
                    if(data.notify){
                        $('.notify').text(data.notify)
                    }
                }, function(err) {
                });
        }
        not();

       setInterval(function () {
           not();
       }, 60000)

    });