var Lang = $("#zd_locale").html().substring(0,2);
if (Lang == 'uk') {
  $.extend( $.validator.messages, {
  	required: "Це поле необхідно заповнити.",
  	remote: "Будь ласка, введіть правильне значення.",
  	email: "Будь ласка, введіть коректну адресу електронної пошти.",
  	url: "Будь ласка, введіть коректний URL.",
  	date: "Будь ласка, введіть коректну дату.",
  	dateISO: "Будь ласка, введіть коректну дату у форматі ISO.",
  	number: "Будь ласка, введіть число.",
  	digits: "Вводити потрібно лише цифри.",
  	creditcard: "Будь ласка, введіть правильний номер кредитної карти.",
  	equalTo: "Будь ласка, введіть таке ж значення ще раз.",
  	extension: "Будь ласка, виберіть файл з правильним розширенням.",
  	maxlength: $.validator.format( "Будь ласка, введіть не більше {0} символів." ),
  	minlength: $.validator.format( "Будь ласка, введіть не менше {0} символів." ),
  	rangelength: $.validator.format( "Будь ласка, введіть значення довжиною від {0} до {1} символів." ),
  	range: $.validator.format( "Будь ласка, введіть число від {0} до {1}." ),
  	max: $.validator.format( "Будь ласка, введіть число, менше або рівно {0}." ),
  	min: $.validator.format( "Будь ласка, введіть число, більше або рівно {0}." )
  } );
}

if (Lang == 'ru') {
  $.extend( $.validator.messages, {
  	required: "Это поле необходимо заполнить.",
  	remote: "Пожалуйста, введите правильное значение.",
  	email: "Пожалуйста, введите корректный адрес электронной почты.",
  	url: "Пожалуйста, введите корректный URL.",
  	date: "Пожалуйста, введите корректную дату.",
  	dateISO: "Пожалуйста, введите корректную дату в формате ISO.",
  	number: "Пожалуйста, введите число.",
  	digits: "Пожалуйста, вводите только цифры.",
  	creditcard: "Пожалуйста, введите правильный номер кредитной карты.",
  	equalTo: "Пожалуйста, введите такое же значение ещё раз.",
  	extension: "Пожалуйста, выберите файл с правильным расширением.",
  	maxlength: $.validator.format( "Пожалуйста, введите не больше {0} символов." ),
  	minlength: $.validator.format( "Пожалуйста, введите не меньше {0} символов." ),
  	rangelength: $.validator.format( "Пожалуйста, введите значение длиной от {0} до {1} символов." ),
  	range: $.validator.format( "Пожалуйста, введите число от {0} до {1}." ),
  	max: $.validator.format( "Пожалуйста, введите число, меньшее или равное {0}." ),
  	min: $.validator.format( "Пожалуйста, введите число, большее или равное {0}." )
  } );
}

if (Lang == 'en') {
  $.extend( $.validator.messages, {
    required: "This field is required.",
    remote: "Please fix this field.",
    email: "Please enter a valid email address.",
    url: "Please enter a valid URL.",
    date: "Please enter a valid date.",
    dateISO: "Please enter a valid date (ISO).",
    number: "Please enter a valid number.",
    digits: "Please enter only digits.",
    creditcard: "Please enter a valid credit card number.",
    equalTo: "Please enter the same value again.",
    accept: "Please enter a value with a valid extension.",
    maxlength: jQuery.validator.format("Please enter no more than {0} characters."),
    minlength: jQuery.validator.format("Please enter at least {0} characters."),
    rangelength: jQuery.validator.format("Please enter a value between {0} and {1} characters long."),
    range: jQuery.validator.format("Please enter a value between {0} and {1}."),
    max: jQuery.validator.format("Please enter a value less than or equal to {0}."),
    min: jQuery.validator.format("Please enter a value greater than or equal to {0}.")
  } );
}

$("#form-tour").validate({
    rules: {
        username: {
            required: true,
            minlength: 3
        },
        tel_user_phone: {
            required: true,
            digits: true,
            minlength: 10
        },
        user_email: {
            required: true,
            email: true
        },
        tour_name: {
            required: true
        },
        date_entry: {
            required: true
        },
        number_of_people: {
            required: true,
            min: 1
        },
        user_comment: {
            maxlength: 300
        }
    },
    onsubmit: true,
    focusCleanup: true,
    focusInvalid: false
});

$( function() {
  var Lang = $("#zd_locale").html().substring(0,2);
    $( "#id_date_entry" ).datepicker( $.datepicker.regional[ Lang ] );
  } );

$("input").addClass("form-control");
$("textarea").addClass("form-control");
$("select#id_tour_name").addClass("form-control");
