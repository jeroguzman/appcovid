const telefono = $('input[name=telefono], input[name=username]');
const cp = $('input[name=cp]');

cp.mask('00000');

$('button[type=submit], input[type=submit]').each(function () {
    $(this).click(function () {
        telefono.unmask();
    });
})

if (telefono.unmask()) {
    telefono.mask('(000)000-0000');
}

function alphaOnly(event) {
    var key = event.keyCode;
    return (key == 8 //Backspace
        || (key >= 65 && key <= 90) //Letters
        || key == 9 //Tab
        || key == 32 //Space
        || key == 109 // -
        || key == 192 //ñ
        || key == 219 // '
    );
};

