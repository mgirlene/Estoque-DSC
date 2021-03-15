// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    language:{
      "lengthMenu": "Mostrar _MENU_ Resultados",
      "info": "Mostrando _START_ a _END_ de _TOTAL_ Resultados",
      "search": "Pesquisar:",
      "paginate": {
        "previous": "Anterior",
        "next": "Próximo"
      }
    }
  });
});
