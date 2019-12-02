var win           = $(window),
    body          = $('body'),
    contentFP     = $('#fullpage'),
    logoHeader    = $('#logo-header'),
    tablaCentros  = $('#tabla-centros');
    // btnMenu       = $(".navbar-toggler"),
    // navbar        = $('.navbar'),
    // navbarToggler = $('.navbar-toggler span'),
    // sideMenu      = $("#sidenav-menu"),
    // linkSideMenu  = $('#sidenav-menu li'),
    // sectionInicio = $('#inicio'),
    // trabajo       = $('.trabajo'),
    // modal         = $('#modal'),
    // modalSection  = $('#modal .section'),
    // btnCloseModal = $('#btn-close'),
    // btnMas        = $("#btn-mas"),
    // btnEnviar     = $('#btn-enviar'),
    // datos         = {};

    function crearFullpage() {
        contentFP.fullpage({
            menu: '#menu',
            slidesNavigation: true,
            // scrollHorizontally: true,
            //loopBottom: true, // va al inicio luego de dar scroll en el final
            scrollOverflow: true,
            // navigation: true,
            // navigationTooltips: ['Pagina Principal', 'Iniciar Sesión'],
            // showActiveTooltip: false,
            onLeave: function (origin, destination, direction) {
                var leavingSection = this;
                    // logoHeader.addClass('hidden'); 
                    let aux = destination.index;
                    $('#menu li a').removeClass('menu-active');
                    aux = $('#menu li').get(aux);
                    $(aux).find('a').addClass('menu-active');
                    if (destination.index == 0) {
                        logoHeader.addClass('d-none');
                    }
                    if (destination.index == 2) {
                        $('.carousel').carousel(0);
                    }
            },
            afterLoad: function (origin, destination, direction) {
                var loadedSection = this;
                if (destination.index != 0) {
                    logoHeader.removeClass('d-none');
                }
            },
        });
    }

    crearFullpage();

    $(document).ready( function () {
        $('#menu li').click(function () {
            // $('#menu li a').removeClass('menu-active');
            // $(this).find('a').addClass('menu-active');
            fullpage_api.moveTo($(this).index()+1);
        });

        $('#form-iniciar').click(function() {
            $('.registrar').addClass('d-none');
            $('.recuperar').addClass('d-none');
            $('.iniciar').removeClass('d-none');
            // $('#section-iniciarSesion').attr('data-anchor', 'Iniciar_Sesion');
        });

        $('#form-registrar').click(function() {
            $('.iniciar').addClass('d-none');
            $('.recuperar').addClass('d-none');
            $('.registrar').removeClass('d-none');
            // $('#section-iniciarSesion').attr('data-anchor', 'Registrarse');
        });

        $('#form-recuperar').click(function() {
            $('.iniciar').addClass('d-none');
            $('.registrar').addClass('d-none');
            $('.recuperar').removeClass('d-none');
            // $('#section-iniciarSesion').attr('data-anchor', 'Recuperar_Contraseña');
        });

        tablaCentros.DataTable({
            "info":     false,
            "ordering": false,
            "pagingType": "simple",
            "lengthChange": false,
            "pageLength": 3,
            "language": {
                "sProcessing":     "Procesando...",
                "sLengthMenu":     "Mostrar _MENU_ registros",
                "sZeroRecords":    "No se encontraron resultados",
                "sEmptyTable":     "Ningún dato disponible en esta tabla",
                "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
                "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
                "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
                "sInfoPostFix":    "",
                "sSearch":         "Buscar:",
                "sUrl":            "",
                "sInfoThousands":  ",",
                "sLoadingRecords": "Cargando...",
                "oPaginate": {
                    "sFirst":    "Primero",
                    "sLast":     "Último",
                    "sNext":     '<i class="fas fa-angle-right"></i>',
                    "sPrevious": '<i class="fas fa-angle-left"></i>',
                },
                "oAria": {
                    "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                    "sSortDescending": ": Activar para ordenar la columna de manera descendente"
                }
            }
        });
    });

    ///////////////////////////Albert

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
            $('.Usuari').removeClass('d-none');
            $('.Usuari').addClass('d-flex');
            $('.sald').removeClass('active');
        });
        $('#apustRea').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#cApus').addClass('active');
            $('.cApus').addClass('active');
            $('.Usuari').removeClass('d-none');
            $('.Usuari').addClass('d-flex');
        });
        $('#inicio').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            //$('#hp1').addClass('active');
            //$('.hp1').addClass('active');
            $('.Hipodro').removeClass('d-none');
            $('.Hipodro').addClass('d-flex');
        });
        $('#sd').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#saldo').addClass('active');
            $('.saldo').addClass('active');
            $('.Usuari').removeClass('d-none');
            $('.Usuari').addClass('d-flex');
        });
        $('#Transaccion').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#transac').addClass('active');
            $('.transac').addClass('active');
            $('.Usuari').removeClass('d-none');
            $('.Usuari').addClass('d-flex');
        });
        $('#Recarga').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#recar').addClass('active');
            $('.recar').addClass('active');
            $('.Usuari').removeClass('d-none');
            $('.Usuari').addClass('d-flex');
        });
        $('#Retira').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#retir').addClass('active');
            $('.retir').addClass('active');
            $('.Usuari').removeClass('d-none');
            $('.Usuari').addClass('d-flex');
        });
        $('#editU').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#personal').addClass('active');
            $('.personal').addClass('active');
            $('.Usuari').removeClass('d-none');
            $('.Usuari').addClass('d-flex');
        });
        $('#gestH').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#Chipo').addClass('active');
            $('.Chipo').addClass('active');
            $('.Gestion').removeClass('d-none');
            $('.Gestion').addClass('d-flex');
        });
        $('#gestC').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#Ccaba').addClass('active');
            $('.Ccaba').addClass('active');
            $('.Gestion').removeClass('d-none');
            $('.Gestion').addClass('d-flex');
        });
        $('#gestJd').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#Cjorn').addClass('active');
            $('.Cjorn').addClass('active');
            $('.Gestion').removeClass('d-none');
            $('.Gestion').addClass('d-flex');
        });
        $('#gestJk').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#Cjock').addClass('active');
            $('.Cjock').addClass('active');
            $('.Gestion').removeClass('d-none');
            $('.Gestion').addClass('d-flex');
        });
        $('#gestCr').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#Ccarr').addClass('active');
            $('.Ccarr').addClass('active');
            $('.Gestion').removeClass('d-none');
            $('.Gestion').addClass('d-flex');
        });
        $('#gestE').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#CEntr').addClass('active');
            $('.CEntr').addClass('active');
            $('.Gestion').removeClass('d-none');
            $('.Gestion').addClass('d-flex');
        });
        $('#gestM').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#CMone').addClass('active');
            $('.CMone').addClass('active');
            $('.Gestion').removeClass('d-none');
            $('.Gestion').addClass('d-flex');
        });
        $('#gestU').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#CUser').addClass('active');
            $('.CUser').addClass('active');
            $('.Gestion').removeClass('d-none');
            $('.Gestion').addClass('d-flex');
        });
        $('#apustAp').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#hp1').addClass('active');
            $('.hp1').addClass('active');
            $('.Hipodro').removeClass('d-none');
            $('.Hipodro').addClass('d-flex');
        });
        $('#apustRg').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('.Reglamen').removeClass('d-none');
            $('.Reglamen').addClass('d-flex');
        });
        $('#inclH').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#IHipo').addClass('active');
            $('.IHipo').addClass('active');
            $('.Inclu').removeClass('d-none');
            $('.Inclu').addClass('d-flex');
        });
        $('#inclC').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#ICaba').addClass('active');
            $('.ICaba').addClass('active');
            $('.Inclu').removeClass('d-none');
            $('.Inclu').addClass('d-flex');
        });
        $('#inclJd').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#IJorn').addClass('active');
            $('.IJorn').addClass('active');
            $('.Inclu').removeClass('d-none');
            $('.Inclu').addClass('d-flex');
        });
        $('#inclJk').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#IJock').addClass('active');
            $('.IJock').addClass('active');
            $('.Inclu').removeClass('d-none');
            $('.Inclu').addClass('d-flex');
        });
        $('#inclCr').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#ICarr').addClass('active');
            $('.ICarr').addClass('active');
            $('.Inclu').removeClass('d-none');
            $('.Inclu').addClass('d-flex');
        });
        $('#inclE').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#IEntr').addClass('active');
            $('.IEntr').addClass('active');
            $('.Inclu').removeClass('d-none');
            $('.Inclu').addClass('d-flex');
        });
        $('#estadHp').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#EHipo').addClass('active');
            $('.EHipo').addClass('active');
            $('.Estadist').removeClass('d-none');
            $('.Estadist').addClass('d-flex');
        });
        $('#estadCb').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#ECaba').addClass('active');
            $('.ECaba').addClass('active');
            $('.Estadist').removeClass('d-none');
            $('.Estadist').addClass('d-flex');
        });
        $('#estadRA').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#RendiApu').addClass('active');
            $('.RendiApu').addClass('active');
            $('.Estadist').removeClass('d-none');
            $('.Estadist').addClass('d-flex');
        });
        $('#estadJk').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#EJock').addClass('active');
            $('.EJock').addClass('active');
            $('.Estadist').removeClass('d-none');
            $('.Estadist').addClass('d-flex');
        });
        $('#estadRs').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#RenSis').addClass('active');
            $('.RenSis').addClass('active');
            $('.Estadist').removeClass('d-none');
            $('.Estadist').addClass('d-flex');
        });
        $('#estadEn').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#EEntr').addClass('active');
            $('.EEntr').addClass('active');
            $('.Estadist').removeClass('d-none');
            $('.Estadist').addClass('d-flex');
        });
        $('#confDp').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#ajusPer').addClass('active');
            $('.ajusPer').addClass('active');
            $('.Configu').removeClass('d-none');
            $('.Configu').addClass('d-flex');
        });
        $('#confSs').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#ajusSis').addClass('active');
            $('.ajusSis').addClass('active');
            $('.Configu').removeClass('d-none');
            $('.Configu').addClass('d-flex');
        });
        $('#btn-apt').click(function () {
            $('.OcultarTodo').removeClass('d-flex');
            $('.OcultarTodo').addClass('d-none');
            $('.Desactivar').removeClass('active');
            $('#sim').addClass('active');
            $('.sim').addClass('active');
            $('.TipApta').removeClass('d-none');
            $('.TipApta').addClass('d-flex');
        });
    });

    function alerta() {
        var mensaje;
        var opcion = confirm("Click en Aceptar o Cancelar");
        if (opcion == true) {
            mensaje = "Has clickado OK";
        } else {
            mensaje = "Has clickado Cancelar";
        }
        document.getElementById("ejemplo").innerHTML = mensaje;
    }

    ///////////////
