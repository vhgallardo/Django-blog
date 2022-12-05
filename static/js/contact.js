$(document).ready(function(){
    
    (function($) {
        "use strict";

    
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value)
    }, "type the correct answer -_-");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                subject: {
                    required: true,
                    minlength: 4
                },
                number: {
                    required: true,
                    minlength: 5
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true,
                    minlength: 20
                }
            },
            messages: {
                name: {
                    required: "Ingresa tu nombre",
                    minlength: "Tu nombre debe tener al menos 2 carácteres"
                },
                subject: {
                    required: "Ingresa el asunto",
                    minlength: "El asunto debe tener al menos 4  carácteres"
                },
                number: {
                    required: "come on, you have a number, don't you?",
                    minlength: "your Number must consist of at least 5 characters"
                },
                email: {
                    required: "Ingresa tu correo"
                },
                message: {
                    required: "Ingresa un mensaje",
                    minlength: "thats all? really?"
                }
            },
            
        })
    })
        
 })(jQuery)
})