var mail_icon = document.getElementById('mail-icon');
var copy_mail_confirm = document.getElementById('copy-mail-confirm');

function CopyString(text, object) {
    // Create new element
    var el = document.createElement('textarea');

    // Set value (string to be copied)
    el.value = text;

    // Set non-editable to avoid focus and move outside of view
    el.setAttribute('readonly', '');
    el.style = {position: 'absolute', left: '-9999px'};
    document.body.appendChild(el);

    // Select text inside element
    el.select();

    // Copy text to clipboard
    document.execCommand('copy');

    // Remove temporary element
    document.body.removeChild(el);

    /* Confirm */
    object.style.display = 'block';

    setTimeout(function(){
        object.style.display = 'none';
    }, 1000);
};


mail_icon.onclick = function(){
    CopyString('bartoszjanjerzy@gmail.com', copy_mail_confirm);
};