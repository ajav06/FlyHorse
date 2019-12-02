var tablaTransacciones  = $('#tabla-transacciones').DataTable({
    "dom": '<"top"i>rt<"bottom">p<"clear">',
    "info":     false,
    "ordering": true, 
    "order": [[ 0, "desc" ]],
    "pagingType": "simple_numbers",
    "lengthChange": false,
    "pageLength": 4,
    "fixedHeader": true,
    "language": {
        "searchPlaceholder": "Buscar registro",
        "sProcessing":     "Procesando...",
        "sLengthMenu":     "Mostrar _MENU_ registros",
        "sZeroRecords":    "No se encontraron resultados",
        "sEmptyTable":     "Ningún dato disponible en esta tabla",
        "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
        "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
        "sInfoPostFix":    "",
        "sSearch":         "",
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
    },
});

$.fn.dataTableExt.afnFiltering.push(
    function( settings, data, dataIndex ) {
        
        var min  = $('#min-date').val()
        var max  = $('#max-date').val()
        var createdAt = data[0] || 0; // Our date column in the table
        var diffDate = moment(createdAt);
        min = moment(min).subtract('1','days');
        max = moment(max).add('1','days');
        if (
        (min == "" || max == "") ||
        (diffDate.isBetween(min, max))


        ) {  return true;  }
        return false;

    }
);

$('#min-date').change(function() {
    tablaTransacciones.draw();
});

$('#max-date').change(function() {
    tablaTransacciones.draw();
});

$('#filtrardescripcion').change(function() {
    tablaTransacciones.search(this.value).draw();
});