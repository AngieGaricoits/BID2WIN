var btnAbrirPopup = document.getElementById('btn-abrir-popup'),
    overlay = document.getElementById('overlay'),
    popup= document.getElementById('popup'),
    btnCerrarPopup = document.getElementById('btn-cerrar-popup');

btnAbrirPopup.addEventListener ('click', function(){
   overlay.classList.add('active')
});

btnCerrarPopup.addEventListener ('click', function(){
   overlay.classList.remove('active');
});

var btnAbrirPopup2 = document.getElementById('btn-abrir-popup2'),
    overlay2 = document.getElementById('overlay2'),
    popup2= document.getElementById('popup2'),
    btnCerrarPopup2 = document.getElementById('btn-cerrar-popup2');


function popupEdit(login_supplier, email, company){
    document.getElementById("edit_login_supplier").value = login_supplier;
    document.getElementById("edit_email").value = email;
    document.getElementById("edit_company").value = company;
    document.getElementById("formPopUp").action = '/suppliers/'+login_supplier+'/editar';
    overlay2.classList.add('active');
}

btnCerrarPopup2.addEventListener ('click', function(){
   overlay2.classList.remove('active');
});

var btnAbrirPopup3 = document.getElementById('btn-abrir-popup3'),
    overlay3 = document.getElementById('overlay3'),
    popup3= document.getElementById('popup3'),
    btnCerrarPopup3 = document.getElementById('btn-cerrar-popup3');


function popupEdit(login_supplier, email, company){
    document.getElementById("edit_login_supplier").value = login_supplier;
    document.getElementById("edit_email").value = email;
    document.getElementById("edit_company").value = company;
    document.getElementById("formPopUp").action = '/suppliers/'+login_supplier+'/editar';
    overlay2.classList.add('active');
}

btnCerrarPopup2.addEventListener ('click', function(){
   overlay2.classList.remove('active');
});

function editQuote(brand, group, style, quantity, supplier, status, dead_line, comments ){
    document.getElementById("edit_brand").value = brand;
    document.getElementById("edit_group").value = group;
    document.getElementById("edit_style").value = style;
    document.getElementById("edit_quantity").value = quantity;
    document.getElementById("edit_supplier").value = supplier;
    document.getElementById("edit_status").value = status;
    document.getElementById("dead_line").value = dead_line;
    document.getElementById("edit_comments").value = comments;
    document.getElementById("editQuote").action = '/quotations/'+id_quote+'/editar';
    overlay2.classList.add('active');
}
