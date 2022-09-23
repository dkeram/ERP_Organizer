$(document).ready(function() { 
    var myModal = new bootstrap.Modal(document.getElementById('loadingModal'));
    $('body').on('click','#clients tbody tr',function(){
        var clientId = $(this).data("id");
        var csrf = $('input[name=csrfmiddlewaretoken').val();
        
        myModal.show();
        //console.log(clientId, csrf);
       
        $.ajax($(this).attr('action'),{
            type:'POST',
            data: {
                csrfmiddlewaretoken:csrf,
                clientId:clientId,
            }
        }).done((data)=>{
            console.log('Ajax returned', data)
            myModal.hide();
        })
    })


});