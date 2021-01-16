const telefono = $('input[name=telefono]');
const cp = $('input[name=cp]');

telefono.mask('(000)000-0000');
cp.mask('00000');

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