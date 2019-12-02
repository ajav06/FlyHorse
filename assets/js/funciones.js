$(document).ready(function () {
    $(document).on('click', '.cta', function () {
        $(this).toggleClass('active')
    })
});

$(document).ready(function () {
    $('.leftmenutrigger').on('click', function (e) {
        $('.side-nav').toggleClass("open");
        e.preventDefault();
    });
});



$(document).ready(function () {
    $('#saldoB').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#saldo').addClass('active');
        $('.saldo').addClass('active');
        $('.Usuario').removeClass('d-none');
        $('.Usuario').addClass('d-flex');
        $('.sald').removeClass('active');
    });
    $('#apustRea').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#cApus').addClass('active');
        $('.cApus').addClass('active');
        $('.Usuario').removeClass('d-none');
        $('.Usuario').addClass('d-flex');
    });
    $('#inicio').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
//        $('#hp1').addClass('active');
//        $('.hp1').addClass('active');
        $('.Hipodromo').removeClass('d-none');
        $('.Hipodromo').addClass('d-flex');
    });
    $('#sd').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#saldo').addClass('active');
        $('.saldo').addClass('active');
        $('.Usuario').removeClass('d-none');
        $('.Usuario').addClass('d-flex');
    });
    $('#Transaccion').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#transac').addClass('active');
        $('.transac').addClass('active');
        $('.Usuario').removeClass('d-none');
        $('.Usuario').addClass('d-flex');
    });
    $('#Recarga').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#recar').addClass('active');
        $('.recar').addClass('active');
        $('.Usuario').removeClass('d-none');
        $('.Usuario').addClass('d-flex');
    });
    $('#Retira').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#retir').addClass('active');
        $('.retir').addClass('active');
        $('.Usuario').removeClass('d-none');
        $('.Usuario').addClass('d-flex');
    });
    $('#editU').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#personal').addClass('active');
        $('.personal').addClass('active');
        $('.Usuario').removeClass('d-none');
        $('.Usuario').addClass('d-flex');
    });
    $('#gestH').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#Chipo').addClass('active');
        $('.Chipo').addClass('active');
        $('.Gestionar').removeClass('d-none');
        $('.Gestionar').addClass('d-flex');
    });
    $('#gestC').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#Ccaba').addClass('active');
        $('.Ccaba').addClass('active');
        $('.Gestionar').removeClass('d-none');
        $('.Gestionar').addClass('d-flex');
    });
    $('#gestJd').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#Cjorn').addClass('active');
        $('.Cjorn').addClass('active');
        $('.Gestionar').removeClass('d-none');
        $('.Gestionar').addClass('d-flex');
    });
    $('#gestJk').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#Cjock').addClass('active');
        $('.Cjock').addClass('active');
        $('.Gestionar').removeClass('d-none');
        $('.Gestionar').addClass('d-flex');
    });
    $('#gestCr').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#Ccarr').addClass('active');
        $('.Ccarr').addClass('active');
        $('.Gestionar').removeClass('d-none');
        $('.Gestionar').addClass('d-flex');
    });
    $('#gestE').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#CEntr').addClass('active');
        $('.CEntr').addClass('active');
        $('.Gestionar').removeClass('d-none');
        $('.Gestionar').addClass('d-flex');
    });
    $('#gestM').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#CMone').addClass('active');
        $('.CMone').addClass('active');
        $('.Gestionar').removeClass('d-none');
        $('.Gestionar').addClass('d-flex');
    });
    $('#gestU').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#CUser').addClass('active');
        $('.CUser').addClass('active');
        $('.Gestionar').removeClass('d-none');
        $('.Gestionar').addClass('d-flex');
    });
    $('#apustAp').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#hp1').addClass('active');
        $('.hp1').addClass('active');
        $('.Hipodromo').removeClass('d-none');
        $('.Hipodromo').addClass('d-flex');
    });
    $('#apustRg').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('.Reglamento').removeClass('d-none');
        $('.Reglamento').addClass('d-flex');
    });
    $('#inclH').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#IHipo').addClass('active');
        $('.IHipo').addClass('active');
        $('.IncluirB').removeClass('d-none');
        $('.IncluirB').addClass('d-flex');
    });
    $('#inclC').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#ICaba').addClass('active');
        $('.ICaba').addClass('active');
        $('.IncluirB').removeClass('d-none');
        $('.IncluirB').addClass('d-flex');
    });
    $('#inclJd').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#IJorn').addClass('active');
        $('.IJorn').addClass('active');
        $('.IncluirB').removeClass('d-none');
        $('.IncluirB').addClass('d-flex');
    });
    $('#inclJk').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#IJock').addClass('active');
        $('.IJock').addClass('active');
        $('.IncluirB').removeClass('d-none');
        $('.IncluirB').addClass('d-flex');
    });
    $('#inclCr').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#ICarr').addClass('active');
        $('.ICarr').addClass('active');
        $('.IncluirB').removeClass('d-none');
        $('.IncluirB').addClass('d-flex');
    });
    $('#inclE').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#IEntr').addClass('active');
        $('.IEntr').addClass('active');
        $('.IncluirB').removeClass('d-none');
        $('.IncluirB').addClass('d-flex');
    });
    $('#estadHp').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#EHipo').addClass('active');
        $('.EHipo').addClass('active');
        $('.Estadistica').removeClass('d-none');
        $('.Estadistica').addClass('d-flex');
    });
    $('#estadCb').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#ECaba').addClass('active');
        $('.ECaba').addClass('active');
        $('.Estadistica').removeClass('d-none');
        $('.Estadistica').addClass('d-flex');
    });
    $('#estadRA').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#RendiApu').addClass('active');
        $('.RendiApu').addClass('active');
        $('.Estadistica').removeClass('d-none');
        $('.Estadistica').addClass('d-flex');
    });
    $('#estadJk').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#EJock').addClass('active');
        $('.EJock').addClass('active');
        $('.Estadistica').removeClass('d-none');
        $('.Estadistica').addClass('d-flex');
    });
    $('#estadRs').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#RenSis').addClass('active');
        $('.RenSis').addClass('active');
        $('.Estadistica').removeClass('d-none');
        $('.Estadistica').addClass('d-flex');
    });
    $('#estadEn').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#EEntr').addClass('active');
        $('.EEntr').addClass('active');
        $('.Estadistica').removeClass('d-none');
        $('.Estadistica').addClass('d-flex');
    });
    $('#confDp').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#ajusPer').addClass('active');
        $('.ajusPer').addClass('active');
        $('.Configuracion').removeClass('d-none');
        $('.Configuracion').addClass('d-flex');
    });
    $('#confSs').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#ajusSis').addClass('active');
        $('.ajusSis').addClass('active');
        $('.Configuracion').removeClass('d-none');
        $('.Configuracion').addClass('d-flex');
    });
    $('#btn-apt').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#sim').addClass('active');
        $('.sim').addClass('active');
        $('.TipApuestas').removeClass('d-none');
        $('.TipApuestas').addClass('d-flex');
    });
    //
    $('#tr-carrera').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#sim').addClass('active');
        $('.sim').addClass('active');
        $('.TipApuestasx2').removeClass('d-none');
        $('.TipApuestasx2').addClass('d-flex');
    });
    //
    $('#cincoy').click(function () {
        $('.OcultarTodo').removeClass('d-flex');
        $('.OcultarTodo').addClass('d-none');
        $('.Desactivar').removeClass('active');
        $('#cincoy').addClass('active');
        $('.cincoy').addClass('active');
        $('.TipApuestas').removeClass('d-none');
        $('.TipApuestas').addClass('d-flex');
    });
});


///////////////
