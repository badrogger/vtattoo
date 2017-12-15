$(document).ready(function(){
    var indexTattoos;
    indexCardsEl = document.getElementsByClassName("card-img-top");
    // console.log(indexCardsEl);
    $.ajax({
           url: addHost_("tattoo-index/"),
           type: 'GET',
           // headers: {"Authorization": localStorage.getItem('token')}
           data: { get_param: 'value' },
           dataType: 'json',
           success: function (data) {
               // console.info(data)
               var len = 6;
               indexTattoos = data.results.slice(0, len);
               for (var i = 0; i < len; ++i) {
                    indexCardsEl[i].src = indexTattoos[i].image_file;
                    console.info(indexCardsEl[i].src);
               }

           }
        });
});
