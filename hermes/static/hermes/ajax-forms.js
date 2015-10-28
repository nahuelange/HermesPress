$.fn.ajaxform = function(){
    return this.each(function(){
        $.ajax({
            type: $(this).attr('method'),

        })
    })
}


