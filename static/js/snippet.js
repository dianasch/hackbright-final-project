"use strict";
// alert('This is my js code')


$(document).ready(function() {
    $('#user-album-form').click(function(evt) {
        console.log(evt);
        evt.preventDefault();

        $.ajax({

            url: "user-album-form",

            type: "GET",

            dataType: 'html',

            success: (res) => {
                $('#show-user-form').html(res);
            }
        });

    });
});

$(document).ready(function() {
    $('#user-album-upload').submit(function(evt) {
        evt.preventDefault();

        const requestArgs = {
            'thumbnail': $('input[name="thumbnail"]').val()
        }

        const extensions = [".bmp", ".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".tif", ".tiff", ".ico", ".cur"];

        const thumbnailURL = requestArgs['thumbnail'];

        $.ajax({
        type: "HEAD",
        url : requestArgs['thumbnail'],
        success: function(message,text,response){

            console.log(response);
            console.log(response.getResponseHeader('Content-Type'));
            console.log(text);
            console.log(response.getResponseHeader('Content-Type').indexOf("image"));
            if (response.getResponseHeader('Content-Type').indexOf("image") === -1){

                for (const extension of extensions) {
                    if (thumbnailURL.indexOf(extension) !== -1) {
                        alert("Oops! Not a valid image! Please submit a valid link for your album thumbnail.");

                        return;
                    }
                }
                
                alert("Oops! Not a valid image! Please submit a valid link for your album thumbnail.");
            }
            else {
                evt.currentTarget.submit();
            }
        
        }
        }); 
    });
});

