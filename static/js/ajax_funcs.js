
// Магія розпочнеться лише після повного завантаження сторінки
   $(document).ready(function () {
       // Посилання з id="test" буде тригером події
       $(document.getElementsByClassName("ajax_adding")).click(function() {
           // AJAX-запит на потрібну адресу
           $.get("/ajax/", function(data) {
               // Замінюємо текст тегу з id="target" на отримані дані
               $(document.getElementsByClassName("target")).html(data.param1+' '+data.param2);
           });
       });
   });
