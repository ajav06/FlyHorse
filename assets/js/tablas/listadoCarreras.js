var tablaCarreras = $('#tabla-carreras').DataTable({
    "dom": '<"top"i>rt<"bottom">p<"clear">',
    "info": false,
    "ordering": true,
    "order": [
        [0, "desc"]
    ],
    "pagingType": "simple_numbers",
    "lengthChange": false,
    "pageLength": 4,
    "fixedHeader": true,
    "language": {
        "searchPlaceholder": "Buscar registro",
        "sProcessing": "Procesando...",
        "sLengthMenu": "Mostrar _MENU_ registros",
        "sZeroRecords": "No se encontraron resultados",
        "sEmptyTable": "Ningún dato disponible en esta tabla",
        "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
        "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
        "sInfoPostFix": "",
        "sSearch": "",
        "sUrl": "",
        "sInfoThousands": ",",
        "sLoadingRecords": "Cargando...",
        "oPaginate": {
            "sFirst": "Primero",
            "sLast": "Último",
            "sNext": '<i class="fas fa-angle-right"></i>',
            "sPrevious": '<i class="fas fa-angle-left"></i>',
        },
        "oAria": {
            "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
        }
    },
});

$('#filtrarestatus').change(function () {
    tablaCarreras.search(this.value).draw();
});